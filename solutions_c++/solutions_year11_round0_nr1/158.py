#include <stdio.h>
#include <algorithm>
#include <queue>
#include <utility>
using namespace std;

#define INF 1023456789

int cost[110][110][110];

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int t=1;t<=datasuu;t++){
		printf("Case #%d: ",t);
		
		int col[110],pos[110];
		int n;
		scanf("%d ",&n);
		for(int k=0;k<n;k++){
			char buf[10];
			scanf("%s%d ",buf,&pos[k]);
			if(buf[0]=='O'){
				col[k]=0;
			}else{
				col[k]=1;
			}
		}
		
		queue<pair<int,pair<int,int> > > que;
		for(int k=0;k<=n;k++)for(int i=1;i<=100;i++)for(int j=1;j<=100;j++)cost[k][i][j]=INF;
		cost[0][1][1]=0;
		que.push(make_pair(0,make_pair(1,1)));
		while(!que.empty()){
			pair<int,pair<int,int> > h=que.front();
			int x=h.second.first,y=h.second.second,pc=h.first;
			que.pop();
			if(pc==n){
				printf("%d\n",cost[pc][x][y]);
				break;
			}
			for(int dx=-1;dx<=1;dx++){
				for(int dy=-1;dy<=1;dy++){
					int nx=x+dx;
					int ny=y+dy;
					if(nx>=1 && nx<=100 && ny>=1 && ny<=100 && cost[pc][nx][ny]>cost[pc][x][y]+1){
						cost[pc][nx][ny]=cost[pc][x][y]+1;
						que.push(make_pair(pc,make_pair(nx,ny)));
					}
				}
			}
			if(col[pc]==0){
				if(x==pos[pc]){
					for(int dy=-1;dy<=1;dy++){
						int ny=y+dy;
						if(ny>=1 && ny<=100 && cost[pc+1][x][ny]>cost[pc][x][y]+1){
							cost[pc+1][x][ny]=cost[pc][x][y]+1;
							que.push(make_pair(pc+1,make_pair(x,ny)));
						}
					}
				}
			}else{
				if(y==pos[pc]){
					for(int dx=-1;dx<=1;dx++){
						int nx=x+dx;
						if(nx>=1 && nx<=100 && cost[pc+1][nx][y]>cost[pc][x][y]+1){
							cost[pc+1][nx][y]=cost[pc][x][y]+1;
							que.push(make_pair(pc+1,make_pair(nx,y)));
						}
					}
				}
			}
		}
	}
}