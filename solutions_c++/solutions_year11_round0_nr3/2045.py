
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

const int inf = (1 << 28) + 42;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);

	int n;
	if(scanf("%d", &n) != 1)
		assert(!"No n");

	int minnum = inf;
	int val = 0;
	int tot = 0;

	for(int i = 0; i < n; ++i) {
		int tmp;
		if(scanf("%d", &tmp) != 1)
			assert(!"Failed to read val");

		minnum = min(minnum, tmp);
		tot += tmp;
		val ^= tmp;
	}

	if(val) {
		printf("NO\n");
	} else {
		printf("%d\n", tot - minnum);
	}
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
