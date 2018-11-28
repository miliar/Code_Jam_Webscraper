#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
namespace Me
{
	using namespace std;
	const int MAXN = 9999;//每个单元存储的最大数
	const int DLEN = 4;//每个数据存储的数据位
	const int DIGIT = 2500;//位数
	
	// 数字在该类中每四位逆序存放。
	// 实现了加减乘除着四个最基本的运算。
	// 乘法的时间复杂度为)O(n^2)
	// 以后会把它改成更加快的傅立叶变换
	class BigNum 
	{
	public:
		BigNum() : len(1) { memset(a, 0, sizeof(a)); }
		BigNum(int );
		BigNum(const char []);
		BigNum(const BigNum &);
		BigNum &operator=(const BigNum &);
		BigNum operator+(const BigNum &) const;
		BigNum operator-(const BigNum &) const;
		BigNum operator*(const BigNum &) const;
		BigNum operator/(const int) const;
		friend ostream & operator<<(ostream &os, const BigNum &n);
		friend istream & operator>>(istream &is, const BigNum &n);
		int a[DIGIT];
		int len;
	};
	BigNum::BigNum(int n)
	{
		len = 0;
		memset(a, 0, sizeof(a));
		while (n) {
			a[len++] = n % (1 + MAXN);
			n /= (1 + MAXN);
		}
		if (len == 0) len = 1;
	}
	BigNum::BigNum(const char s[])
	{
		int j, m, n;
		
		len = 0;
		memset(a, 0, sizeof(a));
		for (n = strlen(s) - 1; n >= 0; n -= 4) {
			m = 0;
			if ((j = n - 3) < 0) j = 0;
			while (j <= n) m = m * 10 + s[j++] - '0';
			a[len++] = m;
		}
	}
	BigNum::BigNum(const BigNum &n)
	{
		*this = n;
	}
	BigNum &BigNum::operator=(const BigNum &n)
	{
		int i;
		
		len = n.len;
		memset(a, 0, sizeof(a));
		for (i = 0; i < len; i++) a[i] = n.a[i];
		return *this;
	}
	BigNum BigNum::operator+(const BigNum &n) const
	{
		BigNum t;
		int i, blen;
		
		blen = len > n.len ? len : n.len;
		for (i = 0; i < blen; i++) {
			t.a[i] += a[i] + n.a[i];
			if (t.a[i] > MAXN) {
				t.a[i + 1]++;
				t.a[i] -= (MAXN + 1);
			}
		}
		if (t.a[blen] == 0) blen--;
		t.len = blen + 1;
		return t;
	}
	// a must bigger to b...
	BigNum BigNum::operator-(const BigNum & n) const
	{
		int   i, j, big;
		BigNum t, a(*this);
		
		big = n.len > a.len ? n.len : a.len;
		for(i = 0 ; i < big; i++){
			if(a.a[i] < n.a[i]){
				j = i + 1;
				while(a.a[j] == 0) j++;
				a.a[j--]--;
				while(j > i) a.a[j--] += MAXN;
				t.a[i] = a.a[i] + MAXN + 1 - n.a[i];
			} else t.a[i] = a.a[i] - n.a[i];
		}
		a.len = big;
		while(t.a[a.len - 1] == 0 && a.len > 1) a.len--;
		t.len = a.len;
		return t;
	}
	BigNum BigNum::operator*(const BigNum &n) const
	{
		BigNum t;
		int   i, j;//blen;
		
		for (i = 0; i < len; i++) {
			for (j = 0; j < n.len; j++) {
				t.a[i + j] += a[i] * n.a[j];
				if (t.a[i + j] > MAXN) {
					t.a[i + j + 1] += t.a[i + j] / (MAXN + 1);
					t.a[i + j] %= (MAXN + 1);
				}
			}
		}
		t.len = len + n.len;
		while (t.a[t.len - 1] == 0 && t.len > 1) t.len--;
		return t;
	}
	BigNum BigNum::operator/(const int n) const
	{
		BigNum t;
		int   i, down;
		
		down = 0;
		for (i = len - 1; i >= 0; i--) {
			t.a[i] = (down * (MAXN + 1) + a[i]) / n;
			down = a[i] + down*(MAXN + 1) - t.a[i]*n;
		}
		t.len = len;
		while (t.a[t.len - 1] == 0 && t.len > 1) t.len--;
		return t;
	}
	ostream & operator<<(ostream &os, const BigNum &n)
	{
		int i;
		
		os << n.a[n.len - 1];
		for(i = n.len - 2 ; i >= 0 ; i--){
			os.width(DLEN);
			os.fill('0');
			os << n.a[i];
		}
		return os;
	}
	istream & operator>>(istream &is, BigNum &n)
	{
		char   s[DIGIT * 4 + 1];
		
		is >> s;
		BigNum t(s);
		n = t;
		return is;
	}
}
using namespace Me;
int hash[128];
char key[100];
int res[100];


int main()
{
	freopen("Al.in","r",stdin);
	freopen("Al.txt","w",stdout);

	int T;
	scanf("%d",&T);

	int bb=1;
	gets(key);

	while (T--)
	{

		int i,b=0;

		memset(hash,-1,sizeof(hash));
		gets(key);
		printf("Case #%d: ",bb++);

		if (strlen(key)==1)
		{
			puts("1");
			continue;
		}

		hash[key[0]]=1;

		for (i=1;key[i]!='\0';++i)
		{
			if (hash[key[i]]==-1)
			{
				if (b==1)
				{
					++b;
					hash[key[i]]=b++;
				}
				else
				{
					hash[key[i]]=b++;
				}
			}
		}

		b=0;

		for (i=0;i<128;++i)
		{
			if (hash[i]!=-1)
			{
				++b;
			}
		}

		if (b==1)
		{
			++b;
		}
	
		for (i=0;key[i]!='\0';++i)
		{
			res[i]=hash[key[i]];
		}

		BigNum ans=0;

		for (i=0;key[i]!='\0';++i)
		{
			ans=ans*b;
			ans=ans+res[i];
		}

		
		cout<<ans<<endl;
	}
	return 0;
}