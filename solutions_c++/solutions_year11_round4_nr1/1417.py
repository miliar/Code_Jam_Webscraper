#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

typedef pair<double, int> PDI;
typedef pair<int, int> PII;

int main() {
  cout << fixed << setprecision(8);
  int T; cin >> T;
  for (int cNum = 1; cNum <= T; ++cNum) {
    int X, S, R, t, N; cin >> X >> S >> R >> t >> N;

    vector<PII> segs; int curPos = 0;
    double travelT = 0;
    for (int i = 0; i < N; ++i) {
      int B, E, w; cin >> B >> E >> w;
      segs.push_back(PII(S, B - curPos));
      segs.push_back(PII(S + w, E - B));

      travelT += double(B - curPos) / S;
      travelT += double(E - B) / (S + w);

      curPos = E;
      }
    segs.push_back(PII(S, X - curPos));
    travelT += double(X - curPos) / S;

    sort(segs.begin(), segs.end());
    double runTime = t, dv = R-S;
    for (vector<PII>::iterator i = segs.begin(); (i != segs.end()) && (runTime > 0); ++i) {
      double runD = min(runTime * (i->first + dv), double(i->second));
      double runT = min(runTime, runD / (i->first + dv));

      runTime -= runT;
      travelT -= runD/i->first - runD/(i->first + dv);
      }

    cout << "Case #" << cNum << ": " << travelT << '\n';
    }
  }
