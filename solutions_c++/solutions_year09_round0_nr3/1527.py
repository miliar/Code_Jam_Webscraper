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

const string WCJ = "welcome to code jam";
const int L = WCJ.length();
vector<int>* _mp[28];
inline vector<int>* mp(char c) { return (c == ' ') ? _mp[27] : _mp[c -'a']; }

int solve() {
  char raw[550];
  cin.getline(raw,510);
  string line(raw);
  vector<int> cnt(L+1,0);
  cnt[0] = 1;

  FOR(cit, line)
  {
    if((int)*cit == 13) break;
    FOR(pit, *mp(*cit))
      cnt[*pit+1] = (cnt[*pit] + cnt[*pit+1]) % 10000;
  }
  return cnt[L];
}

int main () {
  int N; cin >> N;
  cin.ignore();
  REP(i, 28) _mp[i] = new vector<int>;
  REP(i, L) mp(WCJ[i])->push_back(i);
  REP(i,N) {
    printf("Case #%d: %04d\n", i+1, solve());
  }
}
