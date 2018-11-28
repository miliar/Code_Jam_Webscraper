#include <stdio.h>
#define MAXN 1060

int n;
int s[MAXN];

const int inf=1000000000;

int main(void)
{
	int t,casenum=1;
	int i,min,xr,sum;
	scanf("%d",&t);
	while(t--) {
		scanf("%d",&n);
		xr=0;
		min=inf;
		sum=0;
		for(i=0;i<n;i++) {
			scanf("%d",s+i);
			xr^=s[i];
			sum+=s[i];
			if(s[i]<min) min=s[i];
		}
		printf("Case #%d: ",casenum++);
		if(xr!=0) printf("NO\n");
		else printf("%d\n",sum-min);
	}
}
