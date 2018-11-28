#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

bool solve(int P) {
	int dim;
	scanf("%d", &dim);
	vector<int> r;

	for(int i = 0; i < dim; ++i) {
		char buf[200];
		scanf("%s", buf);
		int hi = 0;
		for(int k = 0; k < dim; ++k) {
			if(buf[k] != '0')
				hi = k;
		}
		dprintf("Push: %d\n", hi);
		r.push_back(hi);
	}
	int ret = 0;

	for(int i = 0; i < dim; ++i) {
		for(int k = i; k < dim; ++k) {
			if(r[k] <= i) {
				int tmp = r[k];
				for(int m = k; m > i; --m)
					r[m] = r[m-1];
				r[i] = tmp;

				dprintf("Swap: %d, %d: %d vs %d\n", i, k, r[i], r[k]);
				ret += k - i;
				break;
			}
		}
	}

	printf("Case #%d: %d\n", P + 1, ret);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
