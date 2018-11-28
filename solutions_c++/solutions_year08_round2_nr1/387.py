#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <iterator>
#include <algorithm>

using namespace std;

typedef long long int LL;
typedef unsigned long long int ULL;
typedef unsigned int uint;

int main() {
  LL N;
  cin >> N;

  for (int caseNumber = 1; caseNumber <= N; ++caseNumber) {
    LL A, B, C, D, M, n, X, Y;
    cin >> n >> A >> B >> C >> D >> X >> Y >> M;

    vector< vector<LL> > pairs(3, vector<LL>(3, 0)), individuals(3, vector<LL>(3, 0));

    individuals[X % 3][Y % 3]++;
    LL cnt = 0;
    for (int i = 1; i < n; ++i) {
      X = ((LL)A * X + B) % M;
      Y = ((LL)C * Y + D) % M;

      cnt += pairs[(3 - (X % 3)) % 3][(3 - (Y % 3)) % 3];
      for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
          pairs[(i + X) % 3][(j + Y) % 3] += individuals[i][j];
        }
      }

      individuals[X % 3][Y % 3]++;
    }

    cout << "Case #" << caseNumber << ": " << cnt << endl;
  }
}
