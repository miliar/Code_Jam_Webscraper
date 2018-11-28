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

vector<ll> primes;

void init() {
	const int MAXNUM = 1000000;
	vector<int> notprime(MAXNUM);
	primes.reserve(100000);
	primes.push_back(2);
	for(int i = 3; i < MAXNUM; i += 2) {
		if(notprime[i]) continue; 
		primes.push_back(i);
		for(int k = 2 * i; k < MAXNUM; k += i)
			notprime[k] = 1;
	}
	//printf("%zu\n", primes.size());
}

ll normalize(ll x, ll prime) {
	x %= prime;
	while(x < 0)
		x += prime;
	return x;
}
ll euclid(ll a, ll b, ll &x, ll &y) {
	if (b) {
		ll d = euclid(b, a % b, y, x);
		return y -= a/b * x, d;
	}
	return x = 1, y = 0, a;
}

ll invert(ll x, ll prime) {
	x = normalize(x, prime);
	ll x1, x2;
	ll tmp = euclid(x, prime, x1, x2);
	if(tmp != 1) {
		printf("EEEP! gcd(%lld, %lld) = %lld\n", x, prime, tmp);
		assert(false);
	}
	ll ret = normalize(x1, prime);
	assert( (ret * x) % prime == 1);
	return ret;
}

int solution(ll prime, const vector<ll> &observations) {
	if(observations.size() < 3) {
		if(observations[0] == observations[1])
			return observations[0];
		return -2;
	}

	for(vector<ll>::const_iterator it = observations.begin(); it != observations.end(); ++it) {
		if(*it >= prime)
			return -1;
	}

	ll a;
	if(observations[1] == observations[0]) {
		if(observations[1] != observations[2])
			return -1;
		a = 0;
	} else {
		a = normalize((observations[2] - observations[1]) * invert(observations[1] - observations[0], prime), prime);
	}
	ll b = normalize(observations[1] - observations[0] * a, prime);
	assert(normalize(observations[0] * a + b, prime) == observations[1]);
	assert(normalize(observations[1] * a + b, prime) == observations[2]);
	for(int i = 3; i < (int) observations.size(); ++i) {
		if(normalize(observations[i-1] * a + b, prime) != observations[i])
			return -1;
	}
	ll next = normalize(observations[observations.size() - 1] * a + b, prime);
	return next;
}

bool solve(int P) {
	printf("Case #%d:", P+1);
	int D, K;

	if(scanf("%d%d", &D, &K) != 2)
		assert(!"Failed to read DK");

	int maxval = 1;
	for(int i = 0; i < D; ++i)
		maxval *= 10;

	vector<ll> observations(K);
	for(int i = 0; i < K; ++i) {
		if(scanf("%lld", &observations[i]) != 1)
			assert(!"Failed to read os");
		assert(observations[i] < maxval);
	}

	int output = -1;
	bool multiple = false;
	for(vector<ll>::iterator it = primes.begin(); it != primes.end() && *it < maxval && !multiple; ++it) {
		int tmp_sol = solution(*it, observations);
		if(tmp_sol != -1) {
			if(tmp_sol == -2) {
				multiple = true;
			} else if (output == -1) {
				output = tmp_sol;
			} else if(output != tmp_sol) {
				multiple = true;
			}
		}
	}
	if(output == -1 || multiple) {
		printf(" I don't know.\n");
	} else {
		printf(" %d\n", output);
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
