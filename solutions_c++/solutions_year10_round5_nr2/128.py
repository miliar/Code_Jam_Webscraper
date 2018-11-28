#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "B"

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef long long ll;
typedef pair<int, int> pii;

int gcd(int a, int b) {
  if (!b) {
    return a;
  }
  return gcd(b, a % b);
}

const ll INF = ll(1000000000) * 1000000000;
const int MAXN = 10000;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    ll L;
    int bcount;
    cin >> L >> bcount;
    vector<int> boards(bcount);
    for (int i = 0; i < bcount; ++i) {
      cin >> boards[i];
    }
    int g = 0;
    for (int i = 0; i < boards.size(); ++i) {
      g = gcd(g, boards[i]);
    }
    cout << "Case #" << test_index + 1 << ": ";
    cerr << "Case #" << test_index + 1 << ": ";
    if (L % g) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }
    sort(boards.begin(), boards.end());
    int largeBoard = boards.back();
    //boards.pop_back();
    vector< vector<ll> > minBoards(2, vector<ll>(MAXN, INF));
    for (int length = 0; length < MAXN; length += boards[0]) {
      minBoards[0][length] = length / boards[0];
    }
    int cur = 0;
    int nxt = 1;
    for (int board_index = 1; board_index < boards.size(); ++board_index) {
      for (int length = 0; length < MAXN; ++length) {
        minBoards[nxt][length] = minBoards[cur][length];
        if (length >= boards[board_index]) {
          minBoards[nxt][length] = min(minBoards[nxt][length], minBoards[nxt][length - boards[board_index]] + 1);
        }
      }
      cur = 1 - cur;
      nxt = 1 - nxt;
    }
    ll largeBoardCount = (L - (MAXN - 1) + (largeBoard - 1)) / largeBoard;
    int lengthLeft = L - largeBoardCount * largeBoard;
    ll result = largeBoardCount + minBoards[cur][lengthLeft];
    cout << result << endl;
  }
  return 0;
}
