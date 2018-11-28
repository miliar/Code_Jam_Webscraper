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

const ll MOD = 100003;

ll nsol[501][501];

void init() {
	memset(nsol, -1, sizeof(nsol));
}

ll choice(int n, int k) {
	if(k > n) {
		//printf("(%d,%d) = %d\n", n,k,0);
		return 0;
	}
	k = max(k, n-k);

	ll ret = 1;
	for(int i = 1; i <= n - k; ++i) {
		ret *= k + i;
		ret /= i;
		ret %= MOD;
	}
	//printf("(%d,%d) = %lld\n", n,k,ret);
	return ret;
}

ll Nsol(int n, int k) {
	if(n == 1)
		return 0;
	if(k == 1)
		return 1;
	assert(n > 1);
	assert(k > 1);

	ll &ret = nsol[n][k];
	if(ret != -1)
		return ret;
	ret = 0;
	for(int i = 1; i < k; ++i) {
		ret += Nsol(k, i) * choice(n - k - 1, k - i - 1);
		ret %= MOD;
	}
	//printf("%d,%d = %lld\n", n, k, ret);
	return ret;
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	int n;
	if( scanf("%d", &n) != 1)
		assert(!"Failed to read");

	ll ret = 0;
	for(int i = 1; i < n; ++i) {
		ret += Nsol(n, i);
		ret %= MOD;
	}
	printf("%lld\n", ret);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
