#include<iostream>
#include<cassert>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
using namespace std;
#define valid(i,j) (i>=0 && j >=0 && i < n && j < m)
int xx[] = { -1,0,0,1};
int yy[] = {0,-1,1,0};
int mat[110][110];
int ans[110][110];
int flow[110][110][2];
int main() {
	int t;
	scanf("%d",&t);
	int cas = 0;
	while(t--) {
		cas++;
		int n,m;
		scanf("%d%d",&n,&m);

		for (int i = 0 ; i < n ; ++i) {
			for (int j = 0; j < m ; ++j) {
				scanf("%d",&mat[i][j]);
				ans[i][j] = 0;
			}
		}
		vector<pair<int,int> > sinks;
		for (int i = 0 ; i < n ; ++i) {
			for (int j = 0; j < m ; ++j) {
				int state = true;
				int mini = INT_MAX;
				for ( int k = 0 ; k < 4 ; ++k) {
					int nx = i + xx[k];
					int ny = j + yy[k];
					if(valid(nx,ny) && mat[nx][ny] < mat[i][j]) {
						state = false;
						if(mat[nx][ny] < mini){
							mini = mat[nx][ny];
							flow[i][j][0] = nx;
							flow[i][j][1] = ny;
						}
					}
				}
				if (state){
					sinks.push_back(make_pair(i,j));
					flow[i][j][0] = i;
					flow[i][j][1] = j;

				}
			}
		}
		for(int i = 1 ; i <= sinks.size() ; ++i) {
			ans[sinks[i-1].first][sinks[i-1].second] = i;
			queue<pair<int,int> > q;
			q.push(make_pair(sinks[i-1].first,sinks[i-1].second));
			while(!q.empty()) {
				int x = q.front().first;
				int y = q.front().second;
				q.pop();
				for(int k = 0 ; k < 4; ++k){
					int nx = x + xx[k];
					int ny = y + yy[k];
					if(valid(nx,ny) && flow[nx][ny][0] == x && flow[nx][ny][1] == y) {
						ans[nx][ny] = i;
						q.push(make_pair(nx,ny));
					}
				}
			}

		}
		int ar[300] = {};
		int cnt = 'a';
		
		cout << "Case #" <<cas<<":"<<endl;
		for ( int i = 0 ; i < n ; ++i) {
			for ( int j = 0 ; j < m ; ++j) {
				if(!ar[ans[i][j]]) ar[ans[i][j]] = cnt++;
				if(j!=m-1) 
					cout << (char)(ar[ans[i][j]]) <<" ";
				else cout << (char)(ar[ans[i][j]]);
			}
			cout<<endl;
		}
	}
	return 0;
}
