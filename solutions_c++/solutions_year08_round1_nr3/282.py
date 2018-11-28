#include<stdio.h>

#define MAXN 100000
#define a 5.2360679775

int main()
{
	int i,j,n,CaseNum,t;
	long x[MAXN+1],y[MAXN+1];

	
	long temp;
	char ans[5];

	scanf("%d",&t);
	CaseNum = 1;
	FILE *fp = fopen("msp2.txt","w");
	while (CaseNum <= t) {
		scanf("%d",&n);
		FILE *fp1 = fopen("a.txt","r");
		for (i = 2 ; i <= n ; i++) fscanf(fp1,"%s",ans);
	
		fprintf(fp,"Case #%d: %s\n",CaseNum,ans);
		fclose(fp1);
		CaseNum++;
	}
	fclose(fp);
	return 0;
}