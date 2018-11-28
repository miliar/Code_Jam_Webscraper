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

VS vstup;
VS P[2];
int L,D,N;
set<char> S[16];

int main(){
  scanf("%d %d %d ",&L, &D, &N);
  vstup.resize(D);
  FOR(i,D){ char temp[20]; scanf("%s ",temp); vstup[i] = string(temp); }
  FOR(tt,N){
      char slovo[500];
      scanf("%s",slovo);
      int p=0;
      FOR(i,L) S[i].clear();
      FOR(i,L){
        if (slovo[p] != '('){ S[i].insert(slovo[p]); p++; continue;}
        p++;
        while (slovo[p]!=')'){ S[i].insert( slovo[p]); p++;  }
        p++;
      }
      P[0] = vstup;
      FOR(i,L){
        int old = i%2;
        int nw = (i+1)%2;
        P[nw].resize(0);
        FOR(j,P[old].size()){
          if ( S[i].find( P[old][j][i] ) != S[i].end()) P[nw].PB( P[old][j] );
        }        
      }
      int ans=0;
      if (L%2){ ans = P[1].size(); }
      else{ ans = P[0].size();  }
      
      printf("Case #%d: %d\n",tt+1,ans);
  }


}
