#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int _a;

#define FOR(i , n) for(int i = 0 ; i < n ; i++)
#define FOT(i , a , b) for(int i = a ; i < b ; i++)
#define GETINT (scanf("%d" , &_a) , _a)
#define pb push_back
#define mp make_pair
#define s(a) (int(a.size()))
#define PRINT(a) cerr << #a << " = " << a << endl
#define ALL(a) (a).begin(), (a).end()

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector< vs > vvs;
typedef pair<int , int> PII;

const int MOD = 100003;

map< PII, int > mc;
int c(int n, int k) {
  PII d(n, k);
  if(mc.find(d) != mc.end()) return mc[d];
  mc[d] = 0;
  int &ans = mc[d];
  if(n < 0 || k < 0) ans = 0;
  else if(n == 0) {
    if(k == 0) ans = 1;
  }
  else ans = (c(n - 1, k - 1) + c(n - 1, k)) % MOD;
  return ans;
}



map< PII, int > mb;
int b(int n, int t) {
  if(mb.find(PII(n, t)) != mb.end()) return mb[PII(n, t)];
  mb[PII(n, t)] = 0;
  int &ans = mb[PII(n, t)];
  if(n < 2) ans = 0;
  else if(t == 1) {
    ans = 1;
  }
  else {
    for(int k = 1; k <= t - 1; k++)
      ans = (ans + ll(b(t, k)) * c(n - t - 1, t - k - 1)) % MOD;
  }
  //  cerr << n << ' ' << t << ' ' << ans << endl;
  return ans;
}


int main() {
  mb.clear(); mc.clear();
  int T;
  cin >> T;
  FOR(test, T) {
    int n;
    cin >> n;
    int ret = 0;
    for(int t = 1; t <= n - 1; t++) ret = (ret + b(n, t)) % MOD;
    printf("Case #%d: %d\n", 1+test, ret);
  }
  return 0;
}
