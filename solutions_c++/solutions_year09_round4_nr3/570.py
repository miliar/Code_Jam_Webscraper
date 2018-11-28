#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <string.h>
#include <memory.h>
#define N 1111
long ntests,a[N][N],b[N],can[N][N],u[N],qual[N],pointer[N];


inline void swap(long& a, long& b) {
	long t = a;
	a = b;
	b = t;
}

int main(void) {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	srand(time(NULL));

	scanf("%d\n",&ntests);
	for (long _=1;_<=ntests;_++) {
		long n,k;
		memset(a,0,sizeof(a));
		memset(can,0,sizeof(can));
		memset(b,0,sizeof(b));
		memset(qual,0,sizeof(qual));
	        scanf("%d%d\n",&n,&k);
		for (long i=1;i<=n;i++) {
			for (long j=1;j<=k;j++) scanf("%d",&a[j][i]);
			scanf("\n");
		}

		for (long i=1;i<=n;i++) {
			for (long j=1;j<=n;j++) {
				if (i==j) {
					can[i][i] = 0;
					continue;
				}
				can[i][j] = 1;
				qual[i]++; qual[j]++;
				for (long q=1;q<=k;q++) {
					if (a[q][i]==a[q][j] || (q!=k && a[q][i]<a[q][j] && a[q+1][i]>a[q+1][j]) || (q!=k && a[q][i]>a[q][j] && a[q+1][i]<a[q+1][j])) {
						can[i][j] = 0;
						qual[i]--; qual[j]--;
						break; 
					}
				}
			}
		}
		long ANS = n+n;
		for (long i=1;i<=n;i++) b[i] = i;

                for (long __=1;__<=100;__++) {
		memset(u,0,sizeof(u));
		for (long i=1;i<=n+n+n;i++) swap(b[1+(rand()%n)],b[1+(rand()%n)]);
		
		long ans = 0;
		for (long i=1;i<=n;i++) 
			if (!u[i]) {
                        	u[i] = i;
                        	ans++;
                        	for (long j=i+1;j<=n;j++)
                        		if (!u[j]) {
                        			long f = 1;
                        			for (long k=i;k<j;k++)
                        				if (u[k]==i)
                        					if (!can[b[k]][b[j]]) { 
                        						f = 0;
                        						break;
                        					}
						if (f==1) u[j] = i;
                        		} 			
			}
			ANS <?= ans;
		}

		printf("Case #%d: %d\n",_,ANS);
	}

	return 0;
}
