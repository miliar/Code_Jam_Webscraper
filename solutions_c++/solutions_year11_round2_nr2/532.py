#include <cstdio>
#include <cstring>
#include <string>
#include <math.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>

using namespace std;

const int N=1000010;

int n,m,a[N],d,tt;
double x,y,ans;

bool test( double ans )
{
	double p=a[1]-ans;
	for ( int i=2;i<=m;i++ )
	{
//		if (  )
		if ( p+d>=a[i]-ans && p+d<=a[i]+ans )
			p=p+d;
		else if ( p+d<a[i]-ans ) p=a[i]-ans;
		else return 0;
	}

	return 1;
}

int main()
{
	freopen( "b.in","r",stdin );
	freopen( "b.out","w",stdout );

	scanf( "%d",&tt );
	for ( int ca=1;ca<=tt;ca++ )
	{
		scanf( "%d%d",&n,&d );
		m=0;
		for ( int i=1;i<=n;i++ )
		{
			int x,y;
			scanf( "%d%d",&x,&y );
			for ( int j=1;j<=y;j++ )
				a[++m]=x;
		}
		sort( a+1,a+1+m );

		x=0; y=d*m; ans=y;
		while ( y-x>1e-10 )
			if ( test((x+y)/2) ) 
			{
				if ( ans>(x+y)/2 ) ans=(x+y)/2;
				y=(x+y)/2;				
			}
			else x=(x+y)/2;

		printf("Case #%d: %.10lf\n",ca,ans );

	}

	return 0;

}


