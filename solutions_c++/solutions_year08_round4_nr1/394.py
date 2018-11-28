#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstdlib>
#include<vector>
#include<queue>

using namespace std;

typedef long long LL;

#define FT first
#define SD second
#define MP make_pair
#define PB push_back

#define INF 100000

int T,tmp;
int m,c,g,k,ca,v;
int tab[10005][2];
int w[10005][2];

int main(){
	scanf("%d",&T);
	ca=0;
	while(T--){
		ca++;
		scanf("%d %d",&m,&v);
		for(int i=1;i<=(m-1)/2;i++){
			scanf("%d %d",&g,&c);
			tab[i][0]=g;
			tab[i][1]=c;
		}
		for(int i=(m-1)/2+1;i<=m;i++){
			scanf("%d",&k);
			tab[i][0]=k;
			w[i][k]=0;
			w[i][k^1]=INF;
		}
		for(int i=(m-1)/2;i>0;i--){
			if(tab[i][0]){
				//and
				w[i][0]=INF;
				w[i][1]=INF;
				w[i][0]=min(w[i*2][0],w[i*2+1][0]);
				w[i][1]=min(INF,w[i*2][1]+w[i*2+1][1]);
			}else{
				//or
				w[i][0]=INF;
				w[i][1]=INF;
				w[i][0]=min(INF,w[i*2][0]+w[i*2+1][0]);
				w[i][1]=min(w[i*2][1],w[i*2+1][1]);
			}
			if(tab[i][1]){
				if(!tab[i][0]){
					//and
					tmp=min(w[i*2][0],w[i*2+1][0]);
					w[i][0]=min(tmp+1,w[i][0]);
					tmp=min(INF,w[i*2][1]+w[i*2+1][1]);
					w[i][1]=min(w[i][1],tmp+1);
				}else{
					//or
					tmp=min(INF,w[i*2][0]+w[i*2+1][0]);
					w[i][0]=min(w[i][0],tmp+1);
					tmp=min(w[i*2][1],w[i*2+1][1]);
					w[i][1]=min(w[i][1],tmp+1);
				}
			}
		}
		printf("Case #%d: ",ca);
		if(w[1][v]==INF){
			printf("IMPOSSIBLE\n");
		}else{
			printf("%d\n",w[1][v]);
		}
	}
	return 0;
}

