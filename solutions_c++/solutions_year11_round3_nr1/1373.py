#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

class Solution {
public:
  int solve(int a, int b) {
    int result = -1;
    return result;
  }
};

int stoi(string s) {
  int r;
  stringstream ss;
  ss << s;
  ss >> r;
  return r;
}

// BEGIN CUT HERE
int main() {
  //  Solution ___solution;
  int s_num = 0;
  int sn, i, j, k = 0;
  string line;
  //stringstream ss;
  //static const string empty_string;
  //ss << str; ss >> num;
  //ss.str(empty_string);ss.clear();
  cin >> s_num;
  getline(cin, line);
  for (sn = 0; sn < s_num; sn++) {
    bool is_ok = true;
    vector <string> seqv;
    int l_num = 0;
    int c_num = 0;
    cin >> l_num;
    cin >> c_num;
    getline(cin, line);
    for (i = 0; i < l_num; i++) {
      string seq;
      cin >> seq;
      seqv.push_back(seq);
      getline(cin, line);
      int bcount = count(seq.begin(), seq.end(), '#');
      if (0 != bcount % 2) {
	is_ok = false;
      }
    }

    if (!is_ok) {
    }
    else {
      for (i = 0; i < (seqv.size() - 1); i++) {
	int bcount = count(seqv[i].begin(), seqv[i].end(), '#');
	if (bcount == 0) { continue; }
	for (j = 0; j < (seqv[i].size() - 1); j++) {
	  
	  if ((seqv[i][j] == '#') && (seqv[i][j+1] == '#') && (seqv[i+1][j] == '#') && (seqv[i+1][j+1] == '#')) {
	    seqv[i][j] = '/'; seqv[i][j+1] = '\\'; seqv[i+1][j] = '\\'; seqv[i+1][j+1] = '/';
	    j++;
	  }
	}
	bcount = count(seqv[i].begin(), seqv[i].end(), '#');
	if (bcount != 0) { is_ok = false; break; }
      }
      int bcount = count(seqv[i].begin(), seqv[i].end(), '#');
      if (bcount != 0) { is_ok = false; }
    }

    cout << "Case #" << sn + 1 << ":" << endl;
    if((is_ok) && (seqv.size() > 0)) {
      for (i = 0; i < seqv.size(); i++) {
	cout << seqv[i] << endl;
      }
    }
    else {
      cout << "Impossible" << endl;
    }
  }
}
// END CUT HERE


