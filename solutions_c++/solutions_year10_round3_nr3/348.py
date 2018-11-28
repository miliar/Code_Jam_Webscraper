#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <complex>
#include <functional>
#include <bitset>
#include <string>
#include <valarray>
#include <algorithm>
using namespace std;

#define MP(a,b)     make_pair(a,b)
#define two(i)      (1<<(i))
#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,s,e)  for(int i=(s); i<(e); ++i)
#define FORD(i,s,e) for(int i=(s); i>=(e); --i)
typedef long long i64;
typedef unsigned long long u64;

string name = "CCC";
bool   is_file__ = true;

char  tempS[1024];
int  Row, Col;
char  mask[512][512];
bool  vst[512][512];
unsigned Pat[32];
int   h_val[512][512];
int   h_sum[512][512];
int   v_val[512][512];
int   v_sum[512][512];

void cover(int x, int y, int n) {
	REP(i, n) REP(j, n)
		vst[x+i][y+j] = true;
}
bool isOK(int x, int y, int n) {
	REP(i, n) {
		if(h_sum[x+i][y+n-1] - h_sum[x+i][y] != n-1)
			return false;
		if(v_sum[x+n-1][y+i] - v_sum[x][y+i] != n-1)
			return false;
	} return true;
}

int  calc(int n) {
	int  ans = 0;
	REP(i, Row) {
		if(i+n > Row) break;
		REP(j, Col) {
			if(j+n > Col) break;
			if(vst[i][j] || vst[i+n-1][j+n-1]
			|| vst[i+n-1][j] || vst[i][j+n-1]) continue;
			if(isOK(i, j, n)) {
				cover(i, j, n);
				++ans;
			}
		}
	} return ans;
}

void solve() {
	int  T;
	scanf("%d", &T);
	REP(Ti, T) {
		scanf("%d%d", &Row, &Col);
		REP(i, Row) {
			scanf("%s", tempS);
			int  k = 0;
			REP(j, (Col>>2)) {
				int  v = tempS[j];
				if(v>='A' && v<='F')
					v = 10 + v-'A';
				else
					v -= '0';
				mask[i][k++] = v>>3;
				mask[i][k++] = (v>>2)&1;
				mask[i][k++] = (v>>1)&1;
				mask[i][k++] = v&1;
			}
		}
		memset(h_val, 0, sizeof(h_val));
		memset(h_sum, 0, sizeof(h_sum));
		memset(v_val, 0, sizeof(v_val));
		memset(v_sum, 0, sizeof(v_sum));
		memset(vst, 0, sizeof(vst));
		for(int i=0; i<Row; ++i) {
			for(int j=1; j<Col; ++j) {
				h_val[i][j] = (mask[i][j] != mask[i][j-1]);
				h_sum[i][j] = h_sum[i][j-1] + h_val[i][j];
				//printf(" %2d", h_sum[i][j]);
			} //putchar('\n');
		} //puts("-----------------------");

		for(int j=0; j<Col; ++j) {
			for(int i=1; i<Row; ++i) {
				v_val[i][j] = (mask[i][j] != mask[i-1][j]);
				v_sum[i][j] = v_sum[i-1][j] + v_val[i][j];
			}
		}

		/*for(int i=0; i<Row; ++i) { for(int j=0; j<Col; ++j) {
				printf(" %2d", h_sum[i][j]);
			} putchar('\n');
		} puts("-----------------------");
		
		for(int i=0; i<Row; ++i) {for(int j=0; j<Col; ++j) {
				printf(" %2d", v_sum[i][j]);
			} putchar('\n');
		} puts("-----------------------");*/

		vector<pair<int, int> > ans;
		int  cnt = 0;
		for(int i=min(Row, Col); i>0; --i) {
			int c = calc(i);
			if(c > 0) {
				ans.push_back(MP(i, c));
			}
		}
		printf("Case #%d: %d\n", Ti+1, (int)ans.size());
		for(int i=0; i<(int)ans.size(); ++i)
			printf("%d %d\n", ans[i].first, ans[i].second);
	}
}


void set_file() {
	string in = name+".in";
	string ou = name + ".out";
	freopen(in.c_str(), "r", stdin);
	freopen(ou.c_str(), "w", stdout);
}

int  main(int argc, char* argv[])
{
	if(is_file__)
		set_file();
	solve();
	return 0;
}

