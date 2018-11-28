#include <iostream>
#include <stdio.h>
using namespace std;

FILE* fp;
int n,m,x,y,z;
long long num[500005];
long long a[500005];
unsigned int d[500005];

void solve(int tc)
{
	int i,j;
	for( i=0; i<n; i++ ) {
		d[i]=1;
	}



	for( i=n-1; i>=0; i-- ) {
		for( j=i+1; j<n; j++ ) {
			if( num[j] > num[i] ) {
				d[i] = (d[i]+d[j])%1000000007;
			}
		}
	}

	long long ans=0;
	for( i=0; i<n; i++ ) {
		ans = (ans+d[i])%1000000007;
	}
	fprintf(fp, "Case #%d: %lld\n",tc+1,  ans);
}
int main()
{
	fp= fopen("out.txt", "wt" );
	freopen("c-small-attempt1.in", "rt", stdin );

	int t;
	cin>>t;
	long long i,j;
	for( i=0; i<t; i++ )
	{	
		cin>>n>>m>>x>>y>>z;

		for( j=0; j<m; j++ ) {
			cin>>a[j];
		}

		int cnt=0;
		for( j=0; j<=n-1; j++ ) 
		{
			num[j] = a[j%m];			
			a[j%m] = (x * a[j%m] + y*(j+1)) % z;
		}

		solve(i);
	}

	fclose(fp);
	return 0;
}