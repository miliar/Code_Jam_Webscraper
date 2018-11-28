#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

typedef vector<vector<int> > vvi;


vector<vector<int> > emptyfield() {
	vector<vector<int> > field(101);
	for(int i = 0; i < 101; ++i)
		field[i] = vector<int>(101);
	return field;
}

bool solve(int P) {
	printf("Case #%d:", P+1);

	vvi field = emptyfield();

	int r;
	if(scanf("%d", &r) != 1)
		assert(!"Failed to read r");


	for(int i = 0; i < r; ++i) {
		int x1,y1, x2,y2;
		if(scanf("%d%d%d%d", &x1, &y1, &x2, &y2) !=4 )
			assert(!"Fialed to read xy");
		assert(x1 <= x2);
		assert(y1 <= y2);
		for(int x = x1; x <= x2; ++x) {
			for(int y = y1; y <= y2; ++y) {
				field[x][y] = 1;
			}
		}
	}

	int round;
	const vvi empty = emptyfield();

	for(round = 0; field != empty ; ++round) {
		vvi newfield = emptyfield();
		for(int i = 1; i < 101; ++i) {
			for(int k = 1; k < 101; ++k) {
				if(field[i][k]) {
					if(field[i-1][k] || field[i][k-1]) {
						newfield[i][k] = 1;
					}
				} else {
					if(field[i-1][k] && field[i][k-1]) {
						newfield[i][k] = 1;
					}
				}
			}
		}
		field = newfield;
	}

	printf(" %d\n", round);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
