/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long ll;

char buf[1005], buf2[1005];
char buf3[1005];

void testcase() {
  vector<int> perm;
  int k;
  int n;
  scanf("%d", &k);
  FOR(i,0,k) perm.PB(i);
  scanf("%s", buf);
  n = strlen(buf);
  int res = INT_MAX;
  do {
	FOR(i,0,n) buf2[i] = buf[i];
	FOR(i,0,n) buf3[ perm[i%k]+(i/k)*k ] = buf2[i];
	int tmp_res = 0;
	char poprz = '&';
	FOR(i,0,n) if(buf3[i] != poprz) {
	  ++tmp_res;
	  poprz = buf3[i];
	}
	res = min(res, tmp_res);
  } while(next_permutation(perm.begin(), perm.end()));
  printf("%d", res);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,0,t) {
	printf("Case #%d: ", i+1);
	testcase();
	printf("\n");
  }
  return 0;
}
