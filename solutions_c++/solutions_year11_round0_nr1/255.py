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

int n;
int ap[1111]; char ac[1111];
int ta[1111], tb[1111];
bool tk[1111];

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d", &n);
	FOR(i,0,n){
		scanf("%s%d", ac+i, &ap[i]);
	}
	int ca = 1, cb = 1;
	for(int i=n-1; i>=0; i--){
		if(ac[i]=='O'){
			ca = ap[i];
			tk[i] = true;
		}else{
			cb = ap[i];
			tk[i] = false;
		}
		ta[i]=ca; tb[i] = cb;
		//printf(" %d : %d %d\n", tk[i]?1:0, ca, cb);
	}
	ca = 1; cb = 1;
	int ans = 0;
	FOR(i,0,n){
		int ns;
		if(tk[i]) ns = abs(ca - ta[i])+1;
		else  ns = abs(cb - tb[i])+1;
		if(ca > ta[i]){
			ca = max(ca-ns, ta[i]);
		}else{
			ca = min(ca+ns, ta[i]);
		}
		if(cb > tb[i]){
			cb = max(cb-ns, tb[i]);
		}else{
			cb = min(cb+ns, tb[i]);
		}
		ans += ns;
	}
	printf("Case #%d: %d\n", ++tt, ans);
}
	return 0;
}


