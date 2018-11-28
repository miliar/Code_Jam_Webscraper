//DS includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include<bitset>
#include<complex>

//Other Includes
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>

#define oo 					(int)13e7
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define ull 					unsigned long long
#define ll 						long long
#define bitcount 			__builtin_popcount
#define all(x) 				x.begin(), x.end()
#define pb( z ) 				push_back( z )
#define gcd					__gcd
using namespace std;

const int mxn = 550;
int a[mxn][mxn];
int dp[mxn][mxn];
char b[mxn];
int m, n;

inline void recalcDpRow( int r )
{
	int *d = dp[r];
	d[n-1] = a[r][n-1] != 2;
	for(int j=n-2; j >= 0; j--)
	{
		d[j] = a[r][j] != 2;
		if( a[r][j+1] == (a[r][j]^1) )
			d[j] += d[j+1];
	}
}
inline void printit()
{
	for(int x=0; x < m; x++)
	{
		for(int y=0; y<n;y++)
		cout<<a[x][y];
		cout<<endl;
	}
	 cout<<endl;
}
pair<int,int> solve( int L )
{
	
	
	int sx=-1, sy=-1;
	for(int x=0; x+L <= m; x++)
	for(int y=0; y+L <= n; y++)
	{
		bool ok = 1;
		
		for(int k=0; k < L; k++)
		{
			if( dp[x+k][y] < L )
			{
				ok = 0;
				break;
			}
			if( k )
			if( a[x+k-1][y] != (1^a[x+k][y]) )
			{
				ok = 0;
				break;
			}
		}
		if( ok )
		{
			sx=x; sy=y;
			x=y=1024; break;
		}
	}
	if( sx >= 0 && sy >= 0 )
	for(int x=sx; x < sx+L; x++)
	{
		for(int y=sy; y < sy+L; y++)
		{
			if( x > sx ) assert( a[x][y] != a[x-1][y] );
			if( y > sy ) assert( a[x][y] != a[x][y-1] );
			a[x][y] = 2;
		}
		recalcDpRow( x );
	}
	return make_pair( sx, sy );
}

int main()
{
	//freopen("C-small-attempt0.in", "r", stdin ); freopen("C-small-attempt0.out", "w", stdout );
	freopen("C-small-attempt1.in", "r", stdin ); freopen("C-small-attempt1.out", "w", stdout );
	//freopen("C-small-attempt2.in", "r", stdin ); freopen("C-small-attempt2.out", "w", stdout );
	
	//freopen("C-large.in", "r", stdin ); freopen("C-large.out", "w", stdout );
	
	int T;
	cin>>T;
	for(int t=1; t <= T; t++)
	{
		cin>>m>>n;
		
		for(int i=0; i < m; i++)
		{
			cin>>b;
			for(int j=0, p=0; j < (n/4); j++)
			{
				char c = b[j];
				if( isalpha( c ) )
					c = 10 + c-'A';
				else
					c -= '0';
				for(int k=0; k < 4; k++)
					a[i][p++] = ( c&1<<(3-k) ) ? 1 : 0;
			}
			
			recalcDpRow( i );
		}
		#define debug if( 0 )
		debug printit();
		
		vector<int> l, c; 
		for(int L=min(m,n); L >= 2; L--)
		{
			
			int cur = 0;
			while( true )
			{
				pair<int,int> g = solve( L );
				if( g.first == -1 ) break;
				cur++;
				debug { cout<< g.first <<  "," << g.second << endl; printit(); }
			}
			if( cur )
			{
				l.pb( L ); c.pb( cur ); 
			}
		}
		int s = 0;
		for(int x=0; x < m; x++)
		for(int y=0; y < n; y++)
		if( a[x][y] != 2 )
		s++;
		if( s )
		{
			l.pb( 1 ); c.pb( s );
		}
		printf("Case #%d: %d\n", t, (int)l.size() );
		for(int i=0; i < (int)l.size(); i++)
		printf("%d %d\n", l[i], c[i] );
	}
	
	return 0;
}
