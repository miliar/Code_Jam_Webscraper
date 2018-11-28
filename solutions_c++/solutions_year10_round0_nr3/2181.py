#include <stdio.h>
#include <memory.h>
//#define __int64 long long

int r,n;
__int64 data[1007];

int main()
{
	int t,j,h,now,round,T=0;
	__int64 money,cnt,k;

	freopen("C-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	for(scanf("%d",&t);t;t--) {
		scanf("%d %I64d %d",&r,&k,&n);
		for(j=0;j<n;j++) scanf("%I64d",&data[j]);
		h=0,now=0; round=0; money=0;cnt=0;
		do {
			if(cnt+data[h]<=k) {
				cnt+=data[h];
				h=(h+1)%n; 
				
				if(h==now) {
					round++; money+=cnt;
					cnt=0; now=h;
				}
			}
			else {
				round++; money+=cnt;
				cnt=0; now=h;
			}
		} while(round<r);

		printf("Case #%d: %I64d\n",++T,money);
	}
	return 0;
}