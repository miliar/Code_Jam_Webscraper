//#include "stdio.h"
//#include "iostream.h"

#include <cstdio>
#include <iostream>
using namespace std;


long N;

long P;
long K;
long W;
long f[1000];

int main() {
	
	long long i,j,k,l,Case=0;
	long long x,y;
	long long pn;
	long long pn2;
	long long ans;
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%ld",&N);
//	cout<<N<<endl;
//	cin<<N;
//	printf("%lld\n",N);
	for (Case=1;Case<=N;Case++)
	{
		scanf("%d %d %d",&P,&K,&W);
//		cin<<n<<A<<B<<C<<D<<x0<<yy<<M;

		for (i=0;i<W;i++)
		{
			scanf("%d",&f[i]);
		}
		for (i=0;i<W;i++)
		{
			for (j=i+1;j<W;j++)
			{
				if (f[i]<f[j])
				{
					l=f[i];f[i]=f[j];f[j]=l;
				}
			}
		}
		ans=0;
		l=0;
		for (i=0;i<P && l<W;i++)
		{
			for (j=0;j<K && l<W;j++)
			{
				ans+=((long long)(i+1))*((long long) f[l]);
				l++;
			}
		}
//		printf("Case #%d: ", Case);
//		printf("%lld\n",ans);
		cout<<"Case #"<<Case<<": "<<ans<<endl;
	}
   return 0;
}

