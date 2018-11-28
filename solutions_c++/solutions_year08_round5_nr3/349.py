/*
 1185 炮兵阵地
 fengyu05
 状态压缩DP + 滚动数组 + DFS预处理 + 最优性剪枝
**
  1.确定状态压缩的表示
  2.确定状态
  3.判断两种状态是否可以转移
  4.转移
*/
#include<iostream>
#include<algorithm>
#include<cassert>
using namespace std;
int countbit(int x){
	int re=0;
	while(x>0){
		re+=x%2;
		x/=2;
	}return re;
}
#define M 11
const int N=1<<M;
int n,m;
int valid[128][N];//可行放置
// valid[x][id]=countbit(id) :可行
// valid[x][id]=-1 :不可行
char map[M];//当前行地图，用于DFS
char X[M];
void DFS(int x,int pos){
	if(pos==m){
		int id=0;
		for(int i=0;i<m;i++){
			id=id*2+X[i];
		}
		valid[x][id]=countbit(id);
	}else{
		bool canplace=(map[pos]=='.');
		if(canplace){
			if(pos-1>=0&&X[pos-1]==1) canplace=false;
		}
		if(canplace){
			X[pos]=1;
			DFS(x,pos+1);
		}
		X[pos]=0;
		DFS(x,pos+1);
	}
}
int f[2][N];
int end;
bool safe(int x,int y){// x can behind y
	char map[16]={0};
	int cnt=0;
	while(x>0){
		int id=x%2;
		x/=2;
		if(id==1){
			int a=cnt-1;
			if(a>=0) map[a]=1;
			int b=cnt+1;
			if(b<m) map[b]=1;
		}
		cnt++;
	}
	cnt=0;
	while(y>0){
		int id=y%2;
		y/=2;
		if(id==1&&map[cnt]==1) return false;
		cnt++;
	}
	return true;
}
void solve(){
	int i,j;
	scanf("%d %d\n",&n,&m);
	end=(1<<m);
	memset(valid,-1,sizeof(valid));
	for(i=0;i<n;i++){
		int re=0;
		scanf("%s",map);
		memset(X,0,sizeof(X));
		DFS(i,0);//DFS确定可行放置
	}
	int _max=*max_element(valid[0],valid[0]+end);
	//
	//assert(*max_element(valid[1],valid[1]+end)==5);
	//
	if(n==1){ 
		printf("%d\n",_max);
		return;
	}
	memset(f[1],0,sizeof(f[1]));
	for(i=0;i<end;i++) if(valid[0][i]>=0){
		f[0][i]=valid[0][i];
	}
	//数组滚动
	for(int cnt=1;cnt<n;cnt++){
		int cur=cnt%2,pre=(cnt-1)%2;
		memset(f[cur],0,sizeof(f[cur]));
			for(j=end-1;j>=0;j--) if(valid[cnt-1][j]>=0){
				//if(f[pre][j]+m/2<_max) continue;//最优性剪枝
				for(int k=end-1;k>=0;k--) if(valid[cnt][k]>=0){//
					if( safe(k,j) ){
						int tmp=f[pre][j]+valid[cnt][k];
						if(f[cur][k]<tmp){
							if(tmp>_max) _max=tmp;
							f[cur][k]=tmp;							
						}
					}					
				}
			}
	}
	printf("%d\n",_max);
}
int main()
{	
	freopen("t.in", "r", stdin);
	freopen("t.out", "w", stdout);
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		solve();
	}
	return 0;
}