#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <math.h>
#include <ctype.h>

#define rep(i,n) for(int i=0;i<n;i++)
#define fori(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define ma(a,b) (a>b?a:b)
#define mi(a,b) (a<b?a:b)
#define foreach(it,arr) for(__typeof((arr).begin())it=(arr).begin();it!=(arr).end();it++)
#define foreachd(it,arr) for(__typeof((arr).begin())it=(arr).rbegin();it!=(arr).rend();it++)

typedef long long LL;

using namespace std;
int tc,pd,pg;
LL n;
int main () {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tc);
	fori(t,1,tc){
		scanf("%lld %d %d", &n, &pd, &pg);
		if(pg == 100 && pd != 100){
			printf("Case #%d: %s\n", t, "Broken");
			continue;
		}
		if(pg == 0 && pd == 0){
			printf("Case #%d: %s\n", t, "Possible");
			continue;
		}
		if(pg == 0 && pd > 0){
			printf("Case #%d: %s\n", t, "Broken");
			continue;
		}
		bool ok = false;
		if(n>100) n = 100;
		fori(i,1,n){
			int ra = i * pd;
			if(ra % 100 == 0){
//				int j = i;
//				while(1){
//					int rb = j * pg;
//					if(rb % 100 == 0 && rb >= ra){
//						ok = true;
//						break;
//					}
//					j++;
//				}
//				if(ok) 
				ok=true;
				break;
			}
		}
		printf("Case #%d: %s\n", t, (ok ? "Possible": "Broken"));
	}
    return 0;
}
