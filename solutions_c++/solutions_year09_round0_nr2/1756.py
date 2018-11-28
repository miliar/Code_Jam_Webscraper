#include <cstdio>
#include <cstring>
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int H,W;
int par[10010],h[110][110];
char ans[110][110],next;
bool valid(int x,int y){return 0<=x&&x<H&&0<=y&&y<W;}
int en(int x,int y){return x*W+y;}
char root(int s){
	if(par[s]==s){
		if(ans[s/W][s%W]==0) ans[s/W][s%W]=next++;
		return s;
	}
	int rt=root(par[s]);
	ans[s/W][s%W]=ans[rt/W][rt%W];
	return rt;
}
int main(){
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas){
		scanf("%d %d",&H,&W);
		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j) scanf("%d",h[i]+j);
		}
		memset(ans,0,sizeof(ans));
		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j){
				int bi=i,bj=j;
				for(int k=0;k<4;++k){
					int x=i+dx[k],y=j+dy[k];
					if(valid(x,y)&&h[x][y]<h[bi][bj]){
						bi=x,bj=y;
					}
				}
				par[en(i,j)]=en(bi,bj);
			}
		}
		printf("Case #%d:\n",cas);
		next='a';
		for(int i=0;i<H;++i){
			for(int j=0;j<W;++j){
				root(en(i,j));
				putchar(ans[i][j]);putchar(' ');
			}
			puts("");
		}
	}
	return 0;
}
