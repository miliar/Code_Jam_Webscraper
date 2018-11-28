#include <cstdio>
#include <cstring>
#include <cassert>
#include <algorithm>

using namespace std;

const int maxn = 1005;
const int maxd = 100;
const int BASE = 10;

struct Bigint
{
	int num[maxd];
	Bigint ()
	{
		memset ( num,  0, sizeof num );
	}	
	bool operator<(const Bigint &A)const
	{
		for(int i = maxd-1; i >= 0; i--)
			if(num[i] < A.num[i])
				return true;
			else if( num[i] > A.num[i] )
				return false;
		return false;
	}
	bool operator==(const Bigint &A)const
	{
		for(int i=0;i<maxd;i++)
			if(num[i]!=A.num[i])
				return false;
		return true;
	}
	void operator=(char *p)
	{
		reverse (p , p + strlen(p) );
		for(int i = 0; p[i] ; i++)
			num[i] = p[i] - '0';
		for(int i = strlen(p) ; i < maxd; i++)
			num[i] = 0 ;
		return ;
	}
	Bigint operator-(Bigint B)
	{
		Bigint A = *this;
		int carry = 0 ;

		for(int i = 0; i < maxd ;i ++)
		{
			int temp = B.num[i] + carry;
			A.num[i] = A.num[i] - (B.num[i]+carry)%BASE;
			carry = temp / BASE ;
			if(A.num[i]<0)
			{
				A.num[i] += BASE;
				carry++;
			}
		}

		return A;
	}
	Bigint operator*(const int val)
	{
		Bigint ret = *this;
		int carry = 0;
		for (int i = 0; i < maxd; i++)
		{
			int rem = carry + val*ret.num[i];
			ret.num[ i ] = rem%BASE;
			carry = rem / BASE;
		}
		return ret ;
	}
	Bigint operator+(Bigint B)
	{
		Bigint A = *this;
		int carry = 0;

		for (int i = 0; i < maxd; i++)
		{
			int rem = carry + A.num[ i ] + B.num[ i ];
			A.num[ i ] = rem % BASE;
			carry = rem / BASE;
		}

		return A ;
	}
	Bigint operator%(Bigint B)
	{
		Bigint A, val;
		while( A + B < *this || A+B == *this )
		{
			val = B;
			while( A + val * 2 < *this || A + val * 2 == *this )
				val = val * 2;
			A = A + val;
		}
		A = (*this) - A;
		return A ;
	}
	void print ()
	{
		int start = maxd - 1;

		for ( ; start > 0 && num[start] == 0  ; start --);

		for ( ; start >= 0; start -- )
			putchar ( num[start] + '0' );

		putchar ('\n' );

		return ;
	}
};

char ti[maxd];
Bigint X[maxn];

Bigint gcd(Bigint A,Bigint B)
{
	if( A < B )
		swap (A,B);
	return B == Bigint() ? A : gcd ( B, A % B );
}

int main ()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("B.out", "w", stdout );
	int T ;

	scanf ("%d", &T);

	for (int cas = 1; cas <= T; cas++)
	{
		int n ;
		scanf ("%d", &n);

		for(int i = 0; i < n; i++)
		{
			scanf ("%s", ti);
			X[i] = ti;
		}

		sort( X, X + n);
		Bigint ans = X[1] - X[0];
		Bigint temp ;
		
		for(int i = 2 ; i < n; i ++)
			ans = gcd ( ans , X[i] - X[0] );

		temp = X[0] % ans;

		for(int i = 0 ; i < n; i ++)
			assert ( X[i] % ans == temp );

		if(temp == Bigint())
			ans = temp ;
		else
			ans = ans - temp ;

		printf ("Case #%d: ", cas);

		ans.print ();
	}

	return 0;
}
