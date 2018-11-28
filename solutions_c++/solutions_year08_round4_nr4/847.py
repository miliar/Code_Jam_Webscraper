#include<iostream>
#include<vector>
#include<queue>
#include<list>
#include<algorithm>
#include<functional>
#include<map>
#include<set>
#include<utility>
#include<string>

#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>

using namespace std;

#define FOR(i,s,n) for (int i=(int)(s); i<(int)(n); ++i)
#define REP(i,n) FOR(i,0,n)
#define PB push_back
#define MP make_pair
#define ALL(c) (c).begin(), (c).end()
const int inf(1<<24);

int main()
{
  int N;
  cin >> N;
  REP(i, N) {
    int k;
    string S;
    cin >> k >> S;
    //cerr << S << endl;
    string tmp(S);
    int len(S.length());
    vector<int> perm(k);
    REP(j, k) perm[j] = j;
    int ans(inf);
    do {//while (next_permutation(ALL(perm))) {
      REP(j, len/k) {
        REP(m, k) {
          tmp[j*k + m] = S[j*k + perm[m]];
        }
      }
      //cerr << " " << string(tmp.begin(), unique(ALL(tmp))) << endl;
      int g(1);
      char prev(tmp[0]);
      FOR(j,1,len) {
        if (prev != tmp[j]) {
          prev = tmp[j];
          g++;
        }
      }
      ans = min(ans, g);
      //ans = min(ans, (unique(ALL(tmp)) - tmp.begin()));
    } while (next_permutation(ALL(perm)));
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  
  return 0;
}
