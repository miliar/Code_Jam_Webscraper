#include <cmath>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
using namespace std;

#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define SETMIN(a,b) a = min(a,b)
#define SETMAX(a,b) a = max(a,b)
#define PB push_back
#define FORALL(i,v) for(typeof((v).end())i=(v).begin();i!=(v).end();++i)
#define CLR(x,a) memset(x,a,sizeof(x))
#define BEND(v) v.begin(),v.end()
#define MP make_pair
#define A first
#define B second

#define INF 0x7FFFFFFF

typedef unsigned long long int ull;
typedef long double ld;

#define MAXD 100

bool grid[MAXD + 2][MAXD + 2];

void printgrid() {
	for (int y = 1; y <= 10; y++) {
		for (int x = 1; x <= 10; x++) {
			cerr << grid[y][x];
		}
		cerr << endl;
	}
	cerr << "--" << endl;
}

int simulate() {
	bool living = true;
	int secs = 0;
	while(living) {
		living = false;
		secs ++;
		int nextgrid[MAXD + 2][MAXD + 2];
		FOR(i, MAXD + 2) FOR(j, MAXD + 2) nextgrid[i][j] = grid[i][j];

		for(int y = 1; y <= MAXD; y++) {
			for(int x = 1; x <= MAXD; x++) {
				if (grid[y][x] == 0 && grid[y-1][x] && grid[y][x-1]) {
					nextgrid[y][x] = 1;
					living = true;
				}
				if (grid[y][x] == 1) {
					if (!grid[y-1][x] && !grid[y][x-1]) {
						nextgrid[y][x] = 0;
					} else {
						living = true;
					}
				}
			}
		}

		FOR(i, MAXD + 2) FOR(j, MAXD + 2) grid[i][j] = nextgrid[i][j];

		//printgrid();
	}
	return secs;
}

int main() {
	int T;
	cin >> T;
	FOR(t,T) {
		CLR(grid,0);
		int R;
		cin >> R;
		FOR(i,R) {
			int x,X,y,Y;
			cin >> x >> y >> X >> Y;

			for(int j = y; j <= Y; j++) {
				for(int k = x; k <= X; k++) {
					grid[j][k] = 1;
				}
			}
		}

		printf("Case #%d: %d\n", t+1, simulate());
	}
	return 0;
}
