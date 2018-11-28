using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define REP(v, hi) for (int v=0; v<(hi); v++)
#define REPD(v, hi) for (int v=((hi)-1); v>=0; v--)
#define FOR(v, lo, hi) for (int v=(lo); v<(hi); v++)
#define FORD(v, lo, hi) for (int v=((hi)-1); v>=(lo); v--)

typedef long long LL;
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef vector <string> VS;

LL cnt[50][2][3][5][7];

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {

    string s;
    cin>>s;

    int N=s.SZ;

    memset(cnt,0,sizeof(cnt));
    cnt[0][0][0][0][0] = 1;
    
    REP(n,N) REP(m2,2) REP(m3,3) REP(m5,5) REP(m7,7) {
      int num2=0;
      int num3=0;
      int num5=0;
      int num7=0;

      FOR(next,n,N) {
	num2 = (10*num2 + s[next]-'0') % 2;
	num3 = (10*num3 + s[next]-'0') % 3;
	num5 = (10*num5 + s[next]-'0') % 5;
	num7 = (10*num7 + s[next]-'0') % 7;
	cnt[next+1][(m2+num2)%2][(m3+num3)%3][(m5+num5)%5][(m7+num7)%7] += cnt[n][m2][m3][m5][m7];
	cnt[next+1][(m2-num2+2)%2][(m3-num3+3)%3][(m5-num5+5)%5][(m7-num7+7)%7] += cnt[n][m2][m3][m5][m7];
      }
    }

    LL res=0;
    REP(m2,2) REP(m3,3) REP(m5,5) REP(m7,7)
      if (!m2 || !m3 || !m5 || !m7) res += cnt[N][m2][m3][m5][m7];
    
    printf ("Case #%i: %lli\n",run, res/2);
  }

  return 0;
}
