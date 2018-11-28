#include <cstdio>
#include <cstring>
using namespace std;

const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};

const int maxn=128;
int mat[maxn][maxn];
char lab[maxn][maxn];
char trans[26];

int calc(int x,int y){
	int rst=-1;
	int cur=mat[x][y];
	for(int i=0;i<4;++i){
		int a=x+dx[i],b=y+dy[i];
		if(mat[a][b]>=cur)continue;
		rst=i;
		cur=mat[a][b];
	}
	return rst;
}
void label(int x,int y,char c){
	lab[x][y]=c;
	int s=calc(x,y);
	for(int i=0;i<4;++i){
		if(i==s)continue;
		int a=x+dx[i],b=y+dy[i];
		if(lab[a][b])continue;
		int t=calc(a,b);
		if(dx[i]+dx[t]==0&&dy[i]+dy[t]==0){
			label(a,b,c);
		}
	}
}

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int H,W;
		scanf("%d%d",&H,&W);
		memset(mat,0x7f,sizeof(mat));
		for(int i=1;i<=H;++i)
			for(int j=1;j<=W;++j)
				scanf("%d",&mat[i][j]);
		int labels=0;
		memset(lab,0,sizeof(lab));
		for(int i=1;i<=H;++i)
			for(int j=1;j<=W;++j){
				if(calc(i,j)==-1){
					label(i,j,labels++);
				}
			}
		memset(trans,0,sizeof(trans));
		char cur='a';
		for(int i=1;i<=H;++i)
			for(int j=1;j<=W;++j){
				char c=lab[i][j];
				if(!trans[c])
					trans[c]=cur++;
			}
		printf("Case #%d:\n",t);
		for(int i=1;i<=H;++i){
			putchar(trans[lab[i][1]]);
			for(int j=2;j<=W;++j)
				printf(" %c",trans[lab[i][j]]);
			puts("");
		}
	}
}
