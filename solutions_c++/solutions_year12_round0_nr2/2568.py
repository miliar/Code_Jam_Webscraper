#include <iostream>
#include <fstream>
#include <cassert>
using namespace std;

int main() {
  ifstream cin("data.txt");
  int N, T, S, p, score, maxScore;
  cin >> N;
  for (int i = 0; i < N; i++) {
    int count = 0, excessS = 0, needS = 0;
    cin >> T >> S >> p;
    for (int j = 0; j < T; j++) {
      cin >> score;
      maxScore = score / 3 + score % 3;
      if (score % 3 == 0) {
        bool needSUsed = false;
        if (maxScore >= p) {
          count++;
        } else if ((maxScore >= 1) && (maxScore + 1 >= p)) {
          count++;
          needS++;
          needSUsed = true;
        }
        if (maxScore >= 1 && !needSUsed) {
          excessS++;
        }
      } else if (score % 3 == 1) {
        // not surprise
        if (maxScore >= p) {
          count++;
        }
        if (maxScore >= 2) {
          excessS++; 
        }
      } else {
        if (maxScore > p) {
          count++;
          excessS++;
        } else if (maxScore == p) {
          count++;
          needS++;
        } else {
          excessS++;
        }
      }
    }
    
    //cout << "Need S : " << needS << "   Excess S: " << excessS << "   S: " << S << endl;
    assert(needS + excessS >= S);
    if (needS > S) {
      count -= (needS - S);
    }
    cout << "Case #" << (i+1) << ": " << count << endl;
  }

}