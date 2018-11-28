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
#define INF (int)1e9
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
      map<pair<char,char>,char> comb;
      set<char> oppo[300];
      wez(C)
      FOR(i,C) {
         string s;
         cin >> s;
         comb.insert(mp(mp(s[0],s[1]),s[2]));
         comb.insert(mp(mp(s[1],s[0]),s[2]));
      }
      wez(D)
      FOR(i,D) {
         string s;
         cin >> s;
         oppo[s[0]].insert(s[1]);
         oppo[s[1]].insert(s[0]);
      }
      
      vector<char> v;
      wez(n)
      string s;
      cin >> s;
      FOR(i,n) {
         v.pb(s[i]);
         if (v.sz <= 1) continue;
         while (1) {
            if (v.sz <= 1) break;
            if (IN(mp(v[v.sz-1],v[v.sz-2]),comb)) {
               char nowy = comb[mp(v[v.sz-1],v[v.sz-2])];
               v.pop_back();
               v.pop_back();
               v.pb(nowy);
            } else break;
         }
         if (v.sz <= 1) continue;
         FOR(j,v.sz-1) {
            if (IN(v[j], oppo[v[v.sz-1]])) {
               v.clear();
               break;
            }
         }
      }
      
      printf("Case #%d: [",test);
      if (!v.empty()) {
         printf("%c",v[0]);
         FORI(j,v.sz-1) {
            printf(", %c",v[j]);
         }
      }
      printf("]\n");
      
   }
}
