#include <stdio.h>

long long g[3000],money[3000],profit[3000],times[3000],step[3000],moneyearnedinstep[3000];
int visited[3000],next[3000],stepneededtoreach[3000];

int main(){
	int t,n,u,i,j;
	long long R,k,sum;
	scanf("%d",&t);
	for (u=1; u<=t ;u++){
		scanf("%lld%lld%d",&R,&k,&n);
		for (i=0; i<n; i++) scanf("%lld",&g[i]);
		for (i=0; i<n; i++) g[i+n]=g[i];
		sum=0;
		for (i=j=0; i<n; i++){
			while(j<i+n && sum+g[j]<=k)
				sum+=g[j++];
			next[i]=j%n;
			//printf("%d->%d\n",i,next[i]);
			profit[i]=sum;
			sum-=g[i];
		}
		visited[0]=u;
		i=0;
		money[i]=0;
		stepneededtoreach[0]=0;
		moneyearnedinstep[0]=0;
		int st=0;
		while(1){
			st++;
			j=i;
			i=next[i];
			if (visited[i]==u) break;
			money[i]=money[j]+profit[j];
			stepneededtoreach[i]=1+stepneededtoreach[j];
			moneyearnedinstep[st]=money[i];
			visited[i]=u;
		}
		int entrylen=stepneededtoreach[i];
		int cyclelen=st-entrylen;
		long long cyclemoney=money[j]+profit[j]-money[i];
		int times=(R-entrylen)/cyclelen;
		long long tot=moneyearnedinstep[R-times*cyclelen]+times*cyclemoney;
		printf("Case #%d: %lld\n",u,tot);
	}
	return 0;	
}		
		
