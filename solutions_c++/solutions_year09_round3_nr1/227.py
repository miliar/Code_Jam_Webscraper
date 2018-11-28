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

ull conv(const string& s){
  vector<int> mp(0x100, -1);
  mp[s[0]] = 1;
  int cnt=0;
  for(int i=1;i<s.size();++i){
    if(mp[s[i]] == -1){
      mp[s[i]] = cnt++;
      if(cnt == 1) ++cnt;
    }
  }
  ull ret = 0;
//   string t(s);
//   FOR (it,t) *it = mp[*it] + '0';
//   cerr << s << ',' << t << ',' << cnt << endl;
  if(cnt == 0) cnt = 2;
  REP(i,s.size()){
    ret = ret*cnt + mp[s[i]];
  }
  //if(ret == 1) ret = 0;
  return ret;
}
int main()
{
  int T;
  cin >> T;
  REP(turn, T){
    string s;
    cin >> s;
    printf("Case #%d: %lld\n", turn+1, conv(s));
  }
  
  return 0;
}

