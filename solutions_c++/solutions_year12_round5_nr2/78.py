#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>
#define maxn (105)
using namespace std;

int dx[]={-1,-1,0,0,1,1};
int dy[]={0,-1,-1,1,0,1};

typedef pair<int,int> Tpair;
int S,M,test;

int X[105],Y[105];
queue<Tpair> Q;
vector<Tpair>corners,edge[10];
bool stone[maxn][maxn];
bool g[10][55][10][55];
bool vis[maxn][maxn];

bool isedge(int i,int j){
	return i==1 || j==1 || j-i==S-1 || i-j==S-1 || i==2*S-1 || j==2*S-1;
}
bool check(int i,int j){
	return abs(i-j)<=S-1 && i>=1 && i<=2*S-1 && j>=1 && j<=2*S-1;
}
void getcorners(){
	corners.clear();
	corners.push_back(make_pair(1,1));
	corners.push_back(make_pair(1,S));
	corners.push_back(make_pair(S,2*S-1));
	corners.push_back(make_pair(2*S-1,2*S-1));
	corners.push_back(make_pair(2*S-1,S));
	corners.push_back(make_pair(S,1));
}
void getedge1(){
	edge[1].clear();
	for (int i=0;i<S;i++) edge[1].push_back(make_pair(1,1+i));
}
void getedge2(){
	edge[2].clear();
	for (int i=0;i<S;i++) edge[2].push_back(make_pair(1+i,S+i));
}
void getedge3(){
	edge[3].clear();
	for (int i=0;i<S;i++) edge[3].push_back(make_pair(S+i,2*S-1));
}
void getedge4(){
	edge[4].clear();
	for (int i=0;i<S;i++) edge[4].push_back(make_pair(2*S-1,2*S-1-i));
}
void getedge5(){
	edge[5].clear();
	for (int i=0;i<S;i++) edge[5].push_back(make_pair(2*S-1-i,S-i));
}
void getedge6(){
	edge[6].clear();
	for (int i=0;i<S;i++) edge[6].push_back(make_pair(S-i,1));
}
void getedges(){
	getedge1();
	getedge2();
	getedge3();
	getedge4();
	getedge5();
	getedge6();
}
void bfs(int x,int y,bool boo){
	vis[x][y]=true;
	Q.push(make_pair(x,y));
	for (;!Q.empty();Q.pop()){
		Tpair T=Q.front();
		int x=T.first,y=T.second;
		for (int d=0;d<6;d++){
			int tx=x+dx[d],ty=y+dy[d];
			if (check(tx,ty) && !vis[tx][ty] && stone[tx][ty]==boo){
				vis[tx][ty]=true;
				Q.push(make_pair(tx,ty));
			}
		}
	}
}
void bfs2(int x,int y){
	vis[x][y]=true;
	Q.push(make_pair(x,y));
	for (;!Q.empty();Q.pop()){
		Tpair T=Q.front();
		int x=T.first,y=T.second;
		for (int i=1;i<=6;i++)
			for (int j=1;j<edge[i].size()-1;j++){
			int tx=i,ty=j;
			if (g[x][y][tx][ty] && !vis[tx][ty]){
				vis[tx][ty]=true;
				Q.push(make_pair(tx,ty));
			}
		}
	}
}
bool check_bridge(){
	for (int k1=1;k1<=6;k1++)
		for (int k2=0;k2<edge[k1].size();k2+=S-1)
			for (int i1=k1+1;i1<=6;i1++)
				for (int i2=0;i2<edge[i1].size()-1;i2+=S-1){
					if (g[k1][k2][i1][i2] && 
					(edge[k1][k2].first!=edge[i1][i2].first 
					|| edge[k1][k2].second!=edge[i1][i2].second)) return true;
				}
	return false;
}
bool check_fork(){
	/*for (int k1=1;k1<=6;k1++)
		for (int k2=1;k2<edge[k1].size()-1;k2++)
			for (int i1=k1+1;i1<=6;i1++)
				for (int i2=1;i2<edge[i1].size()-1;i2++)
					for (int j1=i1+1;j1<=6;j1++)
						for (int j2=1;j2<edge[j1].size()-1;j2++){
							if (g[k1][k2][i1][i2] && g[i1][i2][j1][j2]) return true;
						}*/
	return false;
}
bool check_ring(){
	for (int i=1;i<=2*S-1;i++)
		for (int j=1;j<=2*S-1;j++){
			if (!check(i,j)) continue;
			if (stone[i][j]) continue;
			if (isedge(i,j)) continue;
			if (!vis[i][j]) return true;
		}
	return false;
}
int main(){
	freopen("i.txt","r",stdin);
	int cnt=1;
	for (scanf("%d",&test);test--;cnt++){
		printf("Case #%d: ",cnt);
		scanf("%d%d",&S,&M);
		getcorners();
		getedges();
		memset(stone,0,sizeof(stone));
		bool ok=false;
		for (int i=1;i<=M;i++) scanf("%d%d",&X[i],&Y[i]);
		for (int L=1;L<=M;L++){
			int x,y;
			x=X[L];
			y=Y[L];
			stone[x][y]=true;
			bool ok1,ok2,ok3;
			ok1=ok2=ok3=false;
			memset(g,0,sizeof(g));
			for (int i=1;i<=6;i++)
				for (int j=0;j<edge[i].size();j++){
					int x=edge[i][j].first,y=edge[i][j].second;
					if (stone[x][y]) g[i][j][i][j]=true;
				}
			for (int i=1;i<=6;i++)
				for (int j=0;j<edge[i].size();j++){
					int x=edge[i][j].first,y=edge[i][j].second;
					if (!stone[x][y]) continue;
					memset(vis,0,sizeof(vis));
					bfs(x,y,true);
					for (int ii=1;ii<=6;ii++)
						for (int jj=0;jj<edge[ii].size();jj++){
							int tx=edge[ii][jj].first,ty=edge[ii][jj].second;
							if (vis[tx][ty]) g[i][j][ii][jj]=true;
						}
				}
			for (int i=1;i<=6;i++)
				for (int j=1;j<edge[i].size()-1;j++)if (g[i][j][i][j]){
					memset(vis,0,sizeof(vis));
					bfs2(i,j);
					int c=1,o=0;
					for (int ii=1;ii<=6;ii++) if (ii!=i && ii!=o)
						for (int jj=1;jj<edge[ii].size()-1;jj++) if (vis[ii][jj]){
							c++;
							o=ii;
							break;
						}
					if (c>=3) ok2=true;			
				}
			/*for (int k1=1;k1<=6;k1++)
				for (int k2=0;k2<edge[k1].size();k2++)
					for (int i1=1;i1<=6;i1++)
						for (int i2=0;i2<edge[i1].size();i2++)
							for (int j1=1;j1<=6;j1++)
								for (int j2=0;j2<edge[j1].size();j2++){
									if (g[i1][i2][j1][j2] && g[j1][j2][k1][k2]) g[i1][i2][k1][k2]=true;
								}*/
			ok1=check_bridge();
		//	ok2=check_fork();
			memset(vis,0,sizeof(vis));
			for (int i=1;i<=6;i++)
				for (int j=0;j<edge[i].size();j++){
					int x=edge[i][j].first,y=edge[i][j].second;
					if (vis[x][y] || stone[x][y]) continue;
					bfs(x,y,false);
				}
			ok3=check_ring();
			if (ok1 || ok2 || ok3){
				ok=true;
				bool first=true;
				if (ok1){
					printf("bridge");
					first=false;
				}
				if (ok2){
					if (!first) printf("-");
					printf("fork");
					first=false;
				}
				if (ok3){
					if (!first) printf("-");
					printf("ring");
					first=false;
				}
				printf(" in move %d\n",L);
				break;
			}
		}
		if (!ok) puts("none");
	}
	return 0;
}
