#include <stdio.h>
#define max(a,b) (((a)>(b))?(a):(b))
int n,x[1002];

int main()
{
	int t,T,i,j,m,p,r,best,a,b;
	
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	
	scanf("%d",&T);
	
	for(t=1; t<=T; ++t) {
		scanf("%d",&n);
		
		for(i=0;i<n;++i)
			scanf("%d",&x[i]);
			
		m = (1<<n)-1;
		
		for(best=-1,i=1;i<m;++i) {
			for(r=0,p=0,a=0,b=0,j=0;j<n;++j) {
				if(i & (1<<j)) {r ^= x[j]; a += x[j];}
				else {p ^= x[j]; b += x[j];}
			}
			
			if(p == r) best = max(best, max(a,b));;
		}
		
		if(best == -1) printf("Case #%d: NO\n",t);
		else printf("Case #%d: %d\n",t,best);
	}
}

