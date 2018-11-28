#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cctype>
using namespace std;
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define CLR(s) memset(s,0,sizeof(s))
typedef long long LL;
#define PB push_back

int nc, nd, n, ns;
char s[1111], ss[1111];

char ne[256][256];
bool op[256][256];

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	CLR(ne);
	CLR(op);
	scanf("%d", &nc);
	FOR(i,0,nc){
		scanf("%s", s);
		ne[s[0]][s[1]] = s[2];
		ne[s[1]][s[0]] = s[2];
	}
	scanf("%d", &nd);
	FOR(i,0,nd){
		scanf("%s", s);
		op[s[0]][s[1]] = true;
		op[s[1]][s[0]] = true;
	}
	scanf("%d", &n);
	scanf("%s", s);
	ns = 0;
	FOR(i,0,n){
		ss[ns++] = s[i];
		bool did = false;
		while(ns >= 2 && ne[ss[ns-2]][ss[ns-1]]){
			ss[ns-2] = ne[ss[ns-2]][ss[ns-1]];
			ns--;
			did = true;
		}
		if(!did){
			FOR(i,0,ns-1)if(op[ss[i]][ss[ns-1]]){
				ns = 0;
				break;
			}
		}
	}
	printf("Case #%d: [", ++tt);
	FOR(i,0,ns){
		if(i)printf(", ");
		printf("%c", ss[i]);
	}
	printf("]\n");
}
	return 0;
}


