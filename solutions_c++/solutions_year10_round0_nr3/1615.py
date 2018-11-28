#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

// #define DBG(x) cout << #x << " = " << x << endl
#define DBG(x)
#define REP(i, n) for (int (i) = 0; (i) < (n); ++(i))
#define FOR(i, a, b) for (int (i) = (a); (i) <= (b); ++(i))
#define SIZE(a) (int)a.size()

using namespace std;

long long doit(int R, int k, const vector<int>& g) {
  int N = SIZE(g);
  long long total_people = 0;
  REP(i, N) total_people += g[i];
  if (total_people <= k)
    return total_people * R;
  vector<int> last_seen(N, -1);
  vector<long long> moves(1, 0);
  int pos = 0;
  int mv;
  long long profit = 0;
  for (mv = 1; mv <= R; ++mv) {
    if (last_seen[pos] == -1) {
      last_seen[pos] = mv;
      long long this_move = 0;
      for(;;) {
	int gr = g[pos];
	if (this_move + gr > k) {
	  moves.push_back(moves[mv - 1] + this_move);
	  break;
	} else {
	  this_move += gr;
	  ++pos;
	  pos %= N;
	}
      }
      profit = moves[mv];
      DBG(mv);
      DBG(this_move);
      DBG(pos);
    } else {
      int cycle_length = mv - last_seen[pos];
      long long cycle_cost = moves[mv - 1] - moves[last_seen[pos] - 1];
      if (R - mv > 1000) {
	int cycles = (R - 10 - mv) / cycle_length;
	profit = moves[mv - 1] + cycle_cost * cycles;
	mv += cycle_length * cycles;
      }
      DBG("cycle");
      break;
    }
  }
  for (; mv <= R; ++mv) {
    long long this_move = 0;
    for(;;) {
      int gr = g[pos];
      if (this_move + gr > k) break;
      this_move += gr;
      profit += gr;
      ++pos;
      pos %= N;
      DBG(mv); DBG(this_move); DBG(pos);
    }
  }
  return profit;
}

int main() {
  freopen("test.in", "r", stdin);
  freopen("test.out", "w", stdout);
  int tests;
  cin >> tests;
  for (size_t z = 1; z <= tests; ++z) {
    int R, k, N;
    cin >> R >> k >> N;
    vector<int> g(N);
    REP(i, N) {
      cin >> g[i];
    }
    cout << "Case #" << z << ": " << doit(R, k, g) << endl;
  }
  fclose(stdin);
  fclose(stdout);
  return 0;
}
