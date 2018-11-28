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

// uwaga: dzia³aj¹ tylko dla liczb nieujemnych

ll fromOtherBase(string s, int b) {
   ll res = 0, po = 1;
   REPD(i,s.length()-1,0) {
      int num;
      if (s[i] >= '0' && s[i] <= '9') num = s[i]-'0';
      else num = s[i]-'A'+10;
      res += po*num;
      po *= b;
   }
   return res;
}

string toOtherBase(ll num, int b) {
   string w;
   if (num==0) w = "0";
   while (num != 0) {
      int r = num%b;
      num /= b;
      if (r < 10) w += r+'0';
      else w += r+'A'-10;
   }
   reverse(ALL(w));
   return w;
}


int main () {
   int tests;
   scanf("%d",&tests);
   // cin >> tests;
   FORI(testno,tests) {      
      printf("Case #%d: ",testno);
      
      /*FOR(i,100) {
         DBG(i*i)
         string s = toOtherBase(i*i,2);
         FOR(k,50-s.length()) printf(" ");
         cout << s << endl;
      }*/
      string pattern;
      cin >> pattern;
      ll pat = 0, num = 0;
      int len = pattern.length();
      FOR(i,len) {
         if (pattern[len-1-i]=='?') {
            pat |= (1LL << i);
         } else if (pattern[len-1-i]=='1') {
            num |= (1LL << i);
         }
      }
//      DBG(toOtherBase(pat,2))
//      DBG(toOtherBase(num,2))
      FOR(i,1<<30) {
         ll pot = (ll)i*i;
         ll roznice = (pot ^ num) & (~pat);
         if (!roznice) {
            cout << toOtherBase(pot,2) << endl;
            //break;
         }
      }
      cerr << testno << endl;
      
      
      
   }
}
