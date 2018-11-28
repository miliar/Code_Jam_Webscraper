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
int ns[1000];
bool processed[1000];

void input() {
  int inputs[1000];
  int sorted[1000];
  typedef map<int, int> IIMAP;
  IIMAP mapping;

  cin>>N;
  REP(i, 0, N) {
    cin>>inputs[i];
    sorted[i] = inputs[i];
  }

  sort(sorted, sorted+N);
  REP(i, 0, N) {
    mapping[sorted[i]] = i;
  }
  REP(i, 0, N) {
    ns[i] = mapping[inputs[i]];
  }
}

void solve(int caseNum) {
  input();
  // REP(i, 0, N) printf("%3d", ns[i]); printf("\n");

  REP(i, 0, N) {
    processed[i] = false;
  }

  double ans = 0.0;

  REP(i, 0, N) {
    if (ns[i]==i) {
      processed[i] = true;
    }
    if (processed[i]) continue;
    int cur = i;
    int cnt = 0;
    do {
      processed[cur] = true;
      ++cnt;
      cur = ns[cur];
    } while(cur!=i);
    ans += cnt;
  }

  printf("Case #%i: %.8lf", caseNum, ans);
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
}

