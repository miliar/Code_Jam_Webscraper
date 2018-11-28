
#include <cstdio>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

char buf[105], re[105];
int c,d,x, resz;

map<pair<char,char>,char> com;
set<pair<char,char> > opp;

pair<char,char> mp(char a, char b) {
	if (a>b) swap(a,b);
	return make_pair(a,b);
}

main() {
	int ntc;
	scanf("%d", &ntc);
	for (int test=1; test<=ntc; test++) {
		//printf("----------- case %d\n", test);
	
		scanf("%d", &c);
		com.clear();
		for (int i=0; i<c; i++) {
			scanf("%s", buf);
			com[mp(buf[0],buf[1])]=buf[2];
		}
		
		scanf("%d", &d);
		opp.clear();
		for (int i=0; i<d; i++) {
			scanf("%s", buf);
			opp.insert(mp(buf[0],buf[1]));
		}
		scanf("%d%s", &x, buf);
		
		resz=0;
		for (int i=0; i<x; i++) {
			char a=buf[i];
			re[resz++]=a;
			if (resz>1 && com.find(mp(re[resz-2],re[resz-1]))!=com.end()) {
				char r=com[mp(re[resz-2],re[resz-1])];
				resz--;
				re[resz-1]=r;
			} else {
				for (int p=0; p<resz-1; p++) {
					if (opp.find(mp(re[p],a))!=opp.end())
						resz=0;
				}
			}
			//printf("   add %c: %s\n", a, re);
		}
		
		printf("Case #%d: [", test);
		for (int e=0; e<resz; e++) {
			if (e>0) printf(", ");
			printf("%c", re[e]);
		}
		printf("]\n");
	}
}
