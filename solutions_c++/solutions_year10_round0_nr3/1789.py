#include<stdio.h>
#include<string.h>
long long gro[1005];
long long used[1005];
long long time[1005];
int main(){
	long long cases=0;
	long long T;
	long long R,K,N;
	long long i,j,k,l,cir,mod;
	long long sum1,sum2;
	long long tmp;
	long long ans;
//	freopen("G:\\C-large.in","r",stdin);
//	freopen("G:\\C-large.out","w",stdout);
	scanf("%lld",&T);
	while(T--){
		scanf("%lld %lld %lld",&R,&K,&N);
		for(i=0;i<N;i++){
			scanf("%lld",&gro[i]);
		}
		memset(used,-1,sizeof(used));
		k=0;
		sum1=0;
		for(i=cir=0;i<R;i++,cir++){
			if(used[k]!=-1) break;
			used[k]=sum1;
			time[k]=cir;
			tmp=0;
			l=k;
			for(j=k;j<N;j++){
				if(tmp+gro[j]>K) break;
				tmp+=gro[j];
				l=j;
			}
			if(j==N){
				for(j=0;j<k;j++){
					if(tmp+gro[j]>K) break;
					tmp+=gro[j];
					l=j;
				}
			}
			sum1+=tmp;
			k=l+1;
			if(k>=N) k=0;
		}
		if(used[k]!=-1){
			cir-=time[k];
			mod=(R-time[k])%cir;
			cir=(R-time[k])/cir;
			ans=used[k]+(sum1-used[k])*cir;
			sum2=0;
			for(i=0;i<mod;i++){
				tmp=0;
				l=k;
				for(j=k;j<N;j++){
					if(tmp+gro[j]>K) break;
					tmp+=gro[j];
					l=j;
				}
				if(j==N){
					for(j=0;j<k;j++){
						if(tmp+gro[j]>K) break;
						tmp+=gro[j];
						l=j;
					}
				}
				sum2+=tmp;
				k=l+1;
				if(k>=N) k=0;
			}
			ans+=sum2;
		}
		else ans=sum1;
		printf("Case #%lld: %lld\n",++cases,ans);
	}
	return 0;
}