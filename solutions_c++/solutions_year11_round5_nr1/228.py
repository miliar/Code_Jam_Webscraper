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
#include <iomanip>
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

const long double eps = 1e-8;

int main () {
   int tests;
   scanf("%d",&tests);
   // cin >> tests;
   FORI(testno,tests) {
      printf("Case #%d:\n",testno);
      
      wez3(width,low,up)wez(g)
      
      map<long double,long double> lower, upper,m;
      set<long double> hhh;
      
      FOR(i,low) {
         wez2(x,y)
         lower.insert(mp(x,y));
         hhh.insert(x);
      }
      FOR(i,up) {
         wez2(x,y)
         upper.insert(mp(x,y));
         hhh.insert(x);
      }
      FOREACH(it,hhh) {
         long double x = *it;
         bool in1 = IN(x,lower), in2 = IN(x,upper);
         if (in1 && in2) {
            m[x] = upper[x]-lower[x];
         } else if (in1) {
            map<long double,long double>::iterator ig = upper.lower_bound(x);
            long double x2 = ig->fi, y2 = ig->se;
            ig--;
            long double x1 = ig->fi, y1 = ig->se;
//            DBG(x)
  //          DBG(mp(x1,x2))
    //        DBG(mp(y1,y2))
            long double y = (y2-y1)/(x2-x1)*(x-x1) + y1;
      //      DBG(y)
            m[x] = y-lower[x];
         } else {
            map<long double,long double>::iterator ig = lower.lower_bound(x);
            long double x2 = ig->fi, y2 = ig->se;
            ig--;
            long double x1 = ig->fi, y1 = ig->se;
            //DBG(x)
            //DBG(mp(x1,x2))
            //DBG(mp(y1,y2))
            long double y = (y2-y1)/(x2-x1)*(x-x1) + y1;
            //DBG(y)
            m[x] = upper[x]-y;
         }
      }
      
      
      long double calepole = 0;
      FOREACH(it,m) {
         if (it == m.begin()) continue;
         map<long double, long double >::iterator it2 = it;
         it2--;
         long double h1 = it2->se, h2 = it->se, h = (h1+h2)/2;
         calepole += h * (it->fi - it2->fi);
         //DBG(h * (it->fi - it2->fi))
      }
      
      const long double kawalek = calepole/g;
      //DBG(kawalek)
      g--;
      long double akt = kawalek;
      FOREACH(it,m) {
         if (it == m.begin()) continue;
         map<long double, long double >::iterator it2 = it;
         it2--;
         long double h1 = it2->se, h2 = it->se, h = (h1+h2)/2;
         long double pole = h * (it->fi - it2->fi);
         long double x2 = it->fi, x1 = it2->fi;
//         DBG(mp(x1,x2))
         if (akt > pole+eps) {
            akt -= pole;
         } else {
            long double from = 0, to = x2-x1;
            while (to > from+eps) {
               long double mid = (from+to)/2;
               if (mid*(h1 + (h2-h1)*mid/(2*(x2-x1))) > akt) {
                  to = mid;
               } else {
                  from = mid;
               }
            }
            cout << fixed << setprecision(9) << x1+from << endl;
            //DBG(akt)
            //DBG(from*(h1 + (h2-h1)*from/(2*(x2-x1))))
            //
            g--;
            if (!g) break;
            akt = kawalek;
            m.insert(mp(x1+from,h1 + (h2-h1)*from/(x2-x1)));
            //DBG(mp(x1+from,h1 + (h2-h1)*from/(x2-x1)))
            it--;
         }
      }
      
      
   }
}
