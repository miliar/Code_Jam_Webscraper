#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

#include <algorithm>
#include <set>
#include <map>
#include <queue>

using namespace std;

#include <iostream>
#define DB(x) cout << #x " == " << (x) << endl

struct bigint
{
	char num[100];
	int n;
	
	bigint() {}
	//bigint(char *x, int n): n(n) { strcpy(num,x); }
	
	void cap()
	{
		scanf("%s", num);
		n = strlen(num);
	}
	void print()
	{
		printf("%s", num);
	}
	
	bool maiori(const bigint & b, int i) const
	{
		if( i > 0 && num[i-1] != '0' ) return true;
		
		for( int j = 0 ; j < b.n ; ++j )
		{
			if( b.num[j] < num[i+j] ) return true;
			if( b.num[j] > num[i+j] ) return false;
		}
		return true;
	}
	
	void verif(int i)
	{
		while( num[i] < '0' ) num[i--] += 10, num[i]--;
	}
	
	void tirar(const bigint & b, int i)
	{
		for( int j = 1 ; j <= b.n ; ++j )
		{
			num[b.n-j+i] -= b.num[b.n-j]-'0';
			verif(b.n-j+i); 
		}
	}
	
	bigint operator%(const bigint & b) const
	{
		bigint ret = *this;
		for( int i = 0 ; i <= n-b.n ; ++i )
		{
			while( ret.maiori(b,i) )
			{
				ret.tirar(b,i);
			}
		}
		int i = 0;
		while( i < n && ret.num[i] == '0' ) ++i;
		if( i != 0 )
		{
			ret.n -= i;
			for( int j = 0 ; i <= n ; ++i, ++j )
			{
				ret.num[j] = ret.num[i];
			}
			//ret.num[i] = '\0';
		}
		return ret;
	}
	
	bool operator<(const bigint & b) const
	{
		if( n < b.n ) return true;
		if( n > b.n ) return false;
		
		for( int i = 0 ; i < n ; ++i )
		{
			if( num[i] < b.num[i] ) return true;
			if( num[i] > b.num[i] ) return false;
		}
		return false;
	}
	
	bigint operator-(const bigint & b) const
	{
		if( *this < b ) return b - *this;
		else
		{
			bigint ret = *this;
			for( int i = 1 ; i <= b.n ; ++i )
			{
				ret.num[n-i] -= b.num[b.n-i] -'0';
				ret.verif(n-i); 
			}
			int i = 0;
			while( i < n && ret.num[i] == '0' ) ++i;
			if( i != 0 )
			{
				ret.n -= i;
				for( int j = 0 ; i < n ; ++i, ++j )
				{
					ret.num[j] = ret.num[i];
				}
				ret.num[ret.n] = '\0';
			}
			return ret;
		}
	}
	bool zero()
	{
		return n == 0;
	}
};

bigint mdc(bigint a, bigint b)
{
	if( a.zero() ) return b;
	if( b.zero() ) return a;
	if( a < b ) return mdc(b%a, a);
	if( b < a ) return mdc(a%b, b);
	return a;
}

int n;
bigint t[1050], dif[1050], men;

void process()
{
	bigint res;
	bigint db;
	db = t[0]%men;
	if( db.zero() ) printf("0");
	else
	{
		res = men - t[0]%men;
		res.print();
	}
	printf("\n");
}

bool read()
{
	scanf("%d", &n);
	
	t[0].cap();
	for( int i = 1 ; i < n ; ++i )
	{
		t[i].cap();
		dif[i-1] = t[i]-t[i-1];
	}
	men = dif[0];
	
	for( int i = 1 ; i < n-1 ; ++i )
	{
		men = mdc(men, dif[i]);
	}
	return true;
}

int main()
{
	int c; scanf("%d", &c);
	int t = 1;
	while( c-- )
	{
		printf("Case #%d: ", t++);
		read();
		process();
	}	
	return 0;
}
