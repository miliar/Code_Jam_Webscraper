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

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;


const ll inf = 1LL<<40;

ll best[15][1100][15];

ll Best(int canmiss, int game, int row, const vi &M, const vvi &prices) {
	dprintf("Best(%d,%d, %d called\n", canmiss, game, row);
	assert(game >= 0);
	if(row == -1) {
		assert(game < (int) M.size());
		if(M[game] >= canmiss) {
			dprintf("Returning 0\n");
			return 0;
		}
		else {
			dprintf("Returning inf\n");
			return inf;
		}
	}

	assert(row >= 0);
	assert(row < (int) prices.size());
	assert(game < (int) prices[row].size());

	ll &ret = best[canmiss][game][row];
	if(ret != -1) {
		return ret;
	}
	ret = Best(canmiss + 1, 2*game, row - 1, M, prices) + Best(canmiss + 1, 2*game+1, row-1, M, prices);
	ret = min(ret, prices[row][game] + Best(canmiss, 2*game, row - 1, M, prices) + Best(canmiss, 2*game+1, row-1, M, prices));

	dprintf("Best(%d,%d, %d = %lld\n", canmiss, game, row, ret);
	return ret;
}


bool solve(int caseno) {
	printf("Case #%d:", caseno+1);
	int P;

	memset(best, -1, sizeof(best));

	if(scanf("%d", &P) != 1)
		assert(!"Fialed to read P");

	vector<int> M(1 << P);
	vector<vector<int> > prices(P);

	for(int i = 0; i < (1<<P); ++i) {
		if(scanf("%d", &M[i]) != 1)
			assert(!"Failed to read team");
	}

	for(int k = 0; k < P; ++k) {
		prices[k].resize((1<<(P-k-1)));
		for(int i = 0; i < (1<<(P-k-1)); ++i) {
			if(scanf("%d", &prices[k][i]) != 1)
				assert(!"Failed to read price");
		}
	}
	
	ll cost = Best(0, 0, P-1, M, prices);

	printf(" %lld\n", cost);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
