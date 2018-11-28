#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <cmath>
using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<VI> VVI;
typedef long long LL;
typedef stringstream SS;


#define pb(x) push_back(x)
#define ins(x) insert(x)
#define sz size()
#define len length()

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(int i=(a),_d=((a)<(b))?1:-1; _d*i<=_d*(b); i+=_d)
#define FOREACH(it,s) for (typeof((s).begin()) it = (s).begin(); it != (s).end(); ++it)
#define SORT(x) (sort((x).begin(),(x).end()))
#define UNIQ(x) ((x).erase(unique((x).begin(),(x).end()),(x).end()))

#define INF 2147450751



string next(string S) {
  int pos = S.len-1;
  for(; pos >= 1 && S[pos] <= S[pos-1]; pos--);
  if(pos == 0) {S = "0" + S; pos = 1;}
  int min = pos;
  for(int i = pos; i < S.len; i++) {
//    cerr << i << " " << S[i] << " " << S[min] << " " << min << endl;
    if(S[i] > S[pos-1] && S[i] < S[min]) min = i;
  }
//  cerr << pos << " " << min << " " << S[pos] << " " << S[pos-1] << " " << S[min] << " " << S << " ";
  char c = S[pos-1];
  S[pos - 1] = S[min];
  S[min] = c;
//  cerr << " " << S << endl;
  sort(S.begin() + pos, S.end());
//  cerr << S << endl;
  return S;
}

int main() {
  cout.precision(16);
  int T; cin >> T;
  for(int i = 1; i <= T; i++) {
    string S;
    cin >> S;    
    cout << "Case #" << i << ": " << next(S) << endl;

  }
}
