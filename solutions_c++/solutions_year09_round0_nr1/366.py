#include <stdio.h>
#include <string.h>

char word[5001][16];
char problem[10000];
char check[20][30];
int L, D, N;

int main()
{
	int i, j, wc, flag, k,ans;
	FILE *fp, *fp1;
	fp=fopen("A.in","r");
	fp1 = fopen("A.out","w");
	fscanf(fp,"%d %d %d",&L, &D, &N);
	
	for( i=0; i<D ; i++)
	{
		fscanf(fp,"%s",word[i]);
	}



	for( i=0; i<N ; i++)
	{
		fscanf(fp,"%s",problem);
		wc = 0;
		flag = 0;
		for(j=0;j<20;j++) for(k=0;k<30;k++) check[j][k] = 0;

		for (j=0; j< strlen(problem) ; j++)
		{
			if(problem[j] == '(') flag = 1;
			else if(problem[j] == ')') { wc++; flag = 0;}
			else
			{
				check[wc][ problem[j] - 'a' ] = 1;
				if (flag == 0) wc++;
			}
		}
		ans = 0;
		for ( j=0; j<D;j++)
		{
			for(k=0;k<strlen(word[j]);k++)
			{
				if(check[k][ word[j][k] - 'a' ] == 0) break;
			}
			if (k==strlen(word[j])) ans++;
		}
		fprintf(fp1, "Case #%d: %d\n", i+1, ans);
	}
	fclose(fp);

}