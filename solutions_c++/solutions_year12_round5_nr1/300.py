#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>

using namespace std;

//===================================================
class Solver {
  bool debug;
  
  int n;
  vector<int> t, p;
  
public:

  Solver():debug(false) {
    cin >> n;
    t.resize(n);
    p.resize(n);

    int i;
    for (i = 0; i < n; ++i) cin >> t[i];
    for (i = 0; i < n; ++i) { cin >> p[i]; p[i] = 100 - p[i]; }
  }

  double expectedValue(vector<int> index) {
    double E = 0.0;
    int i, j;
    for (i = 1; i < n; ++i) {
      double term = 0.0;
      for (j = 0; j < i; ++j)
	term += (100.0*t[index[j]])/p[index[j]];
      E += (100.0/p[index[i]] - 1.0)*term;
    }
      
    return E;
  }

  void go() {
    double E, newE;
    vector<int> index(n), newIndex(n);
    int i, j, k;
    for (i = 0; i < n; ++i) { index[i] = i; newIndex[i] = i; }
    E = expectedValue(index);

    bool stable = false;
    while (!stable) {
      stable = true;

      for (i = 0; i < n; ++i)
	for (j = i; ++j < n; ) {
	  swap(newIndex[i], newIndex[j]);
	  newE = expectedValue(newIndex);

	  if (newE < E || (newE==E && newIndex < index)) {
	    E = newE;
	    swap(index[i], index[j]);
	    stable = false;
	  } else
	    swap(newIndex[i], newIndex[j]);
	}
    }

    for (i = 0; i < n; ++i) cout << " " << index[i];
  }

};
//===================================================

int main(void) {
  int iTest, nTests; cin >> nTests;

  for (iTest = 1; iTest <= nTests; ++iTest) {
    cerr << iTest << "/" << nTests << "\n";

    Solver solver;

    cout << "Case #" << iTest << ":";

    solver.go();

    cout << "\n";
  }

  return 0;
}
