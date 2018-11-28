#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
using namespace std;
#define pb push_back
#define INF 2147483647
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define sz size()
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,t.size())s<<t[i]<<" ";return s; }
#define IN(x,y) ((y).find((x))!=(y).end()) 
#define DBG(vari) cout<<#vari<<" = "<<vari<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));

int main () {
   wez(te)
   FORI(test,te) {
      wez3(X,S,R)
      wez2(TT,N)
      R -= S; // R to przyspieszenie
      
      vector<pii> v;
      int sumadl = 0;
      while(N--) {
         wez3(bi,ei,wi)
         v.pb(mp(wi+S,ei-bi));
         sumadl += ei-bi;
      }
      
      v.pb(mp(S,X-sumadl));
      sort(ALL(v));
      
      double ans = 0;
      double t = TT;
      
      FOR(i,v.sz) {
         double runspeed = v[i].fi + R, length = v[i].se;
         double runtime = min(t, length/runspeed);
         t -= runtime;
         ans += runtime;
         length -= runtime*runspeed;
         double walkspeed = v[i].fi;
         ans += length/walkspeed;
      }
      
      printf("Case #%d: %.9lf\n",test,ans);
   }
}





