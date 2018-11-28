#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int H,W;
int g[200][200];
int cnt[200][200];
const int mod=10007;
int dx[]={2,1};
int dy[]={1,2};
int ans;

int dfs(int x,int y){
	if(cnt[x][y]!=-1)return cnt[x][y];
	if(x==H&&y==W){
		//ans=(ans+1)%mod;
		cnt[x][y]=1;
		return 1;
	}
	int xx,yy;
	int tot=0;
	for(int i=0;i<2;i++){
		xx=x+dx[i];yy=y+dy[i];
		if(xx>=1&&xx<=H && yy>=1 && yy<=W && g[xx][yy]==0){
			tot=(tot+dfs(xx,yy))%mod;
		}
	}
	cnt[x][y]=tot;
	return tot;
}

int main(){
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	int i,j,k,x,y,t,R;
	scanf("%d",&t);
	for(int ca=1;ca<=t;ca++){
		scanf("%d%d%d",&H,&W,&R);
		memset(g,0,sizeof(g));
		while(R--){
			scanf("%d%d",&x,&y);
			g[x][y]=1;
		}
		 ans=0;
		 memset(cnt,-1,sizeof(cnt));
		dfs(1,1);
		
		printf("Case #%d: %d\n",ca,cnt[1][1]);
	}
	return 0;
}

		