#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
//#include <string>
//#include <map>
//#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	int n, k;

	if(scanf("%d%d", &n, &k) != 2)
		assert(!"Failed to read case");
	assert(n <= 30);

	printf("Case #%d: %s\n", P+1, k % (1<<n) == (1 << n) - 1 ? "ON" : "OFF");

	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
