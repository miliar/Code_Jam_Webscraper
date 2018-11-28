#include <iostream> // 这里不能用using namespace std;
#include <string>
using namespace std;
const int maxNum = 130;
const int base = 10000;
const int baselen = 4;
int countnub = 0;

// 此大整数类用数组digital[maxNum]表示一个大整数;
// 一个digital表示最大为9999;
// len表示目前整数的用到最大digital位,sign表示符号;

class Int
{
public:
	// 构造函数.
	int getlen(){return len;}
/**/Int() { digital[len = 0] = 0, sign = 1;}
	// 比较函数,第二个参数为0则表示绝对值比较.
	int cmp(Int ,int );
	// 判断是否为0.
	bool zero() { return digital[0] == 0 && len == 0; }
	// 判定奇偶性.
	bool odd() { return digital[0] & 1; }
	// 右移一个二进制位.
	Int move();
	// 赋值重载.
/**/Int operator = (int);
/**/Int operator = (Int );
	Int operator = (char *);
	// 双目运算重载.
/**/Int operator +(Int );
/**/Int operator -(Int );
/**/Int operator *(Int );
/**/Int operator /(Int );
/**/Int operator %(Int );
	bool operator >(Int );

	//输入输出.
	friend ostream& operator <<(ostream&, Int );
	friend istream& operator >>(istream& ,Int& );
//private :
	int digital[maxNum];
	int sign;
	int len;
	//十进制移位.
	Int shift(int k); // 除法时要用到.
};

bool Int::operator >(Int a)
{
	int i;
	if (len > a.len) return 1;
	if (len < a.len) return 0;
	for (i = len; i >= 1; i--)
	{
		if (digital[i] > a.digital[i]) return 1;
		if (digital[i] < a.digital[i]) return 0;
	}
	return 0;
}

// 比较函数,第二个参数为0则表示绝对值比较.
int Int::cmp(Int obj, int sel = 1)
{
	if (sel && obj.sign + sign == 0) return sign - obj.sign; // 比较正负号;
	int k = len - obj.len; //比较长度;
	if (k) return sel ? sign*k : k;
	for (k = len; k > 0 && obj.digital[k] == digital[k]; k--); // 比较数位;
	return sel ? sign * ( digital[k] - obj.digital[k] ): digital[k]-obj.digital[k];
}

// 右移一个二进制位.
Int Int::move()
{
	if (digital[0] <= 1 && len == 0) digital[0] = 0;
	else
	{
		int k = len, t, carry = 0;
		if (digital[len] == 1) len--;
		while(k >= 0)
		{
			t = digital[k] & 1;
			digital[k] = digital[k] >> 1;
			if (carry) digital[k] += base / 2;
			k--;
			carry = t;
		}
	}
	if( this->zero() ) sign = 1;
	return *this;
}


///////////////////////////////////////////////////////////////////////////////////
// 赋值重载.

// Int 初始化 Int.
Int Int::operator =(Int obj)
{
	for(len = 0, sign = obj.sign; len <= obj.len; len++) digital[len] = obj.digital[len];
	len--;
	return *this;
}
// int 初始化 Int.
Int Int::operator = (int obj)
{
	if(obj<0) sign = -1, obj = -obj;
	else sign = 1;
	digital[0] = obj % base;
	if(obj /= base)
	{
		digital[1] = obj % base, len = 1;
		if (obj /= base) digital[2] = obj % base, len = 2;
	}
	else len = 0;
	return *this;
}
// char* 初始化 Int.
Int Int::operator = (char *s)
{
	int i, j, l, k;
	if (s[0] == '-') l = 1, sign = -1;
	else l = 0, sign = 1;
	i = l;
	while (s[i]) i++;
	i--;
	k = 0;
	while (i - baselen + 1 >= l)
	{
		for (j = 1, digital[k] = 0; j <= baselen; j++) digital[k] = digital[k] * 10 + s[i - baselen + j] - '0';
		i = i - baselen;
		k++;
	}
	digital[k] = 0;
	while (i >= l) digital[k] = digital[k] * 10 + s[l++] - '0';
	if (k) len = k - (digital[k] == 0);
	else len = 0;
	while (len > 0 && digital[len] == 0) len--; // 去掉前置的0.
	return *this;
}

/////////////////////////////////////////////////////////////////

// 双目运算重载.
Int Int::operator +(Int obj)
{
	Int sum;
	if(obj.sign==sign)
	{ // 同号加;
		int carry;
		int i;
		for (i = carry = 0; i <= len && i <= obj.len; i++)
		{
			carry = carry + digital[i] + obj.digital[i];
			sum.digital[i]  = carry%base;
			carry = carry/base;
		}
		for(; i <= len; i++)
		{
			carry = carry + digital[i];
			sum.digital[i]  = carry%base;
			carry = carry/base;
		}
		for(; i <= obj.len; i++)
		{
			carry = carry + obj.digital[i];
			sum.digital[i]  = carry%base;
			carry = carry/base;
		}
		sum.len = i - !(sum.digital[i] = carry);
		sum.sign = sign;
		return sum;
	}
	else
	{ // 异号变同号减法，这里要用到减法的重载.
		sum = obj;
		sum.sign = -sum.sign;
		return *this - sum;
	}
}

