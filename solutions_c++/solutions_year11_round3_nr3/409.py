#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <queue>
#include <cstring>
using namespace std;

#define loop(i,n) for (int i = 0; i < (int)(n); ++i)
#define Bounded(x,a,b) ((a) <= (x) && (x) <= (b))
#define db(x) #x << " = " << x
#define pdb(x) printf("#x = %d\n",x);
#define All(x) x.begin(),x.end()
#define sz(x) x.size()
typedef vector<int> Vi;
typedef pair<int,int> Pii;
typedef vector<Vi> Adj;
typedef vector<bool> Vb;

void solve(int casenum) {
  int N, L, H; cin >> N >> L >> H;
  Vi A(N); loop(i,N) cin >> A[i];

  printf("Case #%d: ", casenum);

  int found = -1;
  for (int i = L; i <= H && found == -1; ++i) {
    bool t = true;
    for (int j = 0; j < N && t; ++j)
      if (!(A[j]%i == 0 || i%A[j] == 0))
        t = false;
    if (t)
      found = i;
  }

  if (found == -1)
    printf("NO\n");
  else
    printf("%d\n", found);
}

int main() {
  int T; cin >> T;
  loop(i,T) solve(i+1);
  return 0;
}

