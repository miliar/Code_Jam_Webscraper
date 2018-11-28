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
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
const double PI = 3.14159265;

template <class T>
struct fenwick_tree {
  vector<T> x;
  fenwick_tree(int n) : x(n, 0) { }
  T sum(int i, int j) {
    if (i == 0) {
      T S = 0;
      for (j; j >= 0; j = (j & (j + 1)) - 1) S += x[j];
      return S;
    } else return sum(0, j) - sum(0, i-1);
  }
  void add(int k, T a) {
    for (; k < x.size(); k |= k+1) x[k] += a;
  }
};



int main()
{
  int T;
  cin >> T;
  REP(turn, T){
    int P,Q;
    cin >> P >> Q;
    vector<int> qs(Q);
    REP(i,Q){
      int k; cin >> k;
      qs[i] = --k;
    }

    int mincost = 999999999;
    do{
      //simulate
      vector<bool> live(P, true);
      int cost = 0;
      REP(i, Q){
        live[qs[i]] = false;
        for(int k=qs[i]-1; k>=0; --k){
          if(!live[k]) break;
          ++cost;
        }
        for(int k=qs[i]+1;k<P;++k){
          if(!live[k]) break;
          ++cost;
        }
      }
      mincost = min(mincost, cost);
    }while(next_permutation(ALL(qs)));
    //cout << mincost << endl;
    printf("Case #%d: %d\n", turn+1, mincost);
  }
  return 0;
}

