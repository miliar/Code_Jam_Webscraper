#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<vector>
#include<string>

using namespace std;

#define REP(i,n) for(int i=0;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()

typedef unsigned long long ull;

int main () {
  int L, D, N;
  cin >> L >> D >> N;
  vector<string> words(D);
  REP(i,D) cin >> words[i];
  vector<ull> pattern(L);
  REP(i,N) {
    pattern.assign(L, 0);
    int j = 0;
    bool group = false;

    string line;
    cin >> line;
    FOR(c, line) {
      if        (*c == '(') {
        group = true;
      } else if (*c == ')') {
        group = false;
        ++j;
      } else {
        pattern[j] |= 1ull << (*c-'a');
        if(!group) ++j;
      }
    }

    int ans = 0;
    REP(d,D)
      REP(l,L) {
        if ((pattern[l] & (1ull << (words[d][l] - 'a'))) == 0) break;
        if (l == L-1) ans++;
      }
    printf("Case #%d: %d\n", i+1, ans);
  }
}
