#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

#define min(a,b) (a < b ? a : b)

ifstream in("tree.in");
ofstream out("tree.out");

int m,v;
vector<int> val;
vector< vector<int> > nummoves; 
// nummoves[x][b] = whether you can make node x have value b
// value is -1 if impossible, n if n is the minimum needed
vector<bool> gate,changeable;

int main() {
  int n;
  in >> n;

  for (int casenum = 1; casenum <= n; casenum++) {
    in >> m >> v;
    val.clear();
    nummoves.clear();
    gate.clear();
    changeable.clear();
    val.resize(m+1,-1);
    nummoves.resize(m+1, vector<int>(2,-1));
    gate.resize(m+1,-1);
    changeable.resize(m+1,-1);
    for (int i=1; i<=(m-1)/2; i++) {
      int a,b;
      in >> a >> b;
      gate[i] = bool(a);
      changeable[i] = bool(b);
    }
    for (int i=(m+1)/2; i<=m; i++) {
      in >> val[i];
      nummoves[i][val[i]] = 0;
    }
    int z;
    for (int i=(m-1)/2; i>=1; i--) {
      if (gate[i] == 0 || changeable[i]) { //OR
	z = 0;
	if (gate[i] != 0) {
	  z++;
	}

	// to get a value of 1
	if (nummoves[i*2][1] != -1) {
	  if (nummoves[i][1] == -1 || nummoves[i*2][1] + z < nummoves[i][1]) {
	    nummoves[i][1] = nummoves[i*2][1] + z;
	  }
	}
	if (nummoves[i*2+1][1] != -1) {
	  if (nummoves[i][1] == -1 || nummoves[i*2+1][1] + z < nummoves[i][1]) {
	    nummoves[i][1] = nummoves[i*2+1][1] + z;
	  }
	}
	
	// to get value of 0
	if (nummoves[i*2][0] != -1 && nummoves[i*2+1][0] != -1) {
	  if (nummoves[i][0] == -1 || nummoves[i*2][0] + nummoves[i*2+1][0] + z < nummoves[i][0]) {
	    nummoves[i][0] = nummoves[i*2][0] + nummoves[i*2+1][0] + z;
	  }
	}

      }
      if (gate[i] == 1 || changeable[i]){ //AND
	z = 0;
	if (gate[i] != 1) {
	  z++;
	}

	// to get a value of 0
	if (nummoves[i*2][0] != -1) {
	  if (nummoves[i][0] == -1 || nummoves[i*2][0] + z < nummoves[i][0]) {
	    nummoves[i][0] = nummoves[i*2][0] + z;
	  }
	}
	if (nummoves[i*2+1][0] != -1) {
	  if (nummoves[i][0] == -1 || nummoves[i*2+1][0] + z < nummoves[i][0]) {
	    nummoves[i][0] = nummoves[i*2+1][0] + z;
	  }
	}
	
	// to get value of 1
	if (nummoves[i*2][1] != -1 && nummoves[i*2+1][1] != -1) {
	  if (nummoves[i][1] == -1 || nummoves[i*2][1] + nummoves[i*2+1][1] + z < nummoves[i][1]) {
	    nummoves[i][1] = nummoves[i*2][1] + nummoves[i*2+1][1] + z;
	  }
	}	
      }
    }
    out << "Case #" << casenum << ": ";
    if (nummoves[1][v] == -1) {
      out << "IMPOSSIBLE" << endl;
    } else {
      out << nummoves[1][v] << endl;
    }
    /*
    for (int i=1; i<=m; i++) {
      out << i << " " << nummoves[i][0] << " " << nummoves[i][1] << endl;
    }
    */
  }
  return 0;
}
