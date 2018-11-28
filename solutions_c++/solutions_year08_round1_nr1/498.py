#include<stdio.h>

#define MAXN 800

int main()
{
	int i,j,n,CaseNum,t;
	long x[MAXN+1],y[MAXN+1];
	
	long temp;
	long sum;

	scanf("%d",&t);
	CaseNum = 1;
	FILE *fp = fopen("msp1.txt","w");
	while (CaseNum <= t) {
		scanf("%d",&n);
		for (i = 0 ; i < n ; i++) scanf("%ld",&x[i]);
		for (i = 0 ; i < n ; i++) scanf("%ld",&y[i]);
		
		for (i = 0 ; i < n-1 ; i++)
			for (j = i+1 ; j < n ; j++) {
				if (x[i] > x[j]) {
					temp = x[i];
					x[i] = x[j];
					x[j] = temp;
				}
				if (y[i] < y[j]) {
					temp = y[i];
					y[i] = y[j];
					y[j] = temp;
				}
			}
		sum = 0;
		for (i = 0 ; i < n ; i++) sum += x[i]*y[i];

		fprintf(fp,"Case #%d: %ld\n",CaseNum,sum);
		CaseNum++;
	}
	fclose(fp);
	return 0;
}