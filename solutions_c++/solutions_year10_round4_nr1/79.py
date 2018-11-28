#include <iostream>
#include <string>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int casenum = 1; casenum <= t; ++casenum) {
    int k;
    cin >> k;
    string tmp;
    getline(cin, tmp);

    vector<string> rows;
    for (int r = 0; r < k+k-1; ++r) {
      string row;
      getline(cin, row);
      for (int i = 0; i < abs(k-(r+1)); ++i) {
	row[i] = '.';
      }
      while (row.size() < k+k-1) {
	row.push_back('.');
      }
      rows.push_back(row);
    }

    vector<bool> rpoints(k+k-1, true);
    for (int r = 0; r < k+k-1; ++r) {
      for (int i = 0; i < k+k-1; ++i) {
	if (rpoints[i]) {

	  int m = i;
	  int n = i;
	  while (m >= 0 && n < k+k-1 && rows.at(r).at(m) != '.' && rows.at(r).at(n) != '.') {
	    if (rows.at(r).at(m) == rows.at(r).at(n)) {
	      n ++;
	      m --;
	    } else {
	      rpoints[i] = false;
	      break;
	    }
	  }

	}
      }
    }

    for (int i = 0; i < rpoints.size(); ++i) {
      cerr << rpoints[i];
    }
    cerr << endl;

    vector<bool> cpoints(k+k-1, true);
    for (int r = 0; r < k+k-1; ++r) {
      for (int i = 0; i < k+k-1; ++i) {
	if (cpoints[i]) {

	  int m = i;
	  int n = i;
	  while (m >= 0 && n < k+k-1 && rows.at(m).at(r) != '.' && rows.at(n).at(r) != '.') {
	    if (rows.at(m).at(r) == rows.at(n).at(r)) {
	      n ++;
	      m --;
	    } else {
	      cpoints[i] = false;
	      break;
	    }
	  }

	}
      }
    }

    for (int i = 0; i < cpoints.size(); ++i) {
      cerr << cpoints[i];
    }
    cerr << endl;

    // rpoints and cpoints
    // closest to k-1

    int maxdist;
    for (int r = 0; r < k; ++r) {
      if (rpoints[k-1-r] || rpoints[k-1+r]) {
	maxdist = r;
	break;
      }
    }

    int maxdistc;
    for (int c = 0; c < k; ++c) {
      if (cpoints[k-1-c] || cpoints[k-1+c]) {
	maxdistc = c;
	break;
      }
    }
    
    // or mindist heh

    // cost is... each step adds 2*k+1

    int tot = maxdist + maxdistc;
    cerr << "maxdist " << tot << endl;
    int tmpk = k;
    int cost = 0;
    for (int i = 0; i < tot; ++i) {
      cost += 2*tmpk + 1;
      tmpk += 1;
    }




    cout << "Case #" << casenum << ": ";
    cout << cost;
    cout << endl;
  }
}
