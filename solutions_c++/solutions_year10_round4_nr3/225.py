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

char a[128][128];
char b[128][128];
int main()
{
	//freopen("C-small-attempt0.in", "r", stdin ); freopen("C-small-attempt0.out", "w", stdout );
	freopen("C-small-attempt1.in", "r", stdin ); freopen("C-small-attempt1.out", "w", stdout );
	//freopen("C-small-attempt2.in", "r", stdin ); freopen("C-small-attempt2.out", "w", stdout );
	
	//freopen("C-large.in", "r", stdin ); freopen("C-large.out", "w", stdout );
	
	int runs;
	s( runs );
	#define N 127
	for(int t=1; t <= runs; t++)
	{
		int n;
		fill( a, '.' );
		s(n);
		while( n-- )
		{
			int x1, y1, x2, y2;
			s(x1); s(y1); s(x2); s(y2);
			
			for(int x=x1; x <= x2; x++)
			for(int y=y1; y <= y2; y++)
			{
				a[x][y] = '1';
			}
		}
		
		int T = 0;
		do
		{
			bool flag = 0;
			if( 0 )
			{
				for(int x=1; x <= N; x++, cout<<endl)
				for(int y=1; y <= N; y++)
				cout<< a[x][y] ; cout<<endl;
			}
			
			for(int x=1; x <= N; x++)
			for(int y=1; y <= N; y++)
			{
				b[x][y] = a[x][y];
				if( a[x][y] == '1' )
				{
					flag = 1;
					if( a[x-1][y] != '1' && a[x][y-1] != '1' )
					{
						b[x][y] = '.';
					}
				}
				else
				{
					if( a[x-1][y] == '1' && a[x][y-1] == '1' )
					{
						b[x][y] = '1'; flag = 1;
					}
				}
			}
			for(int x=1; x <= N; x++)
			for(int y=1; y <= N; y++)
			a[x][y] = b[x][y];
			if( !flag ) break;
			T++;
		}
		while( true );
		
		printf( "Case #%d: %d\n", t, T );
	}
	
	
	return 0;
}
