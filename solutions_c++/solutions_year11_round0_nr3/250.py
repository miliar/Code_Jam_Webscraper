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

int x, mi, su, n;

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d", &n);
	su = 0;
	mi = 2147483647;
	x = 0;
	FOR(i,0,n){
		int a;
		scanf("%d", &a);
		su += a;
		mi = min(mi, a);
		x ^= a;
	}
	printf("Case #%d: ", ++tt);
	if(x==0)printf("%d\n", su - mi); else printf("NO\n");
}
	return 0;
}


