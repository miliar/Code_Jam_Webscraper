#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<sstream>
#include<cassert>
#include<queue>
#include<stack>
#include<bitset>
#include<cstring>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)

using namespace std;
typedef long long lli;
typedef vector<int> vint;
typedef pair<int, int> pii;
const double EPS = 0.00000001;
const int INF = 1000000000;
template<class T> void pp(T t, int n){
  rep(i, n){
    cout << t[i] << ' ';
  }
  cout << endl;
}

const int N = 100;

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout << "Case #" << tc+1 << ":" << endl;
    char t[N][N];
    int n;
    vector<pair<int, int> > OWP[N];
    cin >> n;
    rep(i, n)rep(j, n)cin>>t[i][j];
    
    long double WP[N];
    rep(r, n){
      int sum = 0, win = 0;
      rep(c, n){
        if(t[r][c] == '.')continue;
        if(t[r][c] == '1')win++;
        sum++;
      }
      WP[r] = (long double)win / (long double)sum;
    }




    rep(r, n){
      rep(out, n){
        if(t[r][out] == '.')continue;
        int sum, win;
        sum = win = 0;
        rep(c, n){
          if(c == out)continue;
          if(t[r][c] == '.')continue;
          sum++;
          if(t[r][c] == '1')win++;
        }
        OWP[out].push_back(make_pair(win, sum));
      }
    }
    long double owp[N];
    rep(i, n){
      owp[i] = 0;
      FOR(it, OWP[i]){
        owp[i] += (long double)it->first / (long double)it->second;
      }
      owp[i] /= (long double)OWP[i].size();
    }
    long double oowp[N];
    rep(r, n){
      long double sum = 0;
      int cnt = 0;
      rep(c, n){
        if(t[r][c] == '.')continue;
        cnt++;
        sum += owp[c];
      }
      oowp[r] = sum / (long double)cnt;
    }
    rep(i, n){
      long double ans = 0.25 * WP[i] + 0.50 * owp[i] + 0.25 * oowp[i];
      printf("%.10Lf\n", ans);
    }
  }
  return 0;
}
