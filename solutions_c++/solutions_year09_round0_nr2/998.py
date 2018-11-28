#include <iostream>
#include <vector>

using namespace std;


int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int n,m,a[101][101];
char c[101][101];
int u[101][101],d[101][101];

bool check(int x, int y) {
	if(x < n && x > -1 && y < m && y > -1) {
		return true;
	}
 	return false;
}

int dir(int x, int y) {
	int min = 10001;
	int l,k,ans;
	for(int i = 0; i < 4; i++) {
		l = x + dx[i];
		k = y + dy[i];
		if(check(l,k) && min > a[l][k]) {
			min = a[l][k];
			ans = i;
		}
	}
	l = x + dx[ans];
	k = y + dy[ans];
	if(a[x][y] <= a[l][k]) return -1;
	return ans;
			
}



int main() {
	freopen("input","r",stdin);
	freopen("output","w",stdout);

	int t;
	cin >> t;
	for(int tc = 0; tc < t; tc++){
		cin >> n >> m;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
		 		cin >> a[i][j];
		   	c[i][j] = '0';
		   }
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				d[i][j] = dir(i,j);
			}
		}
		char cur = 'a'-1;
		memset(u,0,sizeof(u));
		vector<pair<int,int> > q;
		pair<int, int> p;
		int uk = 0;
		for(int l = 0; l < n; l++) {
			for(int k = 0; k < m; k++) {
				if(c[l][k] == '0') {
					q.push_back(make_pair(l,k));
					u[l][k] = 1;
					cur++;
					c[l][k] = cur;
				}
				while(uk < q.size()) {
					p = q[uk++];
					int x = p.first;
					int y = p.second;
					int di = d[x][y];
					if(di != -1 && u[x+dx[di]][y+dy[di]] == 0) { 
						q.push_back(make_pair(x+dx[di],y+dy[di]));
						u[x+dx[di]][y+dy[di]] = 1;
						c[x+dx[di]][y+dy[di]] = cur;
					}
					for(int i = 0; i < 4; i++) {
						if(check(x + dx[i],y + dy[i]) && u[x+dx[i]][y+dy[i]] == 0) {
							di = d[x + dx[i]][y + dy[i]];
							if(di != -1 && dx[i] + dx[di] == 0 && dy[i] + dy[di] == 0) {
								q.push_back(make_pair(x + dx[i],y + dy[i]));
								u[x+dx[i]][y+dy[i]] = 1;
								c[x+dx[i]][y+dy[i]] = cur;
              			}
						}
					}
		      }
			}
		}
		cout << "Case #" << tc+1 << ":" << endl;
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				cout << c[i][j] << " ";
		   }
		   cout << endl;
		}	
	}
 	return 0;
}