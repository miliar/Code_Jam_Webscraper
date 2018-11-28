#include <iostream>
#include <vector>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cmath>
#include <numeric>
#include <cassert>
#include <bitset>

#define pb push_back
#define SZ(v) ((int)(v).size())
#define REP(i, a) for(int i=0; i<(a); ++i)
#define SQR(a) ((a)*(a))
#define TR(v, it) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define ALL(v) (v).begin(), (v).end()

using namespace std;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;

vvi cmap;
vvi hmap;

char nextchar;
int h, w;
int jmp[][2]= {{-1,0}, {0,-1}, {0, 1}, {1, 0}};

char ffill(int y, int x){
	if(cmap[y][x] != '#')
		return cmap[y][x];
	else{
		int best = hmap[y][x];
		int besti = -1;
		REP(i, 4){
			int ny = y + jmp[i][0];
			int nx = x + jmp[i][1];
			if(ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
			if(hmap[ny][nx] < best){
				best = hmap[ny][nx];
				besti = i;
			}
		}
		if(besti == -1){
			return cmap[y][x] = nextchar++;
		}
		else
			return cmap[y][x] = ffill(y + jmp[besti][0], x + jmp[besti][1]);
	}
}

inline bool solve(int tc){
	scanf("%d%d", &h,&w);
	hmap.assign(h, vi(w));
	REP(i, h){
		REP(j, w){
			scanf("%d", &hmap[i][j]);
		}
	}
	cmap.assign(h, vi(w, '#'));
	nextchar = 'a';
	REP(i, h){
		REP(j, w){
			ffill(i, j);
		}
	}
	printf("Case #%d:\n", tc);
	REP(i, h){
		REP(j, w){
			printf("%c ", cmap[i][j]);
		}
		printf("\n");
	}
	return true;
}

int main (int argc, char const *argv[]) {
	int n; scanf("%d",&n);
	for(int k=1;solve(k)&&k<n;k++);
	return 0;
}