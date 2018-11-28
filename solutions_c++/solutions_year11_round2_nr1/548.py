#include <cstdio>
#include <cstring>
#include <string>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>

using namespace std;

const int N=110;

int n,m,tt;
char a[N][N];
double x[N],y[N],z[N];
int s1[N],s2[N];

double cal( int x,int y )
{
//	printf( "%d %d\n",x,y );
	if ( x==0 || y>x || y<0 ) return 0;
	else return y/(double)x;
}

int main()
{
	freopen( "a.in","r",stdin );
	freopen( "a.out","w",stdout );

	scanf( "%d",&tt );
	for ( int ca=1;ca<=tt;ca++ )
	{
		scanf( "%d",&n );
		for ( int i=0;i<n;i++ )
		{
			scanf( "%s",a[i] );
			s1[i]=s2[i]=0;
			for ( int j=0;j<n;j++ )
				if ( a[i][j]!='.' )
				{
//					printf( "%d %d\n",i,j );
					s1[i]++;
					s2[i]+=(a[i][j]=='1');
				}
				x[i]=cal( s1[i],s2[i] );

		}

		for ( int i=0;i<n;i++ )
		{
			y[i]=0;
			for ( int j=0;j<n;j++ )
				if ( a[i][j]!='.' )
				y[i]+=cal( s1[j]-1,s2[j]-(a[i][j]=='0') );
			
//			printf( "%lf\n",y[i] );
			if ( s1[i]==0 ) y[i]=0;
			else y[i]=y[i]/s1[i];
		}

		for ( int i=0;i<n;i++ )
		{
			z[i]=0;
			for ( int j=0;j<n;j++ )
				if ( a[i][j]!='.' )
					z[i]+=y[j];
			if ( s1[i]==0 ) z[i]=0;
			else z[i]=z[i]/s1[i];
		}

		printf( "Case #%d:\n",ca );
		for ( int i=0;i<n;i++ )
			printf( "%.10lf\n",0.25*x[i]+0.5*y[i]+0.25*z[i] );

//		for ( int i=0;i<n;i++ )			printf( "%d %d %lf %lf %lf\n",s1[i],s2[i],x[i],y[i],z[i] );

	}

	return 0;


}




