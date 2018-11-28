#include <iostream>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <sstream>
using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef stack<int> STI;
typedef set<int> SI;
typedef queue<int> QI;
typedef vector<VI> VVI;
typedef vector<PII> VPII;
typedef stack<PII> STPII;
typedef set<PII> SPII;
typedef queue<PII> QPII;
#define oo 1<<30
#define ooLL 1000000000000LL
#define MOD 10007
#define MAXW 101
bool rock[MAXW][MAXW];
int moves[2][2] = {{-1,-2},{-2,-1}};
long long mem[MAXW][MAXW];
long long doit(int r, int c) {
	if(r == 0 && c == 0)
		return 1;
	if(mem[r][c] >= 0)
		return mem[r][c];
	long long ret = 0;
	for(int i = 0; i < 2; ++i) {
		int r2 = r+moves[i][0];
		int c2 = c+moves[i][1];
		if(r2 >= 0 && c2 >= 0 && !rock[r2][c2]) {
			ret = (ret + doit(r2,c2)) % MOD;
		}
	}
	mem[r][c] = ret;
	return ret;
}
int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int W,H,R;
		cin >> H >> W >> R;
		for(int i = 0; i < H; ++i)
			for(int j = 0; j < W; ++j) {
				rock[i][j] = false;
				mem[i][j] = -1;
			}
		for(int i = 0; i < R; ++i) {
			int r,c;
			cin >> r >> c;
			rock[--r][--c] = true;
		}
		cout << "Case #" << t << ": " << doit(H-1,W-1) << endl;
	}
	return 0;
}
