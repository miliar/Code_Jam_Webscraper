#include <stdio.h>
#include <algorithm>
using namespace std;

typedef long long ll;

#define EPS 1e-9

main(){
	int tests;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		ll x[100];
		ll v[100];
		ll n,k,b,tlim;
		scanf("%lld%lld%lld%lld",&n,&k,&b,&tlim);
		for(int i=0;i<n;i++)scanf("%lld",&x[i]);
		for(int i=0;i<n;i++)scanf("%lld",&v[i]);
		int INF=n+1;
		double arr[100];
		for(int i=0;i<n;i++)arr[i]=(double)(b-x[i])/v[i];
		int nuku[100];
		for(int i=0;i<n;i++){
			if(arr[i]>tlim){nuku[i]=INF;continue;}
			nuku[i]=0;
			for(int j=0;j<n;j++){
				if(i==j)continue;
				if(v[j]>=v[i])continue;
				if(x[j]<x[i])continue;
				if(arr[j]>tlim+EPS){
					double ct=(double)(x[j]-x[i])/(v[i]-v[j]);
					if(ct<arr[j]-EPS)nuku[i]++;
				}
			}
		}
		sort(nuku,nuku+n);
		printf("Case #%d: ",t);
		if(nuku[k-1]==INF)printf("IMPOSSIBLE\n");
		else{
			int ans=0;
			for(int i=0;i<k;i++)ans+=nuku[i];
			printf("%d\n",ans);
		}
	}
}