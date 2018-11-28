#include <cmath>
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

typedef unsigned long long int ull;
typedef long double ld;

int T, N, K;
string grid[51];
string rotgrid[51];

int oob(int x, int y) {
	return (x < 0 || y < 0 || x>= N || y>=N);
}

int iswant(int x, int y, char want) {
	if (oob(x,y)) return false;
	return rotgrid[y][x] == want;
}


int has(char want) {
	FOR(y,N) {
		FOR(x,N) {
			if (rotgrid[y][x] != want) continue;
			bool works[4]; // DIRS: R, D, DR, UR
			FOR(i,4) works[i] = true;
			for(int d = 1; d < K; d++) {
				works[0] &= iswant(x+d,y,want);
				works[1] &= iswant(x,y+d,want);
				works[2] &= iswant(x+d,y+d,want);
				works[3] &= iswant(x+d,y-d,want);
			}

			FOR(i,4) {
				if (works[i]) return true;
			}
		}
	}
	return false;
}

string ans() {
	int hasR = has('R'), hasB = has('B');
	if (hasR && hasB) return "Both";
	else if (hasR) return "Red";
	else if (hasB) return "Blue";
	else return "Neither";
}

void gravity() {
	bool change = true;
	while(change) {
		change = false;
		for(int y = N-1; y > 0; y--) {
			FOR(x,N) {
				if (rotgrid[y][x] == '.' && rotgrid[y-1][x] != '.') {
					rotgrid[y][x] = rotgrid[y-1][x];
					rotgrid[y-1][x] = '.';
					change = true;
				}
			}
		}
	}

	/*
	FOR(i,N) {
		cerr << rotgrid[i] << endl;
	}
	cerr << endl;
	*/
}

void rotate() {
	FOR(i,N) rotgrid[i] = grid[i];
	FOR(y,N) {
		FOR(x,N) {
			rotgrid[y][x] = grid[N-1-x][y];
		}
	}

	/*
	FOR(i,N) {
		cerr << rotgrid[i] << endl;
	}
	cerr << endl;
	*/
}

int main() {
	cin >> T;
	FOR(t,T) {
		cin >> N >> K;
		FOR(i,N) {
			grid[i].clear();
			rotgrid[i].clear();
		}
		FOR(i,N) {
			cin >> grid[i];
			//cerr << grid[i] << endl;
		}
		//cerr << endl;
		rotate();
		gravity();
		//cerr << "-------------" << endl;

		cout << "Case #" << t+1 << ": " << ans() << endl;
	}
	return 0;
}
	
