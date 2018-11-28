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

#define M 505
char tab[M][M];
ll mass[M][M];
#define pll pair<ll,ll>
pll vec[M][M],
sumacz[M][M], // sumcz[i][j] = vec[i][0] + ... + vec[i][j];
suma[M][M];

ll msumacz[M][M], msuma[M][M];

pll operator + (const pll &p, const pll &q) {
   return pll(p.fi+q.fi,p.se+q.se);
}
pll operator - (const pll &p, const pll &q) {
   return pll(p.fi-q.fi,p.se-q.se);
}

void go() {
   wez3(n,m,syf)
   FOR(i,n) scanf("%s",tab[i]);
   FOR(i,n) FOR(j,m) {
      mass[i][j]=tab[i][j]-'0';
      vec[i][j] = pll(i*mass[i][j], j * mass[i][j]);
   }
   FOR(i,n) {
      sumacz[i][0] = vec[i][0];
      msumacz[i][0] = mass[i][0];
      FORI(j,m-1) {
         sumacz[i][j] = sumacz[i][j-1] + vec[i][j];
         msumacz[i][j] = msumacz[i][j-1] + mass[i][j];
      }
   }
   FOR(j,m) {
      suma[0][j] = sumacz[0][j];
      msuma[0][j] = msumacz[0][j];
   }
   FORI(i,n-1) {
      FOR(j,m) {
         suma[i][j] = suma[i-1][j] + sumacz[i][j];
         msuma[i][j] = msuma[i-1][j] + msumacz[i][j];
      }
   }
   
   
   REPD(k,min(n,m),3) {
      FOR(i,n-k+1) FOR(j,m-k+1) {
         pll s = suma[i+k-1][j+k-1];
         ll ms = msuma[i+k-1][j+k-1];
         if (i > 0) {
            s = s - suma[i-1][j+k-1];
            ms = ms - msuma[i-1][j+k-1];
         }
         if (j > 0) {
            s = s - suma[i+k-1][j-1];
            ms = ms - msuma[i+k-1][j-1];
         }
         if (i > 0 && j > 0) {
            s = s + suma[i-1][j-1];
            ms = ms + msuma[i-1][j-1];
         }
         s = s - vec[i][j];
         s = s - vec[i+k-1][j];
         s = s - vec[i][j+k-1];
         s = s - vec[i+k-1][j+k-1];
         ms = ms - mass[i][j];
         ms = ms - mass[i+k-1][j];
         ms = ms - mass[i][j+k-1];
         ms = ms - mass[i+k-1][j+k-1];
         
         ll srx2 = 2*i + k-1, sry2 = 2*j + k-1;
         ll bal1 = 2*s.fi - srx2*ms,
         bal2 = 2*s.se - sry2*ms;
         if (bal1 == 0 && bal2 == 0) {
            pisz(k);
            return;
         }
         
         /*double sumx=0,sumy=0;
         double srx=i+(double)(k-1)/2, sry = j+(double)(k-1)/2;
         set<pii> pkty;
         REP(a,i,i+k-1) REP(b,j,j+k-1) {
            pkty.insert(mp(a,b));
         }
         pkty.erase(mp(i,j));
         pkty.erase(mp(i+k-1,j));
         pkty.erase(mp(i+k-1,j+k-1));
         pkty.erase(mp(i,j+k-1));
         FOREACH(it,pkty) {
            int a = it->fi, b = it->se;
            sumx += ((double)a-srx)*num[a][b];
            sumy += ((double)b-sry)*num[a][b];
         }
         if (abs(sumx) +abs(sumy) < 1e-8) {
            pisz(k);
            return;
         }*/
      }
   }
   
   
   

   printf("IMPOSSIBLE\n");
}

int main () {
   wez(te)
   FORI(testno,te) {
      printf("Case #%d: ",testno);
      
      go();
   }
}
