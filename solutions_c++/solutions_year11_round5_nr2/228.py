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

bool spr(const multiset<int> &in, int mid) {
   multiset<int> konce, s = in;
   while (!s.empty()) {
      // probujemy ulozyc str. dlugosci mid
      int m = *(s.begin());
      bool jest = 1;
      REP(i,m+1,m+mid-1) if (!IN(i,s)) { jest=0;break; }
      if (jest) {
         konce.insert(m+mid-1);
         REP(i,m,m+mid-1) s.erase(s.find(i)); // tylko jeden!
      } else {
         if (!IN(m-1,konce)) return 0;
         int minim;
         REP(i,m,m+mid-1) {
            if (!IN(i,s)) {
               minim = i-1;
               break;
            }
            s.erase(s.find(i)); // tylko jeden!
         }
         konce.erase(konce.find(m-1));
         konce.insert(minim);
      }
   }
   return 1;
}


int main () {
   int tests;
   scanf("%d",&tests);
   // cin >> tests;
   FORI(testno,tests) {      
      printf("Case #%d: ",testno);
      
      wez(n)
      if (n==0) {
         pisz(0);
         continue;
      }
      multiset<int> in;
      FOR(i,n) {
         wez(x)
         in.insert(x);
      }
      int from = 2, to = n, best = 1;
      while (to >= from) {
         int mid = (from+to)/2;         
         //DBG(mid)
         
         if (spr(in,mid)) {
            REMAX(best,mid)
            from = mid+1;
         } else {
            to = mid-1;
         }
      }
      
      
      
      printf("%d\n",best);
   }
}
