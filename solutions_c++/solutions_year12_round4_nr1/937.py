#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
#define REP(I,N) for(int I=0;I<(N);++I)
#define FOR(I,A,B) for(int I=(A);I<=(B);++I)
#define FORD(I,A,B) for(int I=(A);I>=(B);--I)
#define FOREACH(I,C) for(__typeof((C.begin())) I=(C).begin();I!=(C).end();++I)
#define st first
#define nd second
#define mp make_pair
#define pb push_back

const int N = 10009;
int range[N];
int dist[N];
int length[N];
int n, d;

bool solve() {
  scanf("%d",&n);
  FOR(i,1,n) scanf("%d %d\n",&dist[i],&length[i]);
  scanf("%d",&d);
  range[1] = min(dist[1], length[1]);
  FOR(i,2,n) range[i] = -1;
  FOR(i,1,n) {
    if (range[i] == -1) continue;
    if (dist[i] + range[i] >= d) return true;
    FOR(j,i+1,n) {
      if (dist[j] <= dist[i] + range[i]) {
        range[j] = max(range[j], min(length[j], dist[j] - dist[i]));
      }
    }
  }
  return false;
}

int main() {
	int tests;
	scanf("%d\n",&tests);
	FOR(test,1,tests) {
		printf("Case #%d: ", test);
		if(solve()) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}

















