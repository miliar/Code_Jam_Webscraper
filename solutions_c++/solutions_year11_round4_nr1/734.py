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

struct edge
{
	int x,y,z;
}a[N];

int n,m,s,r,ca,tt,len;
double t,ans,cur;

bool cmp( edge i,edge j )
{
	return i.z<j.z;
}

void run( double tar,int w )
{
	if ( (tar)/double(r+w)<=t )
	{
		t-=(tar)/double(r+w);
		ans+=(tar)/double(r+w);
	}
	else 
	{
		tar-=t*(r+w);
		ans+=t;
		t=0;
		ans+=(tar)/double(w);
	}
//	printf( "%lf %lf\n",t,ans );
}

int main()
{
	freopen( "a.in","r",stdin );
	freopen( "a.out","w",stdout );
	scanf( "%d",&tt );
	ca=0;
	while ( tt-- ) 
	{
		scanf( "%d%d%d%lf%d",&len,&s,&r,&t,&n );
		for ( int i=1;i<=n;i++ )
		{
			scanf( "%d%d%d",&a[i].x,&a[i].y,&a[i].z );
			a[i].z+=s;
		}
		a[0].y=0;
		for ( int i=n+1;i<=2*n+1;i++ )
		{
			a[i].x=a[i-n-1].y;
			a[i].y=a[i-n].x;
			a[i].z=s;
		}
		a[2*n+1].y=len;

		sort( a+1,a+2+2*n,cmp );
		r-=s;
//		for ( int i=1;i<=2*n+1;i++ )	printf( "%d %d %d\n",a[i].x,a[i].y,a[i].z );

		cur=ans=0;
		for ( int i=1;i<=2*n+1;i++ )
		{
			run(a[i].y-a[i].x,a[i].z);
		}
		printf( "Case #%d: %.15lf\n",++ca,ans );
//		break;
	
	}

	return 0;

}







