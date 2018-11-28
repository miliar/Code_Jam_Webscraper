#include <iostream>
#include <string>
#include <algorithm>
#include <assert.h>

using namespace std;

void tcase(int casen) {
  int N, S, p;
  cin >> N >> S >> p;
  int score;
  cerr << "CASE " << casen << endl;
  cerr << N << " googlers, " << S << " surprising, " << p << " min score" << endl;
  int minNonSurp = max(3 * p - 2, 0);
  int minSurp = max(minNonSurp - 2, 2);
  cerr << "minNonSurp: " << minNonSurp << ", minSurp: " << minSurp << endl;
  int nonSurpCount = 0;
  int surpCount = 0;
  for (int i = 0; i < N; ++i) {
    cin >> score;
    cerr << score << " ";
    if (score >= minNonSurp) {
      ++nonSurpCount;
    }
    else if (score >= minSurp) {
      ++surpCount;
    }
  }
  cerr << endl;
  cerr << nonSurpCount << " non surprisingly over p and " << surpCount << " surprisingly over p" << endl;
  int maxGooglers = nonSurpCount + min(S, surpCount);
  assert(maxGooglers <= N);
  if (p == 0) assert(surpCount == 0);
  cout << "Case #" << casen << ": " << maxGooglers << endl;
}

int main() {
  int T;
  cin >> T;
  cerr << T << " cases" << endl;
  for (int i = 0; i < T; ++i) tcase(i + 1);
}
