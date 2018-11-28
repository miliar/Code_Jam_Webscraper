#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <sstream>
#include <iostream>
#include <queue>
#include <set>
#include <map>

#define ABS(x) ((x)<0?-(x):(x))
#define SQR(x) ((x)*(x))
#define PB push_back
#define MP make_pair
#define SS stringstream
#define LL long long
#define LD long double
#define SZ(x) int(x.size())
#define ALL(x) x.begin(),x.end()
#define FOR(a,b) for(int a=0;a<b;a++)
#define DFOR(a,b) for(int a=b-1;a>=0;a--)
#define CLR(a,b) memset(a,b,sizeof(a))

#define inf 1000000
#define N 6100

using namespace std;

int l;
int minx[N], maxx[N], miny[N], maxy[N];

int dx[] = {0,-1,0,1};
int dy[] = {1,0,-1,0};

void solvecase() {
	int x = 3005, y = 3005, dir = 0;
	int area = 0;
	scanf("%d", &l);
	FOR(i, N) {
		minx[i] = miny[i] = inf;
		maxx[i] = maxy[i] = -inf;
	}
	FOR(i, l) {

		char s[100];
		int q;
		scanf("%s%d", s, &q);
		int len = strlen(s);
		FOR(j, q) FOR(z, len) {

			char cmd = s[z];
			int k = 1;

			if (cmd == 'L') {
				dir = (dir + k) % 4;
			} else if (cmd == 'R') {
				dir = (dir + 4 - k % 4) % 4;
			} else {
				int nx = x + dx[dir] * k;
				int ny = y + dy[dir] * k;
				area += x * ny - y * nx;
				if (dir == 0) {
					int Y = y;
					//for (int Y = y; Y < ny; Y++) {
						minx[Y] = min(minx[Y], x);
						maxx[Y] = max(maxx[Y], x);
					//}
				} else if (dir == 2) {
					int Y = ny;
					//for (int Y = ny-1; Y >= y; Y--) {
						minx[Y] = min(minx[Y], x);
						maxx[Y] = max(maxx[Y], x);
					//}
				} else if (dir == 3) {
					int X = x;
					//for (int X = x; X < nx; X++) {
						miny[X] = min(miny[X], y);
						maxy[X] = max(maxy[X], y);
					//}				
				} else {
					int X = nx;
					//for (int X = nx-1; X >= x; X--) {
						miny[X] = min(miny[X], y);
						maxy[X] = max(maxy[X], y);
					//}				
				}
				x = nx; y = ny;
			}		
		}
	}
	int res = -ABS(area) / 2;
	FOR(x, N) FOR(y, N) 
		if ((miny[x] <= y && y < maxy[x]) || (minx[y] <= x && x < maxx[y])) {
			res++;
		}
	printf("%d", res);	
}

void solve() {
	int n;
	scanf("%d\n", &n);
	FOR(i, n) {
		printf("Case #%d: ", i+1);
		solvecase();
		printf("\n");
	}
}

int main() {
	freopen("y", "rt", stdin);
	//freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	solve();
	return 0;
}