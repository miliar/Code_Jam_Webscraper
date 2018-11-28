#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <vector>
#include <cmath>
#include <list>
#include <sstream>
#include <algorithm>

using namespace std;

typedef pair<int,int> PII;
typedef long long LL;
typedef vector<int> VI;
typedef pair<LL,LL> PLL;
typedef vector<pair<int,int> > VPII;
typedef vector<LL> VLL;
typedef vector<vector<int> > VVI;
typedef vector<string> VS;

#define PI 3.14159265358979323
#define EE 2.71828182845
#define EPS 10e-11
#define INF 1000000

inline LL MAX(LL a, LL b){ return a < b ? b : a;}
inline LL MIN(LL a, LL b){ return a < b ? a : b;}

#define FOR(i,n)      for(int i=0;i<(n);i++)
#define FORD(i,n)     for(int i=(n)-1;i>=0;i--)

#define MP make_pair
#define PB push_back

string pat = "welcome to code jam";

int DP[550][20];

int main(){

  int TT;
  scanf("%d ",&TT);
  FOR(tt,TT){

    string s="";
    char c='.';
    while (c != '\n'){
      s+=c;
      scanf("%c",&c);
    }

    memset(DP,0,sizeof(DP));
    FOR(i,s.length()){
      
      FOR(j,pat.length())if (pat[j] == s[i]){
        if (j == 0){ DP[i][j] = 1; continue; }
        FOR(k,i) if (s[k] == pat[j-1]) DP[i][j] += DP[k][j-1];
        DP[i][j] %= 10000;

        //
        //cout << i << " " << j << " " << DP[i][j] << endl;
        //
      }

    }

    int res = 0;
    FOR(i,s.length()) res += DP[i][ pat.length()-1 ];
    res %= 10000;
    printf("Case #%d: %04d\n",tt+1,res);

  }
  return 0;
}

