#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int n;
pair<int, int> seq[100];


int T[2];
int P[2];


int solve() {
  cin >> n;
  for (int i = 0; i < n; ++i) {
    char ch;
    cin >> ch;
    if (ch == 'O')
      seq[i].first = 0;
    else
      seq[i].first = 1;

    cin >> seq[i].second;
  }

  P[0] = P[1] = 1;
  T[0] = T[1] = 0;

  int total_time = 0;

  for (int i = 0; i < n; ++i) {
    int who = seq[i].first;
    int other = who ^ 1;

    int where = seq[i].second;

    int delta = abs(where - P[who]);
    int run = min(T[who], delta);
    delta -= run;
    T[who] = 0;
    delta += 1;
    if (delta > 0) {
      total_time += delta;
      T[other] += delta;
    }

    P[who] = where;
//    cout << "delta = " << delta << endl;
//    cout << "(" << T[0] << ", " << P[0] << ") ... (" << T[1] << ", " << P[1] << ")\n";
  }

  return total_time;
}

int main() {
  int tests;
  cin >> tests;

  for (int t = 1; t <= tests; ++t) {
    int ans = solve();
    cout << "Case #" << t << ": " << ans << endl;
  }
}

