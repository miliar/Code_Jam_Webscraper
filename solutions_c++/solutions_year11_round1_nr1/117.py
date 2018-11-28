#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <algorithm>
#include <cassert>
#include <cmath>

using namespace std;

typedef long long int int64;
typedef vector<int> VI;
#define REP(i,a,b) for (int i=int(a); i<int(b); ++i)
void unittest();

int64 N, PD, PG;


int64 gcd(int64 a, int64 b) {
  int64 m = max(a, b);
  int64 n = min(a, b);
  if (n==0) return m;
  return gcd(n, m%n);
}

bool check() {
  cin>>N>>PD>>PG;
  if (PD!=0) {
    int64 r = gcd(PD, 100);
    r = 100/r;
    if (r>N)
      return false;
  }
  if ( (PG==0||PG==100) && (PD!=PG))
    return false;
  return true;
}

void solve(int caseNum) {
  printf("Case #%i: %s", caseNum, check()?"Possible":"Broken");
  printf("\n");
}

int main() {
  unittest();

  int caseCount;
  cin>>caseCount;
  REP(i, 1, caseCount+1)
    solve(i);

  return 0;
}

void unittest() {
  assert(true);
  assert(gcd(6, 9)==3);
  assert(gcd(8, 10)==2);
  assert(gcd(100000000000000LL, 10)==10);
}

