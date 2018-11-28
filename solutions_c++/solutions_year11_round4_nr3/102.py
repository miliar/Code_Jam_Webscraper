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

ll nwd (ll a, ll b) {
   if (b==0) return a;
   return nwd(b, a%b);
}

ll nww(ll a, ll b) {
   return a/nwd(a,b)*b;
}

// dziala szybko dla miliona, dla 10 mln - ok. 2 sek
vector<bool> sito(int max_inclusive) { // zwraca zlozone!
   vector<bool> czyZlozona(max_inclusive+1,false);
   czyZlozona[0] = czyZlozona[1] = true;
   for (int i = 2; i*i <= max_inclusive; ++i) {
      if (!czyZlozona[i]) {
         for (int j = i; i*j <= max_inclusive; ++j) {
            czyZlozona[i*j] = true;
         }
      }
   }
   return czyZlozona;
}

vector<int> listaPierwszych (int max_inclusive) {
   vector<bool> czyZlozona = sito(max_inclusive);
   vector<int> wynik;
   FORI(i,max_inclusive) {
      if (!czyZlozona[i]) {
         wynik.pb(i);
      }
   }
   return wynik;
}



int main () {
   wez(te)
   vi v = listaPierwszych(1000000);
   FORI(test,te) {
      ll n;
      scanf("%I64d",&n);
      int pn = 0;
      FOR(i,v.sz) {
         ll po = (ll)v[i]*v[i];
         while (po <= n) {
            ++pn;
            po *= v[i];
         }
      }
      
      int ans = pn;
      if (n > 1) ++ans;
      printf("Case #%d: %d\n",test,ans);
   }
}





