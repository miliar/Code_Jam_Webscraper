#include<stdio.h>
#include<string.h>
#include<algorithm>
int n;
int dist[10010],len[10010],a[10010];
int main(){
	int _;
	scanf("%d",&_);
	for(int t=1; t<=_; t++){
		scanf("%d",&n);
		for(int i=0; i<n; i++)
			scanf("%d%d",&dist[i],&len[i]);
		scanf("%d",&dist[n]);
		len[n]=0;
		memset(a,-1,sizeof(a));
		a[0]=dist[0];
		for(int i=0; i<n; i++)
			if(a[i]!=-1)
			for(int j=i+1; j<=n; j++){
				if(dist[i]+a[i]<dist[j])break;
				a[j]=std::max(a[j],std::min(len[j],dist[j]-dist[i]));
			}
		printf("Case #%d: %s\n",t,a[n]!=-1?"YES":"NO");
	}
	return 0;
}
