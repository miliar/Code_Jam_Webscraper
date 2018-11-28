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

char s[250][250];
double wp[200],owp[200],oowp[200];

int main () {
   wez(te)
   FORI(test,te) {
      printf("Case #%d:\n",test);
      wez(n)
      FOR(i,n) scanf("%s",s[i]);
      
      FOR(i,n) {
         int games = 0, won = 0;
         FOR(j,n) {
            if (s[i][j] == '1') {
               ++games;
               ++won;
            } else if (s[i][j]=='0') ++games;
         }
         wp[i] = (double)won/games;
      }
      
      FOR(i,n) {
         vector<double> wps;
         FOR(j,n) {
            if (s[i][j] == '0' || s[i][j] == '1') {
               // j == opponent
               int games=0,won=0;
               FOR(k,n) {
                  if (k != i) {
                     if (s[j][k] == '1') { ++games; ++won; }
                     else if (s[j][k] == '0') ++games;
                  }
               }
               wps.pb((double)won/games);
            }
         }
         double avg = 0;
         FOR(j,wps.sz) avg += wps[j];
         avg /= wps.sz;
         owp[i] = avg;
      }
      
      FOR(i,n) {
         vector<double> owps;
         FOR(j,n) {
            if (s[i][j] == '0' || s[i][j] == '1') {
               //j == opponent
               owps.pb(owp[j]);
            }
         }
         double avg = 0;
         FOR(j,owps.sz) avg += owps[j];
         avg /= owps.sz;
         oowp[i] = avg;
      }
      
      FOR(i,n) {
         printf("%.9lf\n",0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]);
      }
      //DBG(oowp[0])
      
      
   }
}








