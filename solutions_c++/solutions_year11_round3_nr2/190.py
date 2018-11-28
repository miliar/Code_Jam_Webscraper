#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long v[1000005];
int main() {
  int casn;
  scanf("%d", &casn);
  for(int cas=1; cas<= casn; ++cas) {
    int L, N, C;
    long long t;
    long long res=0;
    scanf("%d%lld%d%d", &L, &t, &N, &C);
    for(int i=0; i<C; ++i) cin >> v[i];
    for(int i=0; i<N; ++i) v[i] = v[i%C], res += v[i] * 2;
    vector<long long> vt;
    int i=0;
    long long tsum=0;
    for(; i<N; ++i) {
      if(tsum+v[i]*2 > t) {
        vt.push_back(v[i]-(t-tsum)/2);
        break;
      }
      tsum += v[i]*2;
    }
//    for(int i=0; i<vt.size(); ++i) cout << vt[i] << " "; cout << endl;
    for(i=i+1; i<N; ++i) vt.push_back(v[i]);
    sort(vt.begin(), vt.end());
    for(int i=0; i<L; ++i) {
      int id=vt.size()-1-i;
      if(id < 0) break;
      res -= vt[id];
    }
    cout << "Case #" << cas << ": " << res << endl;
  }
  return 0;
}

