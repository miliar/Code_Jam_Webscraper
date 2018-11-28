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
#include <list>
#include <deque>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <bitset>
#include <queue>
using namespace std;

//conversion
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long ll;

//container util
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)

//constant
const double EPS = 1e-10;
const int MAXI = 1234567890;

//debug
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;



void printList(vector<int>& v) {
  for (size_t i = 0; i < v.size(); i++) {
	cout << v[i] << " ";
  }
  cout << endl;
}

void printMatrix(vector< vector<int> >& v) {
  for (size_t i = 0; i < v.size(); i++) {
	printList(v[i]);
  }
  cout << endl;
}

int solve(int S, int P, vector<int>& ps) {
  sort(RALL(ps));
  int ans = 0;
  for (int i = 0; i < SZ(ps); i++) {
    int t = ps[i] / 3;
    if (ps[i] % 3 != 0) t++;
    if (t >= P) {
      ans++;
      continue;
    }
    if (S == 0) continue;
    if (ps[i] < 2 || ps[i] > 28) continue;
    if (t == 10) continue;
    if (ps[i] % 3 == 1) continue;

    if (t + 1 >= P) {
      S--;
      ans++;
      continue;
    }
  }
  return ans;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, S, P;
    cin >> N >> S >> P;
    vector<int> ps(N, 0);
    for (int j = 0; j < N; j++) {
      cin >> ps[j];
    }
    int ans = solve(S, P, ps);
    cout << "Case #" << i + 1 << ": " << ans << endl;
  }
  return 0;
}
