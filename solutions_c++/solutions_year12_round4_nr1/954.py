#include <algorithm>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <cstring>

#define SIZE(s) ((int)((s).size()))
#define FOREACH(it,vec) for(typeof((vec).begin())it=(vec).begin();it!=(vec).end();++it)
#define REP(i,n) for(int i=0;i<(int)(n);++i)

using namespace std;

int T,N;
vector<long long> D;
vector<long long> L;
vector<long long> B;

int main(void) {
  cin >> T;
  REP(t,T) {
    D.resize(0); 
    L.resize(0);
    B.resize(0);
    cin >> N;
    D.resize(N+1);
    L.resize(N+1);
    B.resize(N+1,0);
    REP(n,N) cin >> D[n] >> L[n];
    cin >> D[N];
    L[N] = 0;
    B[N] = -1;

    B[0] = D[0];

    REP(i,N+1) {
      for(int j=i+1;j<=N;++j) {
        if (D[j]-D[i] > B[i]) break;
        else B[j] = max(B[j], min(D[j]-D[i],L[j]));
      }
    }
    
    cout << "Case #" << t+1 << ": ";
    if (B[N] > -1) cout << "YES";
    else cout << "NO";
    cout << endl;
  }
  return 0;
}
