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
  printf("Case #%d:\n", num);
  int R, C;
  cin >> R >> C;
  vs S(R);
  for (int i = 0; i < R; ++i)
    cin >> S[i];
  while (true) {
    int i0 = -1, j0 = -1;
    for (int i = 0; i0 == -1 && i < R; ++i) 
      for (int j = 0; i0 == -1 && j < C; ++j)
        if (S[i][j] == '#') {
          i0 = i;
          j0 = j;
        }
    if (i0 == -1) {
      for (int i = 0; i < R; ++i) 
        cout << S[i] << endl;
      return;
    }
    if (i0 + 1 < R && j0 + 1 < C &&   
      S[i0][j0 + 1] == '#' && 
      S[i0 + 1][j0] == '#' && 
      S[i0 + 1][j0 + 1] == '#') {
      S[i0][j0] = S[i0 + 1][j0 + 1] = '/';
      S[i0][j0 + 1] = S[i0 + 1][j0] = '\\';
    } else {
        puts("Impossible");
        return;
    }
  }
}

int main() {
    int tst;
    cin >> tst;
    for (int i = 1; i <= tst; ++i) 
        solve(i);
    return 0;
}
