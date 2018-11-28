#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)));
#define two(x) ((1)<<(x))
#define biti(a,i) (((a)>>(i)) & 1)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define foreach(i,a,b) for(int i=a;i<=b;i++)
#define rep(i,n) REP(i,0,n)
#define SIZE(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)
#define rint(x) scanf("%d",&x)
#define rdbl(x) scanf("%lf",&x)
#define OUT(x) (cout << #x << " = " << x << endl)
#define  pi  acos(-1)

typedef pair<int,int> PI;
typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
template <class T> void out(T x, int n){  for(int i = 1; i <= n; ++i)  cout <<setw(3)<< x[i] << ' ';    cout << endl;    }
template <class T> void out(T x, int n, int m){  for(int i = 1; i <= n; ++i)    out(x[i], m);    cout << endl;    }
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}

const int INF=1000000000;

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
	bool operator >(const Int& ) const ;

	int digital[maxNum];
	int sign;
	int len;
	//十进制移位.
	Int shift(int k); // 除法时要用到.
};

bool Int::operator >(const Int& a) const
{
	int i;
	if (len > a.len) return 1;
	if (len < a.len) return 0;
	for (i = len; i >= 0; i--)
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

bool cmp(const Int& a,const Int& b){
    return b>a;
}

const int AMAX=1005;
Int A[AMAX];
int acnt;
Int B[AMAX];

int main(){
//    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int go;
    rint(go);
    for(int gg=1;gg<=go;gg++){
        rint(acnt);
        rep(i,acnt){
            cin>>A[i];
        }
        sort(A,A+acnt,cmp);
        foreach(i,1,acnt-1){
            B[i]=A[i]-A[i-1];
        }
        Int k=B[1];
        foreach(i,1,acnt-1){
            k=gcd(B[i],k);
        }
        Int ans;
        ans.digital[0]=0;
        ans.len=0;
        rep(i,acnt){
            Int t=A[i]/k;
            Int mod=A[i]-k*t;
            if(mod.zero()==0)
                t=k-mod;
            else t=mod;
            if(t>ans){
                ans=t;
            }
        }
//        rep(i,acnt){
//            Int t=A[i]+ans;
//            if(0==(t%k).zero())cout<<"FAIL"<<endl;
//        }
        cout<<"Case #"<<gg<<": "<<ans<<endl;
    }
	return 0;
}
