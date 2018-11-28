#include <stdio.h>
#include <memory.h>

int su,k;

int main()
{
	int t,n,work[55],cnt,T=0;
	bool s;

	freopen("A-large.in","rt",stdin);
	freopen("output.txt","wt",stdout);
	for(scanf("%d",&t);t;t--) {
		scanf("%d %d",&su,&k);
		cnt=0; n=k;
		memset(work,0,sizeof(work));
		while(n && cnt<=su) { work[cnt++]=n%2; n/=2; }
		s=1;
		for(n=0;n<su;n++) s=(s&&work[n]);
		printf("Case #%d: ",++T);
		if(s==1) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}
