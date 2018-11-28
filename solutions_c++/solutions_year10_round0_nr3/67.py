#include<stdio.h>
#include<string.h>
typedef long long LL;
int g[1000],m[1000],next[1000],idx[1000],gain[1000];
int main(){
	int times;
	scanf("%d",&times);
	for(int tm=1;tm<=times;tm++){
		printf("Case #%d: ",tm);
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;i++)scanf("%d",&g[i]);
		LL sum=0;
		for(int i=0;i<n;i++)sum+=g[i];
		LL res;
		if(sum<=k){
			res=sum*r;
			printf("%lld\n",res);
			continue;
		}
		for(int i=0;i<n;i++){
			int t=0,j;
			for(j=i;;j=(j+1)%n){
				if(t+g[j]>k)break;
				t+=g[j];
			}
			m[i]=t;
			next[i]=j;
		}
		int cur=0;
		res=0;
		for(int i=0;i<r;i++){
			res+=m[cur];
			cur=next[cur];
		}
		printf("%lld\n",res);
	}
	return 0;
}


