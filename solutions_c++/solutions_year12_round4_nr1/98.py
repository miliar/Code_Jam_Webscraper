#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>

#define InputVector(v, Type) { v.clear(); Type t; int _n; cin >> _n; v.reserve(_n); while (--_n >= 0) { cin >> t; v.push_back(t); } }

using namespace std;

//===================================================
class Solver {
  bool debug;
  
  int nVines, target;
  vector<int> vineDists, vineLengths;
  vector<int> deepestVinePos;
  vector<bool> dVPChanged;

public:

  Solver():debug(false) {
    cin >> nVines;
    vineDists.resize(nVines);
    vineLengths.resize(nVines);
    for (int i = 0; i < nVines; ++i)
      cin >> vineDists[i] >> vineLengths[i];
    cin >> target;
  }

  void go() {
    deepestVinePos.resize(nVines);
    dVPChanged.resize(nVines);

    int i, j;
    for (i = 0; i < nVines; ++i) {
      dVPChanged[i] = true;
      deepestVinePos[i] = 0;
    }

    deepestVinePos[0] = vineDists[0];

    bool stable, good = false;
    do {
      stable = true;

      vector<bool> oldDVPChanged = dVPChanged;
      for (i = 0; i < nVines; ++i) dVPChanged[i] = false;

      for (i = 0; i < nVines; ++i)
	if (oldDVPChanged[i]) {
	  stable = false;

	  if (vineDists[i]+deepestVinePos[i] >= target) {
	    good = true;
	    break;
	  }

	  for (j = 0; j < nVines; ++j) 
	    if (j != i && abs(vineDists[i]-vineDists[j]) <= deepestVinePos[i]) {
	      int newPos = min(abs(vineDists[i]-vineDists[j]), vineLengths[j]);
	      if (newPos > deepestVinePos[j]) {	
		deepestVinePos[j] = newPos;
		dVPChanged[j] = true;
	      }
	    }
	}
    } while (!good && !stable);
    
    if (good) cout << " YES"; else cout << " NO";
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
