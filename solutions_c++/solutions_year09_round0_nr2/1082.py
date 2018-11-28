#include <iostream>
#include <string>
#include <set>
#include <vector>

#define forn(i, n) for(int i = 0; i < int(n); i++)
#define sz(s) s.size()
#define X first
#define Y second
using namespace std;
int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};
vector<pair<int, int> > b[200][200];
int a[200][200], h, w;
char ans[200][200];
bool inplace(int x, int y){
	return x >= 0 && x < h && y >= 0 && y < w;
}
void dfs(int x, int y, char c){
	ans[x][y] = c;
	forn(i, b[x][y].size()){
		if (ans[b[x][y][i].X][b[x][y][i].Y] == '0'){
			ans[b[x][y][i].X][b[x][y][i].Y] = c;
			dfs(b[x][y][i].X, b[x][y][i].Y, c);
		}
	}
	
}
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin >> t;
	forn(qw, t){
		cin >> h >> w;
		forn(i, h){
			forn(j, w){
				cin >> a[i][j];
				ans[i][j] = '0';
				b[i][j].resize(0);
			}
		}
		forn(i, h){
			forn(j, w){
				int min_ = 1000 * 1000 * 1000, x = -1, y = -1;
				forn(k, 4){
					if (inplace(dx[k] + i, dy[k] + j) && min_ > a[dx[k] + i][dy[k] + j] ){
						min_ = min(min_, a[dx[k] + i][dy[k] + j]);
						x = i + dx[k];
						y = j + dy[k];
					}
				}
				if (min_ < a[i][j]){
					b[i][j].push_back(make_pair(x, y));
					b[x][y].push_back(make_pair(i, j));
				}
			}
		}
		char l = 'a';
		forn(i, h){
			forn(j, w){
				if (ans[i][j] == '0'){
					dfs(i, j, l);
					l = l + 1;
				}
			}
		}
		cout << "Case #" << qw + 1 << ":" << endl;
		forn(i, h){
			forn(j, w){
				cout << ans[i][j] << " ";
			}
			cout << endl;
		}
	}
	return 0;
}