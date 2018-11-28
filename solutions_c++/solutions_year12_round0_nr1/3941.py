/**
 * Author: Shrey Banga
 */
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <algorithm>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i < (b); i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,v) for(typeof(v.begin()) i = v.begin(); i != v.end(); i++)

#if 0
#define DBG(args...) fprintf(stderr, args)
#else
#define DBG(args...)
#endif

char f[] = "yhesocvxduiglbkrztnwjpfmaq";

void guess(const char* g, const char* e) {
  while(*g) {
    if(*g >= 'a' && *g <= 'z')
      f[*g - 'a'] = *e;
    g++;
    e++;
  }
}

void translate(char* g) {
  while(*g) {
    if(*g >= 'a' && *g <= 'z')
      *g = f[*g - 'a'];
    g++;
  }
}

int main() {
/*  guess("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand");
  guess("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities");
  guess("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up");
  guess("yeq", "aoz");
  printf("%s\n", f);
*/
	int T; scanf("%d\n", &T);
  char g[256];

	FOR(i,0,T) {
    gets(g);
    translate(g);
    printf("Case #%d: %s\n", i+1, g);
	}
}

