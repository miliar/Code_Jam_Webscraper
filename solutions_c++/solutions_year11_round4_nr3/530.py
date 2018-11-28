#include <cstdio>
#include <cstring>
#include <string>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>

using namespace std;

const int N=1010;

int n,m,p[N],a[N],a1,a2,tt,ca,c[N][N];

int main()
{
	freopen( "c.in","r",stdin );
	freopen( "c.out","w",stdout );
	scanf( "%d",&tt );
	ca=0;
	while ( tt-- )
	{
		a1=1;
		scanf( "%d",&n );
		m=0;
		bool ff;
		for ( int i=2;i<=n;i++ )
		{
			ff=0;
			int k=i,cc=0;
			for ( int j=1;j<=m;j++ )
			{
				cc=0;
				while ( k%a[j]==0 ) 
				{
					k/=a[j];
					cc++;
				}
				if ( cc>p[j] ) 
				{
					p[j]=cc;
					ff=1;
				}
			}
			if ( ff || k>1 ) a1++;
			if ( k==1 ) continue;
			a[++m]=k;
			p[m]=1;			
		}
//		for ( int i=1;i<=m;i++ )	printf( "%d %d\n",a[i],p[i] );	printf( "%d\n",a1 );
		
		memset( c,0,sizeof(c) );
		for ( int i=2;i<=n;i++ )
		{
			int k=i;
			for ( int j=1;j<=m;j++ )
				while ( k%a[j]==0 )
				{
					k/=a[j];
					c[i][j]++;
				}
		}
		a2=0;
		for ( int i=n;i>=2;i-- )
		{
			bool ff=0;
			for ( int j=1;j<=m;j++ )
				if ( c[i][j]==p[j] )
				{
					ff=1;
					p[j]=-1;
				}
			a2+=ff;
		}
		if ( a2==0 ) a2=1;

//		for ( int i=1;i<=m;i++ )	printf( "%d %d\n",a[i],p[i] );	printf( "%d\n",a2 );

		
		printf( "Case #%d: %d\n",++ca,a1-a2 );	
	}

	return 0;

}



