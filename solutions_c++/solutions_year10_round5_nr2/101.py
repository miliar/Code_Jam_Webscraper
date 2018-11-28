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

typedef long long ll;

ll gcd(ll a, ll b) {
	if(b == 0)
		return a;
	return gcd(b, a % b);
}

ll lcm(ll a, ll b) {
	return a * (b / gcd(a, b));
}

ll bfs(const vector<ll> &pieces, ll totlen) {
	if(totlen == 0)
		return 0;
	//printf("Bfs, totlen: %lld\n", totlen);
	fflush(stdout);
	vector<int> dist(totlen, -1);
	queue<ll> q;
	q.push(0);
	dist[0] = 0;
	while(!q.empty()) {
		ll curlen = q.front();
		int curdist = dist[curlen];
		q.pop();
		for(vector<ll>::const_iterator it = pieces.begin(); it != pieces.end(); ++it) {
			ll newlen = curlen + *it;
			if(newlen == totlen) {
				return curdist + 1;
			} else if(newlen > totlen) {
				continue;
			} else if(dist[newlen] < 0) {
				dist[newlen] = curdist + 1;
				q.push(newlen);
			}
		}
	}
	return -1;
}

const long long inf = 1LL << 62;


bool solve(int P) {
	printf("Case #%d:", P+1);

	ll L, N;
	if(scanf("%lld%lld", &L, &N) != 2)
		assert(!"Failed to read RN");

	vector<ll> pieces;
	ll maxpiece = 0;

	for(int i = 0; i < N; ++i) {
		ll tmp;
		if(scanf("%lld", &tmp) != 1)
			assert(!"Failed to read piece");
		pieces.push_back(tmp);
		maxpiece = max(maxpiece, tmp);
	}

	long long real_ret = inf;
	
	for(int k = 0; k < 200; ++k) {
		ll newL = L % maxpiece + k * maxpiece;
		ll ret = (L - newL) / maxpiece;
		ll nret = bfs(pieces, newL);
		if(nret != -1) {
			real_ret = min(real_ret, ret + nret);
		}
	}

	if(real_ret == inf) {
		printf(" IMPOSSIBLE\n");
	} else {
		printf(" %lld\n", real_ret);
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