Int Int::operator -(Int obj)
{
	Int *sub1, *sub2, quotient;
	if (sign==obj.sign)
	{ //同号减;
		int i, carry;
		i = this->cmp(obj,0); // 绝对值比较;
		if (i==0) return quotient;
		else if (i<0) { sub1 = &obj; sub2 = this; quotient.sign = -sign; }
		else { sub1 = this; sub2 = &obj; quotient.sign = sign; }
		for	(i = carry = 0; i <= sub2->len; i++)
			if( (quotient.digital[i] = sub1 ->digital[i] - carry - sub2->digital[i]) < 0)
				{ carry = 1; quotient.digital[i] += base; } //借位;
			else carry = 0;
		for(; i <= sub1->len; i++)
			if( (quotient.digital[i] = sub1 ->digital[i] - carry ) < 0 ) {carry = 1, quotient.digital[i] += base; }//借位;
		else carry = 0;
		i--;
		while(i && quotient.digital[i]==0) i--;
		quotient.len = i;
		return quotient;
	}
	else
	{ //异号变同号加，这里要用到加法的重载
		quotient = obj; quotient.sign = -obj.sign;
		return *this + quotient;
	}
}

Int Int::operator *(Int obj)
{
	int carry, i, j, maxlen;
	Int product;
	maxlen = obj.len + len + 2;
	memset (product.digital, 0, sizeof(int) * maxlen );
	for(i = 0; i <= obj.len; i++)
	{
		for(j = 0, carry = 0; j <= len; j++)
		{
			carry += obj.digital[i] * digital[j] + product.digital[j + i];
			product.digital[j + i] = carry % base;
			carry /= base;
		}
		while (carry) { product.digital[i+j++] = carry % base; carry /= base; }
	}
	i = maxlen-1;
	while (i && product.digital[i] == 0) i--;
	product.len = i;
	if (product.zero()) product.sign = 1; //确定符号
	else product.sign = sign * obj.sign;
	return product;
}

Int Int::operator /(Int obj)
{
	int div, k, flag;
	Int x, y, z;
	x = *this;
	flag = obj.sign * sign;
	obj.sign = x.sign = 1;
	while( x.cmp(obj) >0 )
	{
		k = x.len-obj.len;
		if ( x.digital[x.len] > obj.digital[obj.len] ) div = x.digital[x.len] / (obj.digital[obj.len] + 1);
		else if (x.len>obj.len) { k--; div = (x.digital[x.len] * base + x.digital[x.len - 1]) / (obj.digital[obj.len] + 1); }
		else break;
		x = x - ( obj * (z = div) ).shift(k);
		y = y + z.shift(k);
	}
	if (x.cmp(obj) >= 0) y = y + (z = 1);
	if (y.zero()) y.sign = 1;
	else y.sign = flag;
	return y;
}

Int Int::operator %(Int obj)
{
	int div,  k;
	Int x, y, z;
	x = *this;
	obj.sign = x.sign = 1;
	while( x.cmp(obj) > 0 )
	{
		k = x.len-obj.len;
		if ( x.digital[x.len] > obj.digital[obj.len] ) div = x.digital[x.len] / (obj.digital[obj.len] + 1);
		else if (x.len>obj.len) { k--; div = (x.digital[x.len] * base + x.digital[x.len-1]) / (obj.digital[obj.len] + 1); }
		else break;
		x = x - ( obj * (z = div) ).shift(k);
	}
	if (x.cmp(obj) >= 0) x = x - obj;
	if (x.zero()) x.sign = 1;
	else x.sign = sign;
	return x;
}

Int Int::shift(int k)
{
	Int temp;
	int i;
	temp = *this;
	for (i = 0; i <= len; i++) temp.digital[i + k] = digital[i];
	for (i = 0; i < k; i++) temp.digital[i] = 0;
	temp.sign = sign;
	temp.len = len + k;
	return temp;
}

///////////////////////////////////////////////////////////////////////

ostream& operator <<(ostream& out , Int obj)
{
	int i = obj.len;
	if (obj.sign == -1) out << '-';
	out << obj.digital[i--];
	out.fill('0');
	out.setf(ios::right);
	while (i >= 0)
	{
		out.width(baselen);
		out << obj.digital[i--];
	}
	return out;
}

istream& operator >>(istream& in,Int& obj)
{
	char s[baselen * maxNum];
	in >> s;
	obj = s;
	return in;
}

Int gcd(Int a,Int b)
{
	if(a.zero()) return b;
	if(b.zero()) return a;
	if(a.cmp(b,0)) return gcd(b, a % b);
	return gcd(a, b % a);
}
Int g;
int n;
Int num[1005];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("hand.txt","w",stdout);
	int t;
	int cas=1;
	scanf("%d",&t);
	while(t--)
	{
	    scanf("%d",&n);
	    int i;
	    for(i=1;i<=n;i++)
            cin>>num[i];
        g=0;
        int j;
        for(i=1;i<=n;i++)
            for(j=i+1;j<=n;j++)
            {
                if(num[i]>num[j])
                    g=gcd(num[i]-num[j],g);
                else
                    g=gcd(num[j]-num[i],g);
                //cout<<g<<endl;
            }
        //cout<<g<<endl;
        //cout<<temp<<endl;
        //cout<<temp.getlen()<<' '<<temp.digital[3]<<endl;
        Int temp=num[1]%g;
        if(!temp.zero())
        {
            //cout<<"yes"<<endl;
            cout<<"Case #"<<cas++<<": "<<g-num[1]%g<<endl;
            //cout<<g-num[1]%g<<endl;
        }
        else cout<<"Case #"<<cas++<<": 0"<<endl;

	}
	return 0;
}
