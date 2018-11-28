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

int d;

struct Syf {
   vector<pii> v;
   int lewy, prawy;
   int ile;
};

vector<Syf> moduly;

bool merguj() {
   FOR(i,moduly.sz) {
      REP(j,i+1,moduly.sz-1) {
         if (moduly[i].lewy >= moduly[j].prawy || moduly[j].lewy >= moduly[i].prawy) {
            // rozlaczne
         } else {
            moduly[i].ile += moduly[j].ile;
            FOR(k,moduly[j].v.sz) moduly[i].v.pb(moduly[j].v[k]);
            int srodek = (moduly[i].v[0].fi + moduly[i].v.back().fi)/2;
            int ile = moduly[i].ile;
            moduly[i].lewy = srodek - d*ile/2;
            moduly[i].prawy = srodek + d*ile/2;            
            
            moduly.erase(moduly.begin()+j);
            return true;
         }
      }
   }
   return false;
}

int main () {
   wez(te)
   FORI(test,te) {
      moduly.clear();
      wez(c)
      scanf("%d",&d);
      d *= 2;
      while(c--) {
         wez2(p,v)
         p *= 2;
         Syf s;
         s.v.pb(mp(p,v));
         s.ile=v;
         s.lewy = p;
         s.lewy -= d*v/2;
         s.prawy = p;
         s.prawy += d*v/2;
         moduly.pb(s);
      }
      
      while(merguj());
      
/*      FOR(i,moduly.sz) {
         DBG(i)
         DBG(moduly[i].lewy)
         DBG(moduly[i].prawy)
         DBG(moduly[i].ile)
         DBG(moduly[i].v)
      }*/
      
      double ans = 0;
      
      FOR(i,moduly.sz) {
         int poz = moduly[i].lewy + d/2;
         FOR(j,moduly[i].v.sz) {
            FOR(k,moduly[i].v[j].se) {
               int jest = moduly[i].v[j].fi;
               int syfek = abs(jest-poz);
               //DBG(jest)
               //DBG(poz)
               if (ans < syfek) ans = syfek;
               poz += d;
            }
         }
      }
//      ans -= d/2;
      
      printf("Case #%d: %.9lf\n",test,ans/2);
   }
}
