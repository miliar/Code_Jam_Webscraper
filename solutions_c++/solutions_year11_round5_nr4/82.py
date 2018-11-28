#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
typedef unsigned long long ull;

int _;
char s[1000],z[1000];

int main() {
   scanf("%d ",&_);
   REP(test,_) {

      printf("Case #%d: ",test+1);
      gets(s);
      strcpy(z,s);
      int m=strlen(s), n=0;
      REP(i,m) if (s[i]=='?') ++n;
      REP(mask,1<<n) {
	 ull x=0; int k=0;
	 REP(i,m) if (s[i]=='?') x=2*x + !!(mask&(1<<k)), z[i]=!!(mask&(1<<k))+'0', ++k;
	 else x=2*x + s[i]-'0';
	 ull s = sqrtl(x);
	 if (s*s==x) puts(z);
      }

   }
}
