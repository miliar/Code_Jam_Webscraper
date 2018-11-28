#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <set>
#include <map>
#include <iomanip>

#define fr(i,n) for(i=0;i<(int)(n);i++)
#define fit(a,b) for(typeof(b.begin()) a = b.begin(); a != b.end(); a++)
#define pb push_back
#define MP make_pair
#define F first
#define S second
#define SZ(u) ((int)u.size())
#define WT(x) cout << #x << ": " << x << endl

using namespace std;

typedef long long ll;
typedef pair<int,int> p2;
typedef vector<int> vi;
typedef long double ld;

int sortf(pair<p2, int> a, pair<p2, int> b) {
  if (a.F.F * b.F.S == a.F.S * b.F.F) {
    return a.S < b.S;
  }
  return a.F.F * b.F.S > a.F.S * b.F.F;
}

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    int N, i, l, p;
    cin >> N;
    vi ls;
    vector<pair<p2, int> > list;
    fr (i, N) {
      cin >> l;
      ls.pb(l);
    }

    fr (i, N) {
      cin >> p;
      list.pb(MP(MP(l, (100 - p)), i));
    }

    sort(list.begin(), list.end(), sortf);
    cout << "Case #" << cn << ":";

    fr (i, SZ(list)) cout << " " << list[i].S;
    cout << endl;
  }
  return 0;
}
