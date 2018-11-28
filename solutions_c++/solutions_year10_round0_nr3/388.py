#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <numeric>
//#include <string>
#include <map>
#include <vector>

using namespace std;
#define dprintf debug && printf
const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

typedef pair<long long, long long> pii;
typedef long long ll;

void init() {
}

bool solve(int P) {
	map<int, pii> seen;
	vector<ll> groups;
	ll r, k, n;
	if(scanf("%lld%lld%lld", &r, &k, &n) != 3) {
		assert(!"Failed to read input");
	}
	groups.reserve(n);

	for(int i = 0; i < n; ++i) {
		ll tmp;
		if(scanf("%lld", &tmp) != 1)
			assert(!"Failed to read group size");
		groups.push_back(tmp);
	}

	long long money = 0;

	if(accumulate(groups.begin(), groups.end(), 0ll) <= k) {
		money = (ll) r * (ll) accumulate(groups.begin(), groups.end(), 0ll);
	} else {
		int qpos = 0;
		bool looped = false;

		while(r) {
			ll size = k;
			ll curmoney = 0;
			while(size >= groups[qpos]) {
				size -= groups[qpos];
				curmoney += groups[qpos];
				++qpos;
				qpos %= groups.size();
			}
			--r;
			money += curmoney;
			dprintf("qpos: %d, k: %d, curmoney: %d, money: %lld\n", qpos, k, curmoney, money);

			// FIXME: ugly looped
			if(!looped && seen.find(qpos) != seen.end()) {
				pii loop = seen[qpos];
				loop.first++;
				loop.second += curmoney;
				looped = true;
				ll rounds = r / loop.first;
				dprintf("looping %d rounds (%lld coasters, %lld money \n", rounds, rounds * loop.first, rounds * loop.second);
				r -= rounds * loop.first;
				money += rounds * loop.second;
			} else {
				for(map<int, pii>::iterator it = seen.begin(); it != seen.end(); ++it) {
					it->second.first++;
					it->second.second += curmoney;
				}
				seen[qpos] = pii(0,0);
			}
		}
	}
	assert(money >= 0);

	printf("Case #%d: %lld\n", P+1, money);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
