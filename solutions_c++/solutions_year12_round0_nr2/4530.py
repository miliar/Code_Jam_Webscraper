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


void solve(int caseNum) {
  int N, S, P;
  cin>>N>>S>>P;
  int ans=0;

  REP(i, 0, N) {
    int total, avg, mod;
    cin>>total;
    avg = total / 3;
    mod = total % 3;

    int base, potential;

    switch(mod) {
    case 0:
      base = avg;
      potential = avg + 1;
      break;
    case 1:
      base = potential = avg + 1;
      break;
    case 2:
      base = avg + 1;
      potential = avg + 2;
      break;
    }

    // Exception
    if (total==0) {
      base = potential = 0;
    }

    if (base>=P) {
      ++ans;
    } else if (S>0 && potential>=P) {
      ++ans;
      --S;
    }
  }

  printf("Case #%d: %d\n", caseNum, ans);
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
}

