#ifdef DEBUG
	#define D(x...) fprintf(stderr,x);
#else
	#define D(x...) 0
#endif
#include <cstdio>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

char grid[64][64];
int R, C;
int caver[10], cavec[10];
int nCaves;
int curcaver, curcavec;

vector<vector<bool> > seen;
void resetSeen() {seen = vector<vector<bool> >(R, vector<bool>(C));}

set<pair<int, int> > curflag;
void initFlagDFS(int r, int c) {
	if (seen[r][c]) return;
	if (r < 0 || c < 0 || r >= R || c >= C) return;
	if (grid[r][c] == '#') return;
	seen[r][c] = 1;
	curflag.insert(make_pair(r,c));
	initFlagDFS(r-1,c);
	initFlagDFS(r,c-1);
	initFlagDFS(r,c+1);
}

set<set<pair<int, int> > > flagseen;
int dr[3] = {1,0,0}, dc[3] = {0,-1,1};
bool flagDFS(set<pair<int,int> > flag) {
	if (flagseen.count(flag)) return false;
	if (flag.size() == 0) return false;
	if (flag.size() == 1 && (*(flag.begin())) == make_pair(curcaver,curcavec)) return true;
	for (set<pair<int,int> >::iterator itr = flag.begin(); itr != flag.end(); itr++) {
		if (curflag.count(*itr) == 0) return false;
	}
	flagseen.insert(flag);
	for (int k = 0; k < 3; k++) {
		set<pair<int,int> > newflag;
		for (set<pair<int,int> >::iterator itr = flag.begin(); itr != flag.end(); itr++) {
			int nr = itr->first + dr[k];
			int nc = itr->second + dc[k];
			if (nr < 0 || nc < 0 || nr >= R || nc >= C || grid[nr][nc] == '#') {
				nr = itr->first;
				nc = itr->second;
			}
			newflag.insert(make_pair(nr,nc));
		}
		if (flagDFS(newflag)) {
			return true;
		}
	}

	return false;
}

int main() {
	int nTests;
	scanf("%d ",&nTests);
	for (int test=1;test<=nTests;test++) {
		if (1) fprintf(stderr,"Case %d/%d\n",test,nTests);
		scanf("%d%d ",&R,&C);
		for (int i = 0; i < R; i++) scanf("%s ",&grid[i]);

		nCaves = 0;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (grid[i][j] >= '0' && grid[i][j] <= '9') {
					caver[grid[i][j]-'0'] = i;
					cavec[grid[i][j]-'0'] = j;
					nCaves = max(nCaves, grid[i][j]-'0'+1);
				}
			}
		}

		printf("Case #%d:\n",test);
		for (int cave = 0; cave < nCaves; cave++) {
			resetSeen();
			curflag = set<pair<int,int> >();
			initFlagDFS(caver[cave],cavec[cave]);

			int nC = curflag.size();

			flagseen = set<set<pair<int, int> > >();
			curcaver = caver[cave];
			curcavec = cavec[cave];
			bool lucky = flagDFS(curflag);

			printf("%d: %d %s\n",cave,nC,lucky?"Lucky":"Unlucky");
		}
		
		
	}
}
