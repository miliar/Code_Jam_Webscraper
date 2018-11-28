#include <stdio.h>
#include <string.h>
#include <map>
#include <queue>

#define INF 100000

using namespace std;

typedef pair<int,int> par;

#define NORTE 0
#define OESTE 1
#define LESTE 2
#define SUL   3
#define sink  4


static const int dx[]={-1, 0, 0, 1};
static const int dy[]={ 0,-1, 1, 0};
static const bool con[4][4]=
{
 {false,false,false,true },
 {false,false,true ,false},
 {false,true ,false,false},
 {true ,false,false,false}
 };

int X[100][100];
int Y[100][100];
int dir[100][100];
char ans[100][100];
int S[10000], nS;

int main()
{
	int T, H, W, c, k, x, y, m;
	int i, j, u, pv, ux, uy, v, ID;
	char label;

	scanf("%d",&T);
	c=1;
	while(T--){
		
		scanf("%d%d",&H,&W);
		
		for(i=0;i<H;i++)
			for(j=0;j<W;j++){
				scanf("%d",&X[i][j]);
				Y[i][j]=0;
				ans[i][j]=0;
			}
		
		nS=0;
		for(i=0;i<H;i++)
			for(j=0;j<W;j++){
				//Definindo direção de escoamento
				m=INF; v=sink;
				for(k=0;k<4;k++){
					x=i+dx[k]; y=j+dy[k];
					if(x>-1 && y>-1 && x<H && y<W)
						if(X[x][y]<X[i][j] && X[x][y]<m){
							m=X[x][y]; v=k;
						}
				}
				dir[i][j]=v;
				if(v==sink) S[nS++]=i*W+j;
			}
			
		
		ID=0;
		for(i=0;i<nS;i++){
			u=S[i];
			ux=u/W; uy=u%W;
			if(!Y[ux][uy]){
				ID++;
				Y[ux][uy]=ID;
				queue<int> Q;
				Q.push(u);
				while(!Q.empty()){
					u=Q.front(); Q.pop(); 
					ux=u/W; uy=u%W;
					Y[ux][uy]=ID; 
					for(k=0;k<4;k++){
						x=ux+dx[k]; y=uy+dy[k];
						if(x>-1 && y>-1 && x<H && y<W){
							pv=dir[x][y];
							if(pv!=sink)
							if(con[k][pv] && !Y[x][y])
								Q.push(x*W+y);
						}
					}
				}
			}
		}
		
		label='a';
		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
			if(!ans[i][j]){
				queue<int> Q;
				Q.push(i*W+j);
				
				ans[i][j]=label; 
				ID=Y[i][j];
				while(!Q.empty()){
					u=Q.front(); Q.pop();
					ux=u/W; uy=u%W;
					ans[ux][uy]=label;
					for(k=0;k<4;k++){
						x=ux+dx[k]; y=uy+dy[k];
						if(x>-1 && y>-1 && x<H && y<W)
							if(Y[x][y]==ID && !ans[x][y]) Q.push(x*W+y);
					}
				}
				label++;
			}
		
		printf("Case #%d:\n",c);
		for(i=0;i<H;i++){
			printf("%c",ans[i][0]);
			for(j=1;j<W;j++) printf(" %c",ans[i][j]);
			printf("\n");
		}
		
		c++;
	}
	return 0;
}

