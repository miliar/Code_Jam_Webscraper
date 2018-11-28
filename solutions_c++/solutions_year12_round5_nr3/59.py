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

int N;
ll M, F, P[200], S[200];

int main() {
  int tc, cn = 0;
  cin >> tc;
  while (cn++ < tc) {
    cin >> M >> F >> N;
    int i;
    ll p, s;
    vector<pair<ll, ll> > tmp_list;
    fr (i, N) {
      cin >> p >> s;
      tmp_list.pb(MP(p, s + 1));
    }
    sort(tmp_list.begin(), tmp_list.end());
    
    ll sum = 0;
    N = 0;
    fr (i, SZ(tmp_list)) if (tmp_list[i].S > sum) {
      P[N] = tmp_list[i].F;
      S[N] = tmp_list[i].S - sum;
      N++;
      sum = tmp_list[i].S;
    }

    ll res = 0;
    for (ll mul = 1; mul * F <= M; mul++) {
      ll cost = mul * F;
      ll tmp = 0;
      fr (i, N) {
        if (S[i] * mul * P[i] + cost > M) {
          tmp += (M - cost) / P[i];
          res = max(res, tmp);
          break;
        }

        tmp += S[i] * mul;
        cost += S[i] * mul * P[i];
        res = max(res, tmp);
      }
    }

    cout << "Case #" << cn << ": " << res << endl;
  }
  return 0;
}
