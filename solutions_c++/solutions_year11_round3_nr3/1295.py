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
    bool is_ok = false;
    int total = 0;

    int N = 0; int L = 0; int H = 0;
    cin >> N; cin >> L; cin >> H;
    getline(cin, line);
    vector <int> seqv;
    for (i = 0; i < N; i++) {
      int seq;
      cin >> seq;
      seqv.push_back(seq);
    }
    getline(cin, line);
    sort(seqv.begin(), seqv.end());

    for (i = L; i <= H; i++) {
      for (j = 0; j < seqv.size(); j++) {
	if (seqv[j] > i) {
	  if (0 == seqv[j] % i) {
	  }
	  else { break; }
	}
	else {
	  if (0 == i % seqv[j]) {
	  }
	  else { break; }
	}
      }
      if (j == seqv.size()) { is_ok = true; total = i;  break; }
    }
    
    cout << "Case #" << sn + 1 << ": ";
    if((is_ok) && (total > 0)) {
      cout << total << endl;
    }
    else {
      cout << "NO" << endl;
    }
  }
}
// END CUT HERE


