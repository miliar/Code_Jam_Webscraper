#include <iostream>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>
using namespace std;
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)((x).size()))
#define rep(i, N) for (int i = 0; i < N; ++i)
#define foreach(it,v) for(__typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define print(x) cerr<<#x<<" = ";pr(x);cerr<<endl;
#define PRC(l,r) pr(l);foreach(it,v)pr(it==v.begin()?"":","),pr(*it);pr(r);
template<class T>void pr(T x){cerr<<x;} 
template<class T>void pr(vector<T>v){PRC('[',']');} 
template<class T1,class T2>void pr(pair<T1,T2>x){pr(x.first);pr(':');pr(x.second);} 
template<class T>void pr(set<T>v){PRC('{','}');} 
template<class T1,class T2>void pr(map<T1,T2>v){PRC('{','}');}
typedef long long lint;
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long double Double;
typedef vector<long double> vd;

void solve(int num) {
  printf("Case #%d: ", num);
  int N, L, H;
  cin >> N >> L >> H;
  vi f(N);
  for (int i = 0; i < N; ++i)
    cin >> f[i];
  for (int x = L; x <= H; ++x) {
    bool ok = true;
    for (int i = 0; i < N; ++i) {
      if (f[i] % x == 0 || x % f[i] == 0) continue;
      ok = false;
      break;
    }
    if (ok) {
      printf("%d\n", x);
      return;
    }
  }
  puts("NO");
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i) 
        solve(i);
    return 0;
}
