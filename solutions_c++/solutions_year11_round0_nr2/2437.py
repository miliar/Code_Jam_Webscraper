#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;

  string seq;

  char map[1000][1000]; // lawwwwwwlllllllllll
  bool opp[1000][1000];

  for (int i = 0; i < T; i++) {
    int C, D, N;
    cin >> C;

    for (int a = 0; a < 1000; a++) {
      for (int b = 0; b < 1000; b++) {
        map[a][b] = 0;
        opp[a][b] = false;
      }
    }

    for (int j = 0; j < C; j++) {
      cin >> seq;
      int first = (int)(seq[0]);
      int second = (int)(seq[1]);
      char last = seq[2];
      map[first][second] = last;
      map[second][first] = last;
    }

    cin >> D;
    for (int j = 0; j < D; j++) {
      cin >> seq;
      int first = (int)(seq[0]);
      int second = (int)(seq[1]);
      opp[first][second] = true;
      opp[second][first] = true;
    }

    cin >> N;
    cin >> seq;

    deque<char> cc;
    for (int j = 0; j < N; j++) {
      if (cc.empty()) {
        cc.push_back(seq[j]);
        continue;
      }

      int first = (int)(seq[j]);
      int second = (int)(cc.back());

      if (map[first][second] != 0) {
        cc.pop_back();
        cc.push_back(map[first][second]);
        continue;
      }

      bool fail = false;
      for (int k = 0; k < cc.size(); k++) {
        if (opp[first][(int)(cc[k])]) {
          fail = true;
          break;
        }
      }

      if (fail) {
        cc.clear();
        continue;
      }

      cc.push_back(seq[j]);
    }

    cout << "Case #" << (i + 1) << ": [";
    if (cc.empty()) {
      cout << "]" << endl;
      continue;
    }

    cout << cc[0];
    for (int j = 1; j < cc.size(); j++) {
      cout << ", " << cc[j];
    }

    cout << "]" << endl;
  }

  return 0;
}


