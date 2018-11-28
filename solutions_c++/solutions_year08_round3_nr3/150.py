//#include "stdio.h"
//#include "iostream.h"

#include <cstdio>
#include <iostream>
using namespace std;


long N;
long long n,m,X,Y,Z;
long long a[500000];
long long b[500000];		//final output
long long c[500000];
long long ans;

int main() {
	
	long i,j,k,l,Case=0;
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	scanf("%ld",&N);
//	cout<<N<<endl;
//	cin<<N;
//	printf("%lld\n",N);
	for (Case=1;Case<=N;Case++)
	{
		scanf("%ld %ld %ld %ld %ld",&n,&m,&X,&Y,&Z);
//		cin<<n<<A<<B<<C<<D<<x0<<yy<<M;
//		cout<<n<<" " <<m<<" "<<X<<" "<<Y<<" "<<Z<<endl;

		for (i=0;i<m;i++)
		{
			scanf("%ld",&a[i]);
///			cout<<a[i]<<endl;
		}
//		cout<<endl;
		for (i=0;i<n;i++)
		{
			b[i]=a[i%m];
//			cout<<b[i]<<endl;
			a[i%m]=(X * a[i%m] + Y*(i+1) )%Z;
		}
		
		ans=0;
		for (i=0;i<n;i++)
		{
            c[i]=1;
			for (j=0;j<i;j++)
			{
				if (b[i]<=b[j]) continue;
				c[i]=(c[i]+c[j])% 1000000007;
			}
			ans=(ans+c[i])%1000000007;
		}

//		printf("Case #%d: ", Case);
//		printf("%lld\n",ans);
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	}
   return 0;
}

