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


int Line[1024][24];

int count(string S) {
  memset(Line, 0, sizeof(Line));
  for(int i = 0; i < 1000; i++) Line[i][0] = 1;
  string W("welcome to code jam");

  for(int end = 1; end <= W.len; end++) {
    for(int pos = S.len - 1; pos >= 0; pos--) {
      Line[pos][end] = Line[pos+1][end];
      if(S[pos] == W[W.len - end]) Line[pos][end] += Line[pos+1][end-1];
      Line[pos][end] %= 10000;
//    cerr << S[pos] << " " << W[W.len - end] << " " << pos << " " << end << " " << Line[pos][end] << endl;
    }
  }
  return Line[0][W.len];
}


int main() {
  cout.precision(16);
  int N;
  cin >> N;
  string S;
  getline(cin, S);
  for(int i = 1; i <= N; i++) {
    string S;
    getline(cin, S);
    int c = count(S);
    cout << "Case #" << i << ": " << (c/1000)%10 << (c/100)%10 << (c/10)%10 << c%10 << endl;
  }
}
