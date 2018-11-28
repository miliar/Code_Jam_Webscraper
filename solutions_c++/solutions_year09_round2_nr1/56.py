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



double proba(const char* tree, VS &F) {
  int pos, pos2;
  for(pos = 0; tree[pos] != '('; pos++); pos++;
  double p = atof(tree+pos);

//  cerr << tree << " " << p << endl;

  for(pos = 1; tree[pos] != ')' && (tree[pos] < 'a' || tree[pos] > 'z'); pos++);
  if(tree[pos] == ')') return p;
  for(pos2 = pos; tree[pos2] != ' '; pos2++);

  bool feature = false;
  for(int i = 0; i < F.sz; i++) if(F[i] == string(tree + pos, pos2 - pos)) feature = true;

  if(feature) return p * proba(tree + pos2, F);
  for(pos = pos2; tree[pos] != '('; pos++);
  pos++;
  for(int n = 1; n > 0; pos++) {
    if(tree[pos] == ')') n--;
    if(tree[pos] == '(') n++;
  }
  pos++;
  return p * proba(tree + pos, F);
}

int main() {
  cout.precision(16);
  int N;
  cin >> N;
  for(int i = 1; i <= N; i++) {
    int L;
    cin >> L;
    string line;
    getline(cin, line);
    SS S;
    for(int l = 0; l < L; l++) {
      getline(cin, line);
      S << line << " ";
    }
    int A;
    cin >> A;
    cout << "Case #" << i << ":" << endl;
    for(int a = 0; a < A; a++) {
      string f;
      int n;
      cin >> f >> n;
      VS F;
      REP(k, n) {
        cin >> f;
        F.pb(f);
      }
      cout << proba(S.str().c_str(), F) << endl;
    }




  }
}
