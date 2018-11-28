#include <stdio.h>
#include <memory.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#define N 1111
long long a[N+N],cost[N];
int n,T,k,r,next[N],list[N],used[N];


inline long long sum(int l, int r) {
	if (l<=r) {
		if (l) return a[r]-a[l-1];
		else return a[r];
	} else return sum(l,n-1)+sum(0,r);
}

int main(void) {
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		scanf("%d%d%d",&r,&k,&n);
		for (int i=0;i<n;i++) {
			scanf("%lld",&a[i]);
			a[n+i] = a[i];
		}
		for (int i=1;i<n+n;i++)	a[i] += a[i-1];
		
		for (int i=0;i<n;i++) {
			int l=i,r=i+n-1,mid;
			while (l<r) {
				mid = (l+r+1)>>1;
				if (sum(i,mid)>k) r = mid-1;
				else l = mid;
			}
			next[i] = (l+1)%n;
		}
		
		int cur=0; long long ans = 0;
		bool flag = 0;
		memset(used,0,sizeof(used));
		for (int i=1;i<=r;i++)
			if (used[cur]) {
				flag = 1;
				for (int j=1;j<i;j++) cost[j] += cost[j-1];
				long long cst = cost[i-1]-cost[used[cur]-1];
				int len = i-used[cur];
				int count = (r-i)/len;
				ans += (long long) count * cst;
				i += count*len-1;
				memset(used,0,sizeof(used));
			} else {
				used[cur] = i;
				ans += sum(cur,(n+next[cur]-1)%n);
				if (!flag) cost[i] = sum(cur,(n+next[cur]-1)%n);
				cur = next[cur];
			}
		printf("Case #%d: %lld\n",_,ans);		
	}
   
	return 0;
}
