#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define maxn 15000
int flag[maxn],list[maxn],N,que[maxn];
int main(){
	int i,j,tem,T,zu,ans,min;
	FILE *fp1,*fp2;
	fp1 = fopen("C-large.in","r");
	fp2 = fopen("C-large.out","a");
	fscanf(fp1,"%d",&T);
	for (zu = 1; zu <= T; zu++){
		memset(flag,0,sizeof(flag));
		fscanf(fp1,"%d",&N);
		for (i = 1; i <= N; i++)
			fscanf(fp1,"%d", &list[i]);
		ans = list[1];
		for (i = 2; i <= N; i++)
			ans = ans ^list[i];
		if (ans) fprintf(fp2,"Case #%d: NO\n",zu);
		else {
			ans = 0; min = 2010001000;
			for (i = 1; i <= N; i++){
				ans +=list[i];
				if (list[i] < min) min=list[i];
			}
			fprintf(fp2,"Case #%d: %d\n",zu,ans - min);
			}
	}
	return 0;
}