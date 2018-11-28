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

bool solve(int P) {
	printf("Case #%d: ", P+1);
	int n;

	if(scanf("%d", &n) != 1)
		assert(!"no n");

	int bt = 0, bp = 1, ot = 0, op = 1;

	while(n--) {
		char ch[20];
		int pos;
		if(scanf("%3s%d", ch, &pos) != 2)
			assert(!"Failed to read pos");
		if(ch[0] == 'O') {
			ot += abs(op - pos) + 1;
			ot = max(ot, bt + 1);
			op = pos;
		} else if(ch[0] == 'B') {
			bt += abs(bp - pos) + 1;
			bt = max(bt, ot + 1);
			bp = pos;
		} else {
			assert(!"Bad robot");
		}
	}

	printf("%d\n", max(ot, bt));
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
