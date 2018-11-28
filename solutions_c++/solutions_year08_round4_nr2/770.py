#include<stdio.h>

int main()
{
	long i,j,k,l,n,m,a,CaseNum,t;
	
	long temp,z;

	scanf("%d",&t);
	CaseNum = 1;
	FILE *fp = fopen("a1.txt","w");
a1:	while (CaseNum <= t) {
		scanf("%d%d%d",&n,&m,&a);

		if (a > n*m) {
			fprintf(fp,"Case #%d: IMPOSSIBLE\n",CaseNum);
			CaseNum++;
			continue;
		}

		for (i = 0 ; i <= n ; i++)
			for (j = 0 ; j <= m ; j++) {
				for (k = i ; k <= n ; k++)
					for (l = 0 ; l <= m ; l++) {
						z = i*l - j*k;
						if (z == a || z + a == 0) {
							fprintf(fp,"Case #%d: 0 0 %d %d %d %d\n",CaseNum,i,j,k,l);
							CaseNum++;
							goto a1;
						}
					}
			}

		fprintf(fp,"Case #%d: IMPOSSIBLE\n",CaseNum);

		CaseNum++;
	}
	fclose(fp);
	return 0;
}