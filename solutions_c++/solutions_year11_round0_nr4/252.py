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

int nn, n;
int a[11111]; bool v[11111];

int main() {
int nt, tt=0; scanf("%d", &nt); while(nt--){
	scanf("%d", &n);
	FOR(i,0,n){
		scanf("%d", &a[i]);a[i]--;
		v[i] = false;
	}
	int ans = 0;
	FOR(i,0,n)if(!v[i]){
		int c = i, k = 0;
		while(!v[c]){
			v[c] = true;
			c = a[c];
			k++;
		}
		//printf(" k = %d\n", k);
		if(k > 1) ans += k;
	}
	printf("Case #%d: %d.000000\n", ++tt, ans);
}
	return 0;
}


