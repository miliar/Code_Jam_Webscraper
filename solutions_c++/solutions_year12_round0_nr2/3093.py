#include <iostream>
#include <fstream>

#include <set>
#include <vector>

using namespace std;

class Score {
public:
  Score(int sum, int p) {
    a = -1;
    b = -1;
    c = -1;
    for (int max = p; max <= sum; ++max) {
      a = max;
      b = (sum - max)/2;
      c = sum - max - b;
      if (isValid() && !isSurprising()) return;
    }

    for (int max = p; max <= sum; ++max) {
      a = max;
      b = (sum - max)/2;
      c = sum - max - b;
      if (isValid() && isSurprising()) return;
    }
  }
  int a, b, c;
  bool isValid() {
    return a >= 0 && b >= 0 && c >= 0 && abs(a-b) < 3 && abs(a-c) < 3 && abs(b-c) < 3;
  }
  bool isSurprising() {
    int d1 = abs(a-b);
    int d2 = abs(a-c);
    int d3 = abs(b-c);
    return d1 == 2 || d2 == 2 || d3 == 2;
  }
};

int main() {
  ifstream input("B-large.in", ifstream::in);
  ofstream output("problem-b.out", ofstream::out);

  int caseCount;
  input >> caseCount;
  

  for (int caseId = 1; caseId <= caseCount; ++caseId) {
    int googlerCount, surprisingCount, p;

    input >> googlerCount >> surprisingCount >> p;

    vector<Score*> scores;

    for (int i = 0; i < googlerCount; ++i) {
      int sum;
      input >> sum;

      scores.push_back(new Score(sum, p));
    }
    
    int regularScores = 0, surprisingScores = 0;

    for (int i = 0; i < googlerCount; ++i) {
      auto score = scores[i];

      if (score->isValid()) {
        if (score->isSurprising()) {
          surprisingScores++;
        } else { 
          regularScores++;
        }
      }
    }

    output << "Case #" << caseId << ": " << regularScores + min(surprisingCount, surprisingScores) << endl;
  }

  return 0;
}