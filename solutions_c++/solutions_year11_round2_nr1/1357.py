#include <stdio.h> 
#include <stdlib.h> 
#include <ctype.h> 
#include <string.h> 
#include <math.h> 
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <string> 
#include <iostream> 
#include <sstream>  
#include <set>
#include <map>
using namespace std; 

#define fo(i,n) for(i=0;i<(n);++i) 
#define MP make_pair

typedef long long ll ;
typedef vector<long long> vi ; 
typedef vector<string> vs ; 
typedef vector<double> vd ; 

char x[111][111];
long double WP[111] , OWP[111] , OOWP[111] , RPI[111];
int total[111];

int main ()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t , n ;
	scanf ("%d",&t);
	for (int tc=1 ; tc<=t ; tc++)
	{
		printf ("Case #%d:\n",tc);
		scanf("%d",&n);
		for ( int i=0 ; i<n ; i++ )
			scanf("%s",x[i]);
		for ( int i=0 ; i<n ; i++ )
		{
			long double  tot=0,w=0;
			for ( int j=0 ; j<n ; j++ )
			{
				if ( x[i][j]!='.' )	tot ++ , total[i]++;
				if ( x[i][j]=='1' ) w ++ ;
			}
			WP[i] = w/tot ;
		}
		for ( int i=0 ; i<n ; i++ )
		{
			long double  s=0 , tot=0 ;
			for ( int j=0 ; j<n ; j++ )
			{
				if ( i == j )	continue ;
				if ( x[i][j]=='1' || x[i][j]=='0' ) 
				{
					tot++ ;
					double tt=0 , ww = 0 ;
					for ( int k=0 ; k<n ; k++ )
					{
						if ( k == i )	continue ;
						if ( x[j][k]!='.' )	tt ++ ;
						if ( x[j][k]=='1' ) ww ++ ;
					}
					s += ( ww / tt ) ;
				}
			}
			OWP [ i ] = s / tot ;
		}
		for ( int i=0 ; i<n ; i++ )
		{
			long double s=0 , tot=0 ;
			for ( int j=0 ; j<n ; j++ )
			{
				if ( x[i][j]!='.' )	{
					s += OWP[j] ;
					tot ++ ;
				}
			}
			OOWP [ i ] = s / tot ;
		}
		int sss;
		for ( int i=0 ; i<n ; i++ )
		{
			long double ans = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i] ;
			printf ("%0.6llf\n",ans);
		}
	}
	//while(1);
}