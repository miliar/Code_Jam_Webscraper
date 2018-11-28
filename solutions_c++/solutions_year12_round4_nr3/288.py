#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
using namespace std;

#define REP(i,n) for(int i = 0; i < (n); ++i)
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define FORE(it,V) for(__typeof(V.begin()) it = V.begin(); it != V.end(); ++it)
#define FI first
#define SE second
#define PB push_back
#define MP make_pair
typedef long long LL;

int perm[11];
int maksior[10];

void printout(int n) {
  REP(i,n-1) printf("%d ", perm[i]);
  printf("%d\n", perm[n-1]);
}

void testcase() {
  int n;
  srand(time(NULL));
  scanf("%d", &n);
  REP(i,n+1) perm[i] = i;
  REP(i,n-1) {
    scanf("%d", maksior+i);
    --maksior[i];
  }
  REP(i,n-1) if (maksior[i] <= i) {
    printf("Impossible\n");
    return;
  }

  do {
    bool ok = true;
    REP(i,n-1) {
      FOR(k,i+1,maksior[i]-1)
	if ( (perm[maksior[i]] - perm[i])*(k-i) <= (perm[k]-perm[i])*(maksior[i]-i)) {
	  ok = false;
	  break;
	}

      FOR(k,maksior[i]+1,n-1) {
	if ( (perm[maksior[i]] - perm[i])*(k-i) < (perm[k]-perm[i])*(maksior[i]-i)) {
	  ok = false;
	  break;
	}
      }
    }
    if (ok) {
      printout(n);
      return;
    }
  } while(next_permutation(perm, perm+n));
  
  
  REP(p,100) {
  REP(i,n) perm[i] = rand()%1000;
  sort(perm, perm+n);
  
  do {
    bool ok = true;
    REP(i,n-1) {
      FOR(k,i+1,maksior[i]-1)
	if ( (perm[maksior[i]] - perm[i])*(k-i) <= (perm[k]-perm[i])*(maksior[i]-i)) {
	  ok = false;
	  break;
	}

      FOR(k,maksior[i]+1,n-1) {
	if ( (perm[maksior[i]] - perm[i])*(k-i) < (perm[k]-perm[i])*(maksior[i]-i)) {
	  ok = false;
	  break;
	}
      }
    }
    if (ok) {
      printout(n);
      return;
    }
  } while(next_permutation(perm, perm+n));
  }

  REP(i,n+1) perm[i] = 0;
  if (false)
  do {
    int skok = 0;
    while (perm[skok] == 9) perm[skok++] = 0;
    ++perm[skok];

    bool ok = true;
    REP(i,n-1) {
      FOR(k,i+1,maksior[i]-1)
	if ( (perm[maksior[i]] - perm[i])*(k-i) <= (perm[k]-perm[i])*(maksior[i]-i)) {
	  ok = false;
	  break;
	}

      FOR(k,maksior[i]+1,n-1) {
	if ( (perm[maksior[i]] - perm[i])*(k-i) < (perm[k]-perm[i])*(maksior[i]-i)) {
	  ok = false;
	  break;
	}
      }
    }
    if (ok) {
      printout(n);
      return;
    }
  } while(perm[n] == 0);

  printf("Impossible\n");
}

int main() {
  int t;
  scanf("%d", &t);
  REP(i,t) {
    printf("Case #%d: ", i+1);
    testcase();
  }
}
