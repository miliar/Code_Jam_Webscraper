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

int N;
int C[1000];

void solve(int caseNum) {
  cin>>N;
  int mask = 0;
  int total = 0;
  REP(i, 0, N) {
    cin>>C[i];
    mask ^= C[i];
    total += C[i];
  }

  if (mask) {
    printf("Case #%i: NO\n", caseNum);
    return;
  }

  sort(C, C+N);

  printf("Case #%i: %d\n", caseNum, total-C[0]);
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
}

