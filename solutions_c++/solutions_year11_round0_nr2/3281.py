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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

// MACROS
#define PRunsigned(X, K) cout << "Case #" << X << ": " << K << endl;
#define FOR(i, a, b) for(unsigned i=(a); i<(b);++i)
#define FOREACH(T, I, J) for (T::iterator I = J.begin(); I != J.end(); ++I)
#define FOREACH_B(T, I, S, E) for (I = S; I != E; ++I)
#define FOREACH_CONST(T, I, J) for (T::const_iterator I = J.begin(); I != J.end(); ++I)
#define PRunsigned_COLLECTION(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << " " << *it;
#define cti(C) (((int) C) - 65)
#define lor(A, B) (1 << cti(A) | 1 << cti(B))

#define PRINT_MAPPING(T, C) for(T::iterator it=C.begin(); it!=C.end(); ++it) cout << it->first << " : " << it->second << endl; cout << endl;

int flatten(string s) {
  int res = 0;
  FOR(i, 0, s.size()) { res = res | (1 << cti(s[i])); }
  return res;
}

void sta(int c, string s) {
  cout << "Case #" << (c) << ": [";
  if (s.size() > 0) cout << s[0];
  FOR(i, 1, s.size()) {
    cout << ", " << s[i];
  }
  cout << "]" << endl;
}

int main() {
  
  unsigned T; cin >> T;
  unsigned C, D, n;
  string s, in;
  
  FOR(i, 0, T) {
    
    map<int, char> comb = map<int, char>();
    vector<int> opp = vector<int>();
  
    cin >> C;
    FOR(Ci, 0, C) {
      cin >> s;
      comb[lor(s[0], s[1])] = s[2];
    }
    
    // opposition table
    cin >> D;
    FOR(Di, 0, D) {
      cin >> s;
      opp.push_back(lor(s[0], s[1]));
    }
    
    cin >> n >> in;
    string out;
    int checksum = 0;
    char rep;
    FOR(j, 0, n) {
      if (out.size() > 0) {
        // check for combination
        if (comb.count(lor(in[j], out[out.size()-1])) > 0) {
          // combine
          rep = comb[lor(in[j], out[out.size()-1])];
          out = out.erase(out.length() - 1);
          out += rep;
        } else {
          out += in[j];
        }
      } else {
        out += in[j];
      }
      
      checksum = flatten(out);
      // check for opp
      FOREACH(vector<int>, it, opp) {
        if ((checksum & *it) == *it) {
          out = "";
          break;
        }
      }
    }
    sta(i+1, out);
    
  }

}

