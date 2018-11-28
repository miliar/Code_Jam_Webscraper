
// UW forfiters
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<string> VS;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

string tab1[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                 "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                  "de kr kd eoya kw aej tysr re ujdr lkgc jv"};


string tab2[] = {"our language is impossible to understand",
                 "there are twenty six factorial possibilities",
                  "so it is okay if you want to just give up"};

const int max_len = 1000100;
char buf[max_len];
int main()
{
   map<char,char> M;
   REP(i,3) {
      REP(j,SIZE(tab1[i])) M[tab1[i][j]] = tab2[i][j];
   }
//   FORE(e,M) printf("%c->%c\n",e->FI,e->SE);
 //  printf("%d\n",SIZE(M));
   M['z'] = 'q';
   M['q'] = 'z';
   int T;
   scanf("%d",&T);
   fgets(buf, max_len - 1, stdin);

   FOR(tc,1,T) {
      fgets(buf, max_len - 1, stdin);
      int d = strlen(buf) - 1;
      printf("Case #%d: ",tc);
      REP(i,d) printf("%c", M[buf[i]]);
      puts("");
   }
   return 0;
}
