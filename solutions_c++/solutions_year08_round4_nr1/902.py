#include <iostream>
#include <vector>
#include <cctype>
using namespace std;

int main() {
  int ncases;
  cin >> ncases;
  for (int casenum=1; casenum<=ncases; casenum++) {
    int M, V;
    cin >> M >> V;

    int N = (M-1)/2;

    vector<bool> gates(N);
    vector<bool> values(M);
    vector<int> changeables;

    for (int i=0; i<N; i++) {
      int G, C;
      cin >> G >> C;
      gates[i] = (G == 1);
      if (C == 1) changeables.push_back(i);
    }

    for (int i=N; i<M; i++) {
      int I;
      cin >> I;
      values[i] = (I == 1);
    }

    int best = INT_MAX;

    int n = (int)changeables.size();
    for (int comb=0; comb<(1<<n); comb++) {
      vector<bool> ngates = gates;
      int dist = 0;
      for (int i=0; i<n; i++) {
	int j = changeables[i];
	ngates[j] = (comb & (1<<i)) > 0;
	if (ngates[j] != gates[j]) dist++;
      }

      for (int i=N-1; i>=0; i--) {
	bool v1 = values[2*(i+1)-1];
	bool v2 = values[2*(i+1)];
	if (ngates[i]) {
	  values[i] = v1 && v2;
	} else {
	  values[i] = v1 || v2;
	}
      }

      if (values[0] == (V==1)) best = min(best, dist);
    }

    cout << "Case #" << casenum << ": ";
    if (best == INT_MAX) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << best << endl;
    }
  }

  return 0;
}
