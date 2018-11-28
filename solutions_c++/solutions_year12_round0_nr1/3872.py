#ifndef DEBUG
# define dbg(x)
# define NDEBUG
#else
# define dbg(x) x
#endif
#include <cstdio>
#include <cstring>
#include <cstdarg>
#include <cassert>
#include <algorithm>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);i++)
#define FOR(i,b) FR(i,0,b)
typedef long long ll;
const ll INF=1000000000000000000LL;

const char map1[] = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jvaozq";
const char map2[] = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give upyeqz";

const int MAXG=100;
int T,G;
char buf[MAXG+1];
bool cov[26];

char map(char c) {
	FOR(j,sizeof(map1)/sizeof(char)) {
		if(map1[j]==c) {
			return map2[j];
		}
	}
	return -1;
}

int main() {
	dbg(freopen("ese.in","r",stdin));
	dbg(freopen("ese.out","w",stdout));
	scanf("%d ",&T);
	FOR(i,26) {
		cov[map(i+'a')-'a']=true;
	}
	FOR(i,26) {
		if(!cov[i]) putchar('a'+i);
	}
	FOR(t,T) {
		gets(buf);
		G=strlen(buf);
		printf("Case #%d: ",t+1);
		FOR(i,G) {
			char c=map(buf[i]);
			assert(c!=-1);
			putchar(c);
		}
		putchar('\n');
	}

	return 0;
}

