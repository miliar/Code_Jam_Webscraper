#include <iostream>
#include <cmath>
using namespace std;
#define inf 70000006
int c[1005];
int main()
{
	freopen("D:\\C-large.in","r",stdin);
	freopen("D:\\C-large.out","w",stdout);
	int T,n,cnt=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		int ans = inf,res = 0;
		for(int i= 0 ; i < n ; i++) {
			scanf("%d",&c[i]);
			if(c[i] < ans) ans = c[i];
			res += c[i];
		}
		int sum = c[0];
		for(int i = 1 ; i < n ; i ++) {
			sum ^= c[i];
		}
		if(sum != 0) printf("Case #%d: NO\n",++cnt);
		else printf("Case #%d: %d\n",++cnt,res - ans);
	}
	return 0;
}