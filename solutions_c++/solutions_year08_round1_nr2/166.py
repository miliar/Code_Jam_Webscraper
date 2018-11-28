#include <vector>
#include <algorithm>
#include <string>
#include <iostream>
#include <cmath>
#include <set>
#include <queue>
using namespace std;
#define GI ({int t;scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i<(b);++i)
#define EACH(x,v) for(typeof(v.begin()) x=v.begin();x<v.end();x++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define mkp make_pair
#define sz size()
#define bset(i,j) (i&(1<<j))
#define INF (int)1e8
#define MAX 402
typedef long long LL;
typedef double D;
typedef vector<int> VI;
using namespace std;
int main()
{
     #define MALTED 1
     #define UNMALTED 0
  int t=GI, kase=1;
  while(t--) {
     int n=GI, cust=GI;
     vector < pair<int,int> > v[cust];
     REP(i,cust) {
          int pref=GI;
          REP(j,pref) {
               int a=GI-1, b=GI;
               v[i].pb(mkp(a,b));
          }
     }
     VI ans;
     REP(i,n) ans.pb(0);
     int changed=1;
     while(changed) {
          changed=0;
          REP(i,cust) {
               int good=0;
               REP(j,v[i].sz) {
                    int type = v[i][j].first, malt=v[i][j].second;
                    if(malt==UNMALTED && ans[type] == UNMALTED)
                    good=1;
                    else if(malt==MALTED && ans[type] == MALTED)
                    good=1;
                    if(good) break;
               }
               if(!good) {
                    REP(j,v[i].sz) 
                    if(v[i][j].second == MALTED) {
                         ans[v[i][j].first] = MALTED;
                         changed=1;
                         break;
                    }          
               }
          }
     }
     int bad=0;
     REP(i,cust) {
          int good=0;
          REP(j,v[i].sz) {
               int type = v[i][j].first, malt=v[i][j].second;
               if(malt==UNMALTED && ans[type] == UNMALTED)
               good=1;
               else if(malt==MALTED && ans[type] == MALTED)
               good=1;
               if(good) break;
          }
          if(!good) { bad=1; break; }
     
     }
     if(bad)
     printf("Case #%d: IMPOSSIBLE\n", kase++);
     else {
     printf("Case #%d: ", kase++);
     REP(i,n) printf("%d ", ans[i]);
     printf("\n");
     }
  }
  
  
  
  
}
