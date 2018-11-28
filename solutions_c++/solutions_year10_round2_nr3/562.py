#include<iostream>
#include<map>
#include<queue>
#include<vector>
#include<set>
#include<sstream>
#include<cmath>
#include<algorithm>
#define oo (int)1e9
#define s(n)scanf("%d",&n)
using namespace std;
#include<string.h>
#include<cstdio>
#define gcd __gcd
#define lcm(a,b) (a/gcd(a,b))*b
#define mod 100003

int n,k;
int cs;
int soln[128];

int main()
{
	
//	freopen("C.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);	
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);	
	
	
	/*
	for( int N = 2 ; N <= 20 ; N++ )
	{
		int n = N - 1 ;
		int cnt = 0;
		map< vector<int> , bool >M;
		for(int mask=1;mask<(1<<n);mask++)
		{
			vector<int>v;
			for(int i=0;i<n-1;i++)
			 if( mask & 1<<i )
			  v.push_back( i+2 );
			  v.push_back( n+1 );
			  
			 bool ok = 1;
			 

			 if( M [v] )continue;
			 M[v] = 1;
			 int no = n;

			 
			 while( no > 1 )
			 {
			 	if( !binary_search( v.begin() , v.end() , no )  )
			 	{
			 		ok = 0;
			 		break;
			 	}
			 	
			 	
			 	int pos = -1;
			 	for(int i=0;i<v.size();i++)if( no == v[i] ){ pos = i ; break; }
			 	no = pos+1;
			 }
			 
			 cnt += no == 1;
			 
		}
		//printf( "%d %d  :DDDDDD" , N , cnt );
		//cout << endl; 
		printf( "%d,",cnt );
		
	}
	puts( "" );
	
	*/


soln[0] = 0;
soln[1] = 1;
soln[2] = 1;
soln[3] = 2;
soln[4] = 3;
soln[5] = 5;
soln[6] = 8;
soln[7] = 14;
soln[8] = 24;
soln[9] = 43;
soln[10] = 77;
soln[11] = 140;
soln[12] = 256;
soln[13] = 472;
soln[14] = 874;
soln[15] = 1628;
soln[16] = 3045;
soln[17] = 5719;
soln[18] = 10780;
soln[19] = 20388;
soln[20] = 38674;
soln[21] = 73562;
soln[22] = 40265;
soln[23] = 68060;
soln[24] = 13335;
soln[25] = 84884;
soln[25] = 84884;


	
	int runs;

	s( runs );
	while( runs-- )
	{
		s( n );
		printf( "Case #%d: %d\n" , ++cs , soln[n] );

	}
	
}

