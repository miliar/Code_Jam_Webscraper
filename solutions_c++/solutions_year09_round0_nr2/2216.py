#include <cstdio>
#define AX 10005
#define FOR(i,a,b) for(int i=a; i<b; ++i)
using namespace std;

int T, H, W;
int mp[102][102], res[102][102];
char dec[AX];
int par[AX], rank[AX];

const int dirx[] = {-1,  0,  0, +1};
const int diry[] = { 0, -1, +1,  0};

void makeSet(int x) {
	par[x] = x, rank[x] = 0;
}

int findSet(int x) {
	if(x != par[x]) par[x] = findSet(par[x]);
	return par[x];
}

void setUnion(int x, int y) {
	x = findSet(x), y = findSet(y);
	if(rank[x] > rank[y]) par[y] = x;
	else par[x] = y;
	if(rank[x] == rank[y]) ++rank[y];
}

int main() {
	scanf("%d", &T);
	FOR(z,0,T) {
		scanf("%d%d", &H, &W);
		FOR(i,1,H+1) FOR(j,1,W+1) scanf("%d", &mp[i][j]), res[i][j] = -1;
		FOR(j,0,W+2) mp[0][j] = mp[H+1][j] = AX;
		FOR(i,0,H+2) mp[i][0] = mp[i][W+1] = AX;
		FOR(i,0,AX) makeSet(i), dec[i] = (char)NULL;

		int nextVal = 0;
		FOR(i,1,H+1) FOR(j,1,W+1) {
			int v = AX;
			if(res[i][j] == -1) res[i][j] = nextVal++;
			FOR(k,0,4) {
				int x = i + dirx[k], y = j + diry[k];
				if(mp[x][y] < v) v = mp[x][y];
			}
			if(v >= mp[i][j]) continue;
			FOR(k,0,4) {
				int x = i + dirx[k], y = j + diry[k];
				if(mp[x][y] != v) continue;
				if(res[x][y] == -1) {
					res[x][y] = res[i][j];
				}
				else if(findSet(res[i][j]) != findSet(res[x][y])) {
					setUnion(res[i][j], res[x][y]);
				}
				break;
			}
		}

		char nextLet = 'a';
		FOR(i,0,nextVal) {
			if(dec[findSet(i)] != (char)NULL) continue;
			dec[findSet(i)] = nextLet++;
		}

		printf("Case #%d:\n", z + 1);
		FOR(i,1,H+1) {
			FOR(j,1,W+1) printf("%c ", dec[findSet(res[i][j])]);
			printf("\n");
		}
	}
	return 0;
}
