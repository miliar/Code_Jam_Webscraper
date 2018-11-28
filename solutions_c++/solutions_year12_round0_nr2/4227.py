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
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	int N, S, p;
	scanf("%d%d%d", &N, &S, &p);
	int ret = 0;
	for(int i = 0; i < N; ++i) {
		int tmp;
		scanf("%d", &tmp);
		if(tmp < p)
			continue;
		if(tmp >= p + 2*(p-1))
			++ret;
		else if(tmp >= p + 2*(p-2) && S)
			--S, ++ret;
	}
	printf("%d\n", ret);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
