#include<iostream>
#include<algorithm>
#define MX 10312
#define INF 10000000
using namespace std;
int g[MX],c[MX],val[MX],b[MX][2],m;
void dfs(int p){
	//printf("DFS %d\n",p,(m-1)/2);
	if(p<=(m-1)/2){
		dfs(p*2);
		dfs(p*2+1);
		if(c[p]==0){
			if(g[p]==1){
				b[p][0]=min(min(b[p*2][0]+b[p*2+1][0],b[p*2][0]+b[p*2+1][1]),b[p*2][1]+b[p*2+1][0]);
				b[p][1]=b[p*2][1]+b[p*2+1][1];
			}else{
				b[p][1]=min(min(b[p*2][1]+b[p*2+1][1],b[p*2][0]+b[p*2+1][1]),b[p*2][1]+b[p*2+1][0]);
				b[p][0]=b[p*2][0]+b[p*2+1][0];
			}
		}else{
			if(g[p]==1){
				b[p][0]=min(min(b[p*2][0]+b[p*2+1][0],b[p*2][0]+b[p*2+1][1]),b[p*2][1]+b[p*2+1][0]);
				b[p][1]=min(min(b[p*2][1]+b[p*2+1][1],b[p*2][1]+b[p*2+1][0]+1),b[p*2][0]+b[p*2+1][1]+1);
			}else{
				b[p][1]=min(min(b[p*2][1]+b[p*2+1][1],b[p*2][0]+b[p*2+1][1]),b[p*2][1]+b[p*2+1][0]);
				b[p][0]=min(min(b[p*2][0]+b[p*2+1][0],b[p*2][1]+b[p*2+1][0]+1),b[p*2][0]+b[p*2+1][1]+1);
			}
		}
	}else{
		b[p][val[p]]=0;
		b[p][1-val[p]]=INF;
	}
	//printf("%d %d\n",b[p][0],b[p][1]);
}
main(){
	int t,tt,v,i;
	scanf("%d",&t);
	for(tt=1;tt<=t;tt++){
		scanf("%d",&m);
		scanf("%d",&v);
		for(i=1;i<=(m-1)/2;i++){
			scanf("%d",&g[i]);
			scanf("%d",&c[i]);
		}
		for(i=((m-1)/2)+1;i<=m;i++){
			scanf("%d",&val[i]);
		}
		//printf("OK\n");fflush(stdout);
		dfs(1);
		//printf("OK\n");fflush(stdout);
		printf("Case #%d: ",tt);
		if(b[1][v]>=INF){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",b[1][v]);
		}
	}
}
