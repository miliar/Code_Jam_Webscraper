/**
 * Author: Shrey Banga
 */
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define FORn(i,n) FOR(i,0,n)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,v) for(typeof(v.begin()) i = v.begin(); i != v.end(); i++)

#if 0
#define DBG(args...) fprintf(stderr, args)
#else
#define DBG(args...)
#endif

#define MAXN 101

int compare (const void * a, const void * b) {
  return ( *(int*)a - *(int*)b );
}

int main2() {
  int t[MAXN];
  int N, S, p;

  scanf("%d %d %d", &N, &S, &p);

  FORn(i,N)
    scanf("%d", &t[i]);

  qsort(t, N, sizeof(int), compare);

  int count = 0;
  for(int i = N-1; i >= 0; i--) {
    int max = 0, r = t[i] % 3;

    switch(r) {
      case 0:
        max = t[i] / 3;
        break;
      case 1:
        max = (t[i] + 2) / 3;
        break;
      case 2:
        max = (t[i] + 1) / 3;
        break;
    }

    if(max >= p) {
        count++;
        //printf("s = %d, max = %d\n", t[i], max);
    } else if(max == (p-1) && t[i] >= 2 && S > 0 && (r == 0 || r == 2)) {
        S--;
        count++;
        //printf("*s = %d, max = %d\n", t[i], max+1);
    }
  }

  return count;
}

int main() {
	int T; scanf("%d", &T);

	FOR(i,0,T) {
		printf("Case #%d: %d\n", i+1, main2());
	}
}

