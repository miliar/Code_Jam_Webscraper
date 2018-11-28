#include <queue>
#include <vector>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define DBGV(_v) { REP(_i, v.size()) { cout << _v[_i] << "\t";} cout << endl;} 
typedef pair<int,int> PII;
#define OK(x, y) (x>=0 && y>=0 && x<h && y<w)
#define INF (int)1e6
#define sz size()
#define DEBUG(x) printf("%s", x);

int main() {
	int kases = GI;
	REP(kase, kases)	 {
		char cur = 'a';
		int h = GI, w = GI;
		int grid[101][101];
		char res[101][101];
		int visited[101][101];
		REP(i, 101) REP(j, 101) { 
			res[i][j] = '-';
			visited[i][j] = 0;
		}
		REP(i, h) REP(j, w) {
			grid[i][j] = GI;
		}
		REP(i, h) REP(j, w) {
			if (res[i][j] == '-') {
				//cout << "Empty cell at " << i << " " << j << endl;
				//Start a BFS from the current cell and see if ending cell has a character already.
				queue <PII> q;
				q.push(PII(i, j));
				vector <PII> path;
				path.push_back(PII(i, j));
				visited[i][j] = 1;
				int min = grid[i][j];				
				while (!q.empty()) {
					PII t = q.front();
					q.pop();
					int curx = t.first, cury = t.second;
					//cout << "Checking " << curx << " " << cury << endl;
					int nextx = -1, nexty = -1;
					for(int dx = -1; dx <= 1; dx++) {
						for(int dy = -1; dy <= 1; dy++) {
							if (dx*dy != 0 || (dx ==0 && dy==0)) continue;
							if (OK(curx+dx, cury+dy)) {
								if (grid[curx+dx][cury+dy] < min) {
									min = grid[curx+dx][cury+dy];
									nextx = curx+dx;
									nexty = cury+dy; 
								}
							}
						}
					}
					if (nextx != -1) {
						//cout << "Min value is " << min << endl;
						if (visited[nextx][nexty] == 1) {
							path.push_back(PII(nextx, nexty));
						}
						else {
							path.push_back(PII(nextx, nexty));
							q.push(PII(nextx, nexty));
							visited[nextx][nexty] = 1;
						}
					}
				}
				char now = 0;
				PII last = path[path.sz-1];
				if (res[last.first][last.second] != '-') { 
					//cout << "Tail value is not empty" << endl;
					now = res[last.first][last.second];
				}
				else {
					now = cur;
					cur++;
				}
				REP(l, path.sz) {
					PII t = path[l];
					res[t.first][t.second] = now;
				}
			}
		}
		
		printf("Case #%d:\n", kase+1);
		REP(i, h) {
			REP(j, w) {
				printf("%c", res[i][j]);
				if (j != w-1) printf(" ");				
			}
			printf("\n");
		}	
	}
	return 0;  
}
