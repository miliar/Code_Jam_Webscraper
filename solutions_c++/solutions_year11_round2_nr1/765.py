#include <iostream>
#include <vector>
#include <set>

using namespace std;
namespace {
void PrintOutput(size_t iter, const vector<double> result) {
  cout << "Case #" << iter+1 << ":" << endl;
  for (size_t i = 0; i < result.size(); ++i) {
    cout << result[i] << endl;
  }
}
} //namespace

int main() {
  cout.precision(10);
  size_t T;
  cin >> T;

  for (size_t t = 0; t < T; ++t) {
    size_t N;
    cin >> N;

    vector<double> wp;
    vector<set<size_t> > opponents;
    vector<vector<double> > wp_without_table;
    for (size_t n = 0; n < N; ++n) {
      size_t trial = 0;
      size_t win = 0;
      set<size_t> opponent;
      vector<size_t> win_lose(N, 2);

      for (size_t opp = 0; opp < N; ++opp) {
        char tmp;
        cin >> tmp;
        if (tmp == '0'){
          ++trial;
          opponent.insert(opp);
          win_lose[opp] = 0;
        } else if(tmp == '1') {
          ++trial;
          ++win;
          opponent.insert(opp);
          win_lose[opp] = 1;
        }
      }

      wp.push_back(win/(double)trial);
      opponents.push_back(opponent);

      vector<double> wp_without;
      for (size_t i = 0; i < N; ++i) {
        if (win_lose[i] == 0)
          wp_without.push_back(win / (double)(trial - 1));
        else if(win_lose[i] == 1)
          wp_without.push_back((win-1) / (double)(trial - 1));
        else
          wp_without.push_back(win / (double)(trial));
      }
      wp_without_table.push_back(wp_without);
    }

    vector<double> owp;
    for (size_t n = 0; n < N; ++n) {
      size_t set_size = 0;
      double total = 0.0;
      for (set<size_t>::iterator it = opponents[n].begin();
           it != opponents[n].end();
           ++it) {
        total += wp_without_table[*it][n];
        ++set_size;
      }
      owp.push_back(total / set_size);
    }

    vector<double> oowp;
    for (size_t n = 0; n < N; ++n) {
      size_t set_size = 0;
      double total = 0.0;
      for (set<size_t>::iterator it = opponents[n].begin();
           it != opponents[n].end();
           ++it) {
        total += owp[*it];
        ++set_size;
      }
      oowp.push_back(total / set_size);
    }

    vector<double> rpi;
    for (size_t n = 0; n < N; ++n) {
      rpi.push_back(0.25 * wp[n] + 0.50 * owp[n] + 0.25 * oowp[n]);
    }

    PrintOutput(t, rpi);
  }

  return 0;
}
