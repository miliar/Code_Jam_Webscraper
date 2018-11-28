#include <cstdio>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <cassert>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> PII;
#define MP make_pair
#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

int tab[200000];
int nums[200];

const int INFTY = 100000000;

priority_queue<PII> PQ;

int main () {
  int number_of_tests;
  scanf("%d", &number_of_tests);
  REP (test_number, number_of_tests) {
    printf("Case #%d: ", test_number+1);
		ll L;
		scanf("%lld", &L);
    int N;
		scanf("%d", &N);
		REP (i, N) {
			scanf("%d", &nums[i]);
		}
    sort(&nums[0], &nums[N]);
		int P = nums[N-1];
		REP (i, P+1) tab[i] = INFTY;
		tab[0] = 0;
		PQ.push(MP(0,0));
		while (!PQ.empty()) {
			PII PR = PQ.top();
			PQ.pop();
			if (tab[PR.second] == PR.first) {
				REP (i, N-1) {
					int cur = PR.second + nums[i];
					int crc = PR.first + 1;
					if (cur >= P) {crc -= 1; cur -= P;}
					if (tab[cur] > crc) {
						PQ.push(MP(crc,cur));
						tab[cur] = crc;
					}
				}
			}
		}
		int R = (int) (L % (ll) P);
		ll res = (L / P);
		res += (ll) tab[R];
		if (tab[R] == INFTY) printf("IMPOSSIBLE\n"); else printf("%lld\n", res);
  }
  return 0;
}

