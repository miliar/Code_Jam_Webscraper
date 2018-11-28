#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <memory.h>
#include <queue>
#include <vector>
#include <math.h>
int o_o;
#define N 111
int n,a[N],b[N];

int main(void) {
	freopen(".in","r",stdin);
	freopen(".out","w",stdout);
	
	scanf("%d",&o_o);
	for (int O_o=1;O_o<=o_o;O_o++) {
	      	scanf("%d",&n);
	      	int k = n-1,size=0,ans=0;
	      	int lim = 1<<k;
	      	for (int msk=0;msk<lim;msk++) {
	      		size = 0;
	      		memset(a,0,sizeof(a));
	      		for (int j=0;j<k;j++)
	      			if (msk&(1<<j)) {
	      				a[++size] = j+2;
	      			}
			memset(b,0,sizeof(b));
			
			for (int i=1;i<=size;i++)
				b[a[i]] = i;
		
			if (!b[n]) continue;

		bool flag = 1;
		int cur = n;
		while (cur!=1) {
			cur = b[cur];
			if (!b[cur]) break;
		}

		if (cur==1) ans = (ans+1)%100003;
		
		}

		printf("Case #%d: %d\n",O_o,ans);
	}

	return 0;
} 
