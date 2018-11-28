// BEGIN CUT HERE
#include "cout.h"
// END CUT HERE
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <cmath>
#include <queue>
#include <list>
#include <complex>
#include <iomanip>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long LL;
typedef complex<double> CMP;
#define Fill(a, b) memset((a), (b), sizeof(a))
#define REP(a, b) for (size_t (a) = 0; (a)<(size_t)(b); ++(a))
#define sz size()
#define Tr(c, i) for(typeof((c).begin()) i= (c).begin(); (i) != (c).end(); ++(i))
#define All(c) (c).begin(), (c).end()
#define Present(c, x) ((c).find(x) != (c).end()) // for Map or Set
#define CPresent(c, x) (find(All(c), x) != end()) // for vector

#include <assert.h>

long long ipow(int a, int b) {
  long long ret = 1LL;
  REP(i, b)
    ret *= a;
  return ret;
}

int prison[100002];

int mincost = INT_MAX;

int calccost(int p) {
  int ret = 0;
  int i = p+1;
  while(prison[i]) {
    i++;
    ret++;
  }
  i = p-1;
  while(prison[i]) {
    i--;
    ret++;
  }
  return ret;
}

void search(vector<int> &moves, int cost) {
  REP(i, moves.sz) {
    int tomove = moves[i];
    vector<int> nextmoves = moves;
    vector<int>::iterator end_it = remove(All(nextmoves), tomove);
    nextmoves.erase(end_it, nextmoves.end());
    int tc = calccost(tomove);
    prison[tomove] = 0;
    if (moves.sz <= 1) {
      if (cost + tc < mincost) {
        mincost = cost + tc;
      }
    } else {
      search(nextmoves, cost + tc);
    }
    prison[tomove] = 1;
  }
}

int main(void)
{
  int N;
  cin >> N;

  REP(i, N) {
    int P, Q;
    cin >> P >> Q;
    vector<int> prisons;
    int n;
    int ans = 0;
    Fill(prison, 0x0);
    for (int j = 1; j<= P; ++j) {
      prison[j] = 1;
    }
    REP(j, Q) {
      cin >> n;
      prisons.push_back(n);
    }
    mincost = INT_MAX;
    search(prisons, 0);
    ans = mincost;
    cout << "Case #" << (i+1) << ": " << ans << endl;


  }
  return 0;
}



