#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <string> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <cstring> 
#include <ctime> 
 
using namespace std; 

string combine (string s, string * sc, int C) {
  for (int c = 0; c < C; c++) {
    int l = s.length ();
    if (l < 2) break;
    int i = l-2;
    if ((s[i] == sc[c][0] && s[i+1] == sc[c][1]) || \
	(s[i] == sc[c][1] && s[i+1] == sc[c][0])) {
      s[i] = sc[c][2];
      s.erase (i+1, 1);
    }
  }
  return s;
}

string oppose (string s, string * sd, int D) {
  int i, j;
  for (int d = 0; d < D; d++) {
    int l = s.length ();
    if (l < 2) break;
    for (i = 0; i < l-1; i++) {
      j = l - 1;
      if ((s[i] == sd[d][0] && s[j] == sd[d][1]) || \
	  (s[i] == sd[d][1] && s[j] == sd[d][0])) {
	s = "";
	break;
      }
    }
  }
  return s;
}

int main () { 
  int t, T; 

  cin >> T; 
  for (t = 1; t <= T; t++) {
    int c, C;
    cin >> C;
    string sc[C];
    for (c = 0; c < C; c++) cin >> sc[c];
    int d, D;
    cin >> D;
    string sd[D];
    for (d = 0; d < D; d++) cin >> sd[d];
    int i, l;
    cin >> l;
    string str;
    cin >> str;

    string res;

    for (i = 0; i < l; i++) {
      res += str[i];
      string t = combine (res, sc, c);
      if (t == res)
	res = oppose (res, sd, d);
      else res = t;
    }

    cout << "Case #" << t << ": [";

    l = res.length ();
    if (l == 0) { cout << "]" << endl; continue; }
    for (i = 0; i < l - 1; i++)
      cout << res[i] << ", ";
    cout << res[l-1] << "]" << endl;
  }
  return 0; 
}
