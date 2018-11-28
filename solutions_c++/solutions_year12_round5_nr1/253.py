// BEGIN CUT HERE
// headers begin
// END CUT HERE
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <utility>
#include <vector>
// BEGIN CUT HERE
// headers end
// END CUT HERE

using namespace std;

// BEGIN CUT HERE 
// helper functions begin
// END CUT HERE
// BEGIN CUT HERE 
// helper functions end
template<typename T> ostream& operator<<( ostream &os, const vector<T> &v ) { os << "{"; for ( typename vector<T>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " " << *vi; } os << " }"; return os; }
template<> ostream& operator<<( ostream &os, const vector<string> &v ) { os << "{"; for ( vector<string>::const_iterator vi=v.begin(); vi!=v.end(); ++vi ) { if ( vi != v.begin() ) os << ","; os << " \"" << *vi << "\""; } os << " }"; return os; }
template<typename T, typename U> ostream& operator<<( ostream &os, const pair<T, U> &P ) { return os << "(" << P.first << ", " << P.second << ")"; }
template<typename T> ostream& operator<<( ostream &os, const set<T> &S ) { return os << vector<T>( S.begin(), S.end() ); }
template<typename T, typename U> ostream& operator<<( ostream &os, const map<T, U> &M ) { for ( typename map<T, U>::const_iterator mi=M.begin(); mi!=M.end(); ++mi ) { os << mi->first << " => " << mi->second << endl; } return os; }
// END CUT HERE

int main() {
  cin.sync_with_stdio(0);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) {
    int n;
    cin >> n;
    
    vector<int> L(n), P(n);
    for (int i=0; i<n; ++i) {
      cin >> L[i];
    }
    for (int i=0; i<n; ++i) {
      cin >> P[i];
    }

    vector<pair<int, int> > order;
    for (int i=0; i<n; ++i) {
      order.push_back(make_pair(-P[i], i));
    }
    sort(order.begin(), order.end());

    printf("Case #%d:", tt);
    for (int i=0; i<n; ++i) {
      printf(" %d", order[i].second);
    }
    printf("\n");
  }
  return 0;
}
