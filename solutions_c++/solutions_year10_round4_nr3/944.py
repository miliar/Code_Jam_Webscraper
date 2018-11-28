/*****************************

******************************/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
int max( int a, int b ){ return a > b ? a : b; }
int min( int a, int b ){ return a < b ? a : b; }
int a[ 500][ 500 ], b[ 500 ][ 500 ];
int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.ans","w",stdout);

	int tc, cs = 1;
	cin >> tc;
	while( tc -- )
	{
		int r, i, j, i1, mx = 0, my = 0;
		cin >> r;
		
		CLR( a );
		CLR( b );
			for(i1 = 0; i1 < r ; i1 ++ )
		{
			int x1,x2,y1,y2;
			cin >> y1 >> x1 >> y2 >> x2;
			for(i = x1; i <= x2; i ++ )
				for(j = y1; j <= y2; j ++ )
					a[ i  ][ j  ] = 1;
			mx = max( mx, y1 );
			mx = max( mx, y2 );

			my = max( my, x1 );
			my = max( my, x2 );
		}
		mx ++, my ++;
		int fl = 1, cnt = 0;;
		while( fl )
		{
			fl = 0;
			cnt ++ ;
			for(i = 1; i <= 110 ; i ++)
				for(j = 1 ; j <= 110; j ++ )
				{
					if( a[ i - 1 ][ j ] == 1 && a[ i ][ j - 1] == 1 ){
						b[ i ][ j ] = 1;
						fl = 1;
					}
					else if( a[ i - 1 ][ j ] == 0 && a[ i ][ j - 1] == 0 ) 
						b[ i ][ j ] = 0;		
					else b[ i ][ j ] = a[ i ][ j ];					
				}
			for(i = 0; i <= 110 ;i ++)
				for(j = 0; j <= 110 ; j ++ )
				{
					a[ i ][ j ] = b[ i ][ j ];
				    if( a[ i ][ j ] == 1 ) fl = 1;
				}			
		}
		
		cout << "Case #"<<cs ++<<": "<<cnt  << endl;
	}
	return 0;
}
