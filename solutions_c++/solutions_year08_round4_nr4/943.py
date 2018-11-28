#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <sstream>
#include <cstdlib>
#include <cmath>

using namespace std;

#define LET(x,a) typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(i,v) FOR(i,(v).begin(),(v).end())
#define SET0(a) memset(a,0,sizeof(a))
#define SET1(a) memset(a,-1,sizeof(a))
#define pb push_back
#define PII pair<int,int>
#define ins insert
#define mp make_pair

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;

#define INF (int)1e9
#define GI ({int ttxxy;scanf("%d",&ttxxy);ttxxy;})
#define sz size()

int main() {
  int T = GI;
  REP(kase, T) {
    int k = GI;
    string s; cin >> s;
    int a[k];
    REP(i,k) a[i] = i;
    int ans = INF;
    string best;
    do {
      string p = s;
      REP(i,s.sz/k) REP(j,k)
	p[k*i+a[j]] = s[k*i+j];
      char prev = '.';
      string temp;
      REP(i,s.sz) if(prev != p[i]) prev = p[i], temp += p[i];
      //cout << p << " "  << temp << endl;
      if(ans > temp.sz)
	ans = temp.sz, best = temp;
    } while(next_permutation(a, a+k));
    //cout << best << endl;
    printf("Case #%d: %d\n", kase+1, ans);
  }
  return 0;
}
