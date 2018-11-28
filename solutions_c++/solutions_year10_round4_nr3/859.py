#include <iostream>
#include <algorithm>
#include <limits>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

#define forloop(i, s, t) for(__typeof(s) i = s; i t; i++)
#define forrloop(i, s, t) for(__typeof(s) i = s; i t; i--)
#define foreach(itr, c) for(__typeof((c).begin()) itr = (c).begin(); itr != (c).end(); itr++)

#define tpop(x) (x).top(); (x).pop();
#define fpop(x) (x).front(); (x).pop();
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()

#define chmin(a, b) a = min(a, b)
#define chmax(a, b) a = max(a, b)
//inline void chmin(int& a, const int b) { a = min(a, b); }
//inline void chmax(int& a, const int b) { a = max(a, b); }

#define debug(v) #v << '=' << v
#define pdebug(v, w) '(' << debug(v) << ',' << debug(w) << ')'

#define printgrid(g, y, x) forloop(i, 0, < y) {	forloop(j, 0, < x) cout<< g[i][j] << ' ';	cout << endl; }
#define rprintgrid(g, y, x) forloop(i, 0, < y) {	forloop(j, 0, < x) cout<< g[j][i] << ' ';	cout << endl; }
/*inline void printgrid(RandomAccessIterator g, int y, int x) {
	forloop(i, 0, < y) {
		forloop(j, 0, < x) cout<< g[i][j] << ' ';
		cout << endl;
	}
}*/

#define gcase int T; cin >> T; for(int gtest = 1; gtest <= T; gtest++)
#define gstate() cerr << "Case: " << gtest << '/' << T << endl
#define gout cout << "Case #" << gtest << ": "

const int INF = numeric_limits<int>::max();
const double EPS = INF*numeric_limits<double>::epsilon();

int main() {
	gcase {
		gstate();
		int R, bac = 0;
		int grid[100][100];
		forloop(i, 0, < 100) fill_n(grid[i], 100, 0);
		cin >> R;
		forloop(i, 0, < R) {
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			forloop(x, x1, <= x2) {
				forloop(y, y1, <= y2) {
					if(!grid[x-1][y-1]) bac++;
					grid[x-1][y-1] = 1;
				}
			}
		}
		int rounds = 0;
		//rprintgrid(grid, 10, 10);
		//cout << endl;
		while(bac > 0) {
			rounds++;
			vector< pair<int, int> > v;
			forloop(x, 0, < 100) {
				forloop(y, 0, < 100) {
					if(grid[x][y]) {
						if((x == 0 || !grid[x-1][y]) && (y == 0 || !grid[x][y-1])) {
							bac--;
							grid[x][y] = -1;
						}
					}
					else {
						if(x > 0 && grid[x-1][y] && y > 0 && grid[x][y-1]) {
							bac++;
							v.push_back(mp(x,y));
							//grid[x][y] = 1;
						}
					}
					if(x > 0 && grid[x-1][y] == -1) grid[x-1][y] = 0;
				}
			}
			forloop(y, 0, < 100) if(grid[99][y] == -1) grid[99][y] = 0;
			foreach(it, v) {
				grid[it->first][it->second] = 1;
			}
			//rprintgrid(grid, 10, 10);
			//cout << endl;
		}
		gout << rounds << endl;
	}
}
