#include <cstdio>
#include <algorithm>
using namespace std;
int C,T,N,M;
int escolhidos[10];
int grafo[100][100];
int pessoas[100];
int ans2[10];

int ans=10000;
void escolhe(int p) {
	if(p==N) {
		int tmp=0;
		for(int i=0;i<M;i++) {
			int j=0;
			int aux=1;
			bool foi=false;
			for(j=0;j<N;j++) {
				if(grafo[i][j+N*escolhidos[j]]==1) {
					if(escolhidos[j]==0)
						aux=0;
					foi=true;
				}
			}
			if(!foi)
				return;
			tmp+=aux;
		}
		if(tmp<ans) {
			ans=tmp;
			for(int i=0;i<N;i++)
				ans2[i]=escolhidos[i];
		}
		return;
	}
	escolhidos[p]=0;
	escolhe(p+1);
	escolhidos[p]=1;
	escolhe(p+1);
}

int main(void) {
	scanf("%d",&C);
	for(int T=1;T<=C;T++) {
		ans=10000;
		printf("Case #%d:",T);
		memset(grafo,0,sizeof(grafo));
		scanf("%d %d",&N,&M);
		for(int i=0;i<M;i++) {
			int t;
			scanf("%d",&t);
			for(int j=0;j<t;j++) {
				int x,y;
				scanf("%d %d",&x,&y);
				x--;
				grafo[i][x+N*y]=1;
			}
		}
		escolhe(0);
		if(ans==10000) {
			printf(" IMPOSSIBLE");
		} else {
			for(int i=0;i<N;i++)
				printf(" %d",ans2[i]);
		}
		printf("\n");
	}
	return 0;
}
