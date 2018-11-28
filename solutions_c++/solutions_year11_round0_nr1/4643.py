#include <iostream>
#include <vector>
using namespace std;

typedef pair<int, int> PI;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int N;
    cin >> N;
    vector<PI> O(0), B(0);
    for (int i = 0; i < N; ++i) {
      char bot;
      PI p(i, 0);
      cin >> bot >> p.second;
      if (bot == 'O') O.push_back(p);
      else B.push_back(p);
    }
    int step, actO, actB, iO, iB, sec;
    actO = actB = 1;
    step = sec = iO = iB = 0;
    while (step < N) {
      int button = 0;
      if (O.size() > iO) {
        if (O[iO].second > actO) ++actO;
        else if (O[iO].second < actO) --actO;
        else if (O[iO].first == step) {
          button = 1;
          ++iO;
        }
      }
      if (B.size() > iB) {
        if (B[iB].second > actB) ++actB;
        else if (B[iB].second < actB) --actB;
        else if (B[iB].first == step) {
          button = 1;
          ++iB;
        }
      }
      step += button;
      ++sec;
    }
    cout << "Case #" << cas << ": " << sec << endl;
  }
}
