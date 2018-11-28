#include<stdio.h>
#include<memory.h>
using namespace std;
long long t,n,r,k,g[1000],sumi[1000],next[1000];
int main(){
	scanf("%lld",&t);
	for(int i=1;i<=t;++i){
		scanf("%lld%lld%lld",&r,&k,&n);
		long long idx=0,earn=0;
		for(int j=0;j<n;++j) scanf("%lld",&g[j]);
		memset(sumi,0,sizeof(sumi));
		for(int j=0;j<r;++j){
			long long sum=0;
			if(sumi[idx]==0){
				int first=idx;
				sum+=g[idx]; idx=(idx+1)%n;
				for(;sum+g[idx]<=k && idx!=first;idx=(idx+1)%n) sum+=g[idx];
				sumi[first]=sum;
				next[first]=idx;
			}
			else{
				sum=sumi[idx];
				idx=next[idx];
				//printf("*");
			}
			earn+=sum;
		}
		printf("Case #%d: %lld\n",i,earn);
	}
	return 0;
}
