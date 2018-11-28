#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<queue>
#include<stack>
#include<deque>
#include<vector>
#include<algorithm>
#include<string>
#include<sstream>
#include<set>
#include<map>
#include<fstream>
#include<complex>
#include<cassert>
#include<climits>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
const double PI = 3.14159265;

string mat[40];
int N;

struct S{
  vector<int> r;
  int t;
  S() : t(0), r(N){
    t = 0;
    REP(i,N) r[i] = i;
  }
  bool check() const{
    REP(i,N){
      for(int j=i+1; j < N; ++j){
        if(mat[r[i]][j] == '1') return false;
      }
    }
    return true;
  }
  void print() const{
    cout << t << endl;
    REP(i, N){
      cout << mat[r[i]] << endl;
    }
    cout << endl;
  }
};

int main()
{
  int T;
  cin >> T;
  REP(turn, T){
    cin >> N;
    REP(i, N) cin >> mat[i];
    
    int ans = 9999999;
    queue<S> q;
    S init;
    set<vector<int> > memo;
    q.push(init);
    while(!q.empty()){
      S s = q.front(); q.pop();
      if(memo.find(s.r) != memo.end()) continue;
      memo.insert(s.r);
      //cout << s.t << endl;
      //s.print();
      if(s.check()){
        ans = s.t;
        break;
      }
      REP(i, N-1){
        S ns;
        ns.r = s.r;
        ns.t = s.t +1;
        swap(ns.r[i], ns.r[i+1]);
        q.push(ns);
      }
    }
    printf("Case #%d: %d\n", turn + 1, ans);
    //return 0;
  }
  return 0;
}

