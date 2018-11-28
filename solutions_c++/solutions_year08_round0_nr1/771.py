#include<stdio.h>
#include<string.h>

#define MAXS 100
#define MAXL 100
int main()
{
	int i,j,k,n,CaseNum,s,q,ans;
	char EngineName[MAXS+1][MAXL+2];
	char query[MAXL+2];
	short covered[MAXS+1];
	int tot;
	scanf("%d",&n);
	CaseNum = 1;
	FILE *fp = fopen("ans2.txt","w");
	while (CaseNum <= n) {
		scanf("%d",&s);
		for (i = 0 ; i < s ; i++) {
			gets(EngineName[i]);
			covered[i] = 0;
			if (!strcmp(EngineName[i],"")) i--;
		}
		scanf("%d",&q);
		ans = 0;
		tot = 0;
		for (i = 0 ; i < q ; i++) {
			gets(query);
			if (!strcmp(query,"")) { i--; continue; }
			for (j = 0 ; j < s ; j++) {
				if (!strcmp(EngineName[j],query)) {
					if (!covered[j]) {
						tot++;
						if (tot >= s) {
							ans++;
							tot = 1;
							for (k = 0 ; k < s ; k++) covered[k] = 0;
						}
						covered[j] = 1;
					}
				}
			}
		}

		fprintf(fp,"Case #%d: %d\n",CaseNum,ans);
		CaseNum++;
	}
	fclose(fp);
	return 0;
}