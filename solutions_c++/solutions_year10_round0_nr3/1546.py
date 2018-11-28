#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int n,m,tt,r,k,ne[2010],ca;
long long sum[2010],ans,ans1;
bool v[1010];

int main()
{
	freopen( "3.in","r",stdin );
	freopen( "3.out","w",stdout );
	ca=0;
	scanf( "%d",&tt );
	while ( tt-- )
	{
		ca++;
		printf( "Case #%d: ",ca );
		scanf( "%d%d%d",&r,&k,&n );
		sum[0]=0;
		for ( int i=1;i<=n;i++ )
		{
			cin>>sum[i];
			sum[i]+=sum[i-1];		
		}
		for ( int i=n+1;i<=n+n;i++ )
			sum[i]=sum[i-n]+sum[n];

		int j=1;
		for ( int i=1;i<=n;i++ )
		{
			while ( j<n+i && sum[j]-sum[i-1]<=k ) j++;
			ne[i]=j-1;
		}
		

		ans=0;
		memset( v,1,sizeof(v) );

		int i,det=0;
		for ( i=1;v[i] && det<r;i=ne[i]%n+1 )
		{
			det++;
			v[i]=0;
			ans+=sum[ne[i]]-sum[i-1];
		}

		if ( det==r ) 
		{
			cout<<ans<<endl;
			continue;
		}

		r-=det; det=0; ans1=0;
		memset( v,1,sizeof(v) );
		for ( ;v[i] && det<r;i=ne[i]%n+1 )
		{
			det++;
			v[i]=0;
			ans1+=sum[ne[i]]-sum[i-1];
		}

		if ( det==r ) 
		{
			cout<<ans1+ans<<endl;
			continue;
		}

		ans+=ans1*(r/det);

		r%=det; det=0;
		memset( v,1,sizeof(v) );
		for ( ;v[i] && det<r;i=ne[i]%n+1 )
		{
			det++;
			v[i]=0;
			ans+=sum[ne[i]]-sum[i-1];
		}

		cout<<ans<<endl;
		
		
	}

	return 0;

}
