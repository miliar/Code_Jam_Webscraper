#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int a[111][111];
bool sink[111][111];
vector<pair<int, int> > d[111][111];
int dx[] = {-1,0,0,1};
int dy[] = {0,-1,1,0};
char ans[111][111];
bool c[111][111];
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		memset(a,0,sizeof(a));
		int n,m;
		scanf("%d %d\n",&n,&m);
		for(int i=1; i<=n; i++)
			for(int j=1; j<=m; j++)
				d[i][j].clear();
		memset(sink,false,sizeof(sink));
		for(int i=1; i<=n; i++){
			for(int j=1; j<=m; j++){
				scanf("%d ",&a[i][j]);
			}
		}
		memset(ans,0,sizeof(ans));
		vector<pair<int,pair<int,int> > > b;
		for(int i=1; i<=n; i++){
			for(int j=1; j<=m; j++){
				b.push_back(make_pair(-a[i][j],make_pair(i,j)));
			}
		}
		memset(c,false,sizeof(c));
		sort(b.begin(),b.end());
		for(int i=0; i<(int)b.size(); i++){
			int x,y;
			x = b[i].second.first;
			y = b[i].second.second;
			int low=a[x][y];
			int what=-1;
			for(int k=0; k<4; k++){
				int tx = x+dx[k];
				int ty = y+dy[k];
				if(tx>=1 && tx<=n && ty>=1 && ty<=m){
					if(low>a[tx][ty]){
						low=a[tx][ty];
						what=k;
					}
				}
			}
			if(what==-1){
				sink[x][y]=true;
			}
			else{
				d[x+dx[what]][y+dy[what]].push_back(make_pair(x,y));
				d[x][y].push_back(make_pair(x+dx[what],y+dy[what]));
			}
		}
		char alpha='a';
		for(int i=1; i<=n; i++){
			for(int j=1; j<=m; j++){
				if(c[i][j]==false){
					queue<pair<int,int> > q;
					q.push(make_pair(i,j));
					c[i][j]=true;
					ans[i][j]=alpha;
					while(!q.empty()){
						int x = q.front().first;
						int y = q.front().second;
						q.pop();
						for(int k=0; k<d[x][y].size(); k++){
							if(c[d[x][y][k].first][d[x][y][k].second]==false){
								q.push(d[x][y][k]);
								c[d[x][y][k].first][d[x][y][k].second]=true;
								ans[d[x][y][k].first][d[x][y][k].second]=alpha;
							}
						}
					}
					alpha++;
				}
			}
		}
		printf("Case #%d:\n",tc);
		for(int i=1; i<=n; i++){
			for(int j=1; j<=m; j++){
				printf("%c ",ans[i][j]);
			}
			printf("\n");
		}
	}
}
	