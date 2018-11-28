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

typedef long long ll;

void init() {
}

bool solve(int P) {
	printf("Case #%d: ", P+1);

	ll N,K,B,T;
	if(scanf("%lld%lld%lld%lld", &N, &K, &B, &T) != 4)
		assert(!"Failed to read nkbt");

	vector<ll> xs, vs;
	xs.reserve(N);
	vs.reserve(N);

	for(int i = 0; i < N; ++i) {
		ll tmp;
		if(scanf("%lld", &tmp) != 1)
			assert(!"Failed to read");
		xs.push_back(tmp);
	}

	for(int i = 0; i < N; ++i) {
		ll tmp;
		if(scanf("%lld", &tmp) != 1)
			assert(!"Failed to read");
		vs.push_back(tmp);
	}

	int blockers = 0;
	int done = 0;
	int ret = 0;
	for(int i = N-1; done < K && i >= 0; --i) {
		ll fdist = vs[i] * T + xs[i];
		if(fdist >= B) {
			ret += blockers;
			++done;
		} else {
			++blockers;
		}
	}

	if(done == K) {
		printf("%d\n", ret);
	} else {
		assert(done < K);
		printf("IMPOSSIBLE\n");
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
