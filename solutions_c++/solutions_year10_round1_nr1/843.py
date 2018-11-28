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
int main()
{
	int cs = 1;
	freopen("A-large.in","r",stdin);
   freopen("A-large.ans","w",stdout);

	int tc, i, j;
	cin >> tc;
	while( tc -- )
	{
		int n, k;
		string s[ 100 ], p[ 100 ];
		cin >> n >> k;
		for(i = 0; i < n ; i ++ ) {
			cin >> s[ i ];
			reverse( s[ i ].begin(), s[ i ].end() );

			for(j = 0; j < s[ i ].size(); j ++ )
				if( s[ i ][ j ] == 'R' || s[ i ][ j ] == 'B' )
					p[ i ] += s[ i ][ j ];
			for(j = p[ i ].size();j< 60; j ++ ) p[ i ] += '.';
		}
		for(;i<60; i ++ )
			for(j = 0 ;j< 60; j ++ ) p[ i ] += '.';
		bool r = 0, b = 0;

		for(i = 0; i < 60 ; i ++ )
		{
			int cn = 0;
			for(j = 0; j < 60 ; j ++ )
			{
				if( p[ i ][ j ] != 'R' ) cn = 0;
				else cn ++;
				if( cn == k ){
					r = true;
					break;
				}
			}
			cn = 0;
			for(j = 0; j < 60 ; j ++ )
			{
				if( p[ i ][ j ] != 'B' ) cn = 0;
				else cn ++;
				if( cn == k ){
					b = true;
					break;
				}
			}
		}
		for(i = 0; i < 60; i ++ )
		{
			int cn = 0;
			
			for(j = 0; j < 60 ; j ++ )
			{
				if( p[ j ][ i ] != 'R' ) cn = 0;
				else cn ++;
				if( cn == k ){
					r = true;
					break;
				}
			}
			cn = 0;
			for(j = 0; j < 60 ; j ++ )
			{
				if( p[ j ][ i ] != 'B' ) cn = 0;
				else cn ++;
				if( cn == k ){
					b = true;
					break;
				}
			}
		}
		int sti, stj ;
		for(sti = 0, stj = 0;sti < 60;sti ++)
		{
			int cn = 0;
			for(i = sti, j = stj; i < 60 && j < 60 ; i ++ , j ++ )
			{
					
				if( p[ i ][ j ] != 'R' ) cn = 0;
				else cn ++;
				if( cn == k ){
					r = true;
					break;
				}
			}
			cn = 0;
			for(i = sti, j = stj; i < 60 && j < 60 ; i ++ , j ++ )
			{
				if( p[ i ][ j ] != 'B' ) cn = 0;
				else cn ++;
				if( cn == k ){
					b = true;
					break;
				}
			}			
		}
		for(sti = 0, stj = 0;stj < 60;stj ++)
		{
			int cn = 0;
			for(i = sti, j = stj; i < 60 && j < 60 ; i ++ , j ++ )
			{
					
				if( p[ i ][ j ] != 'R' ) cn = 0;
				else cn ++;
				if( cn == k ){
					r = true;
					break;
				}
			}
			cn = 0;
			for(i = sti, j = stj; i < 60 && j < 60 ; i ++ , j ++ )
			{
				if( p[ i ][ j ] != 'B' ) cn = 0;
				else cn ++;
				if( cn == k ){
					b = true;
					break;
				}
			}			
		}
		for(sti = 0, stj = 0;sti < 60;sti ++)
		{
			int cn = 0;
			for(i = sti, j = stj; i >= 0 && j >= 0 ; i -- , j ++ )
			{
					
				if(p[ i ][ j ] != 'R' ) cn = 0;
				else cn ++;
				if( cn == k ){
					r = true;
					break;
				}
			}
			cn = 0;
			for(i = sti, j = stj; i >= 0 && j >= 0 ; i -- , j ++ )
			{
				if( p[ i ][ j ] != 'B' ) cn = 0;
				else cn ++;
				if( cn == k ){
					b = true;
					break;
				}
			}			
		}
		for(sti = 59, stj = 0;stj < 60;stj ++)
		{
			int cn = 0;
			for(i = sti, j = stj; i >= 0 && j >= 0 ; i -- , j ++ )
			{
					
				if( p[ i ][ j ] != 'R' ) cn = 0;
				else cn ++;
				if( cn == k ){
					r = true;
					break;
				}
			}
			cn = 0;
			for(i = sti, j = stj; i >= 0 && j >= 0 ; i -- , j ++ )
			{
				if( p[ i ][ j ] != 'B' ) cn = 0;
				else cn ++;
				if( cn == k ){
					b = true;
					break;
				}
			}		
		}

		cout << "Case #"<<cs ++ <<": ";
		if( r && b ) cout <<"Both"<<endl;
		else if( r  ) cout <<"Red"<<endl;
		else if( b ) cout <<"Blue"<<endl;
		else  cout <<"Neither"<<endl;

		
	}
	return 0;
}