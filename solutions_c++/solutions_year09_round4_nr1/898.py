#include <stdio.h>
#include <algorithm>
#include <string.h>
#include <memory.h>
#define N 1111
long ntests,n,a[N];

inline void swap(long& a, long& b) {
	long t = a;
	a = b;
	b = t;
}

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	
	scanf("%d\n",&ntests);
	for (long _=1;_<=ntests;_++) {
		memset(a,0,sizeof(a));
                scanf("%d\n",&n);
                for (long i=1;i<=n;i++) {
                	for (long j=1;j<=n;j++) {
                		char c;
                		scanf("%c",&c);
                		if (c=='1') a[i] = j;
                	}
                	scanf("\n");
                }
	
	        long ans = 0;
                for (long I=1;I<=n;I++) {
                for (long j=n;j;j--) {
                	if (a[j]>j) {
                		long nw = 0;
                		for (long k=j+1;k<=n;k++)
                			if (a[k]<=j) {
                				nw = k;
                				break;	
                			}
				for (long k=nw;k>j;k--) {
					swap(a[k],a[k-1]);
					ans++;
				}				
                	}
                }                
                }

		printf("Case #%d: %d\n",_,ans);
	}

	return 0;
}
