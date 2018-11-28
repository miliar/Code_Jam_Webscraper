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

const int inf = 1<<30;

int best(map<map<int, int>, int> &Best, map<int, int> state) {
	bool done = true;
	int ret = 0;
	do {
		done = true;
		for(map<int, int>::const_iterator it = state.begin(); it != state.end(); ++it) {
			if(it->second > 1) {
				int tomove = it->second / 2;
				state[it->first - 1] += tomove;
				state[it->first + 1] += tomove;
				if(it->second == 2 * tomove) {
					state.erase(it->first);
				} else {
					state[it->first] -= 2 * tomove;
				}
				ret += tomove;
				done = false;
				break;
			}
		}
	} while(!done);
	return ret;
}

bool solve(int P) {
	printf("Case #%d:", P+1);
	map<map<int, int>, int> Best;

	int C;
	if(scanf("%d", &C) != 1)
		assert(!"Failed to read C");

	map<int, int> initial;
	for(int i = 0; i < C ; ++i) {
		int a, b;
		if(scanf("%d%d", &a, &b) != 2)
			assert(!"Failed to read ab");
		initial[a] = b;
	}

	printf(" %d\n", best(Best, initial));
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
