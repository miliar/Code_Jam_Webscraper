#include <stdio.h>
#include <iostream>
#include <math.h>
using namespace std;

int main() {
	int t,n,m;
	FILE *fp1, *fp2;
	char ca[50][50];
	fp1 = fopen("C:\\Users\\zerosumi\\Project\\gcj2010\\Debug\\C-large.in", "r");
	fp2 = fopen("C:\\Users\\zerosumi\\Project\\gcj2010\\Debug\\a.out.txt", "w+");

	int srn = 0,mkn = 0,createnum = 0;
	char srstr[1000][100],mkstr[100][100];
	fscanf(fp1, "%d", &t);
	char stemp[1000];
	for (int i = 1; i <= t; i++)
	{
		srn = 0;mkn = 0;createnum = 0;
		fscanf(fp1, "%d %d", &n, &m);
		for (int j = 1; j <= n; j++)
		{
			fscanf(fp1, "%s", &stemp);
			for (int k = 1;stemp[k]!='\0';k++)
			{
				if (stemp[k] == '/')
				{
					strncpy(srstr[srn], stemp, k);
					srstr[srn++][k] = '\0';
				}
			}
			strcpy(srstr[srn++], stemp);
		}
		for (int j = 1; j <= m; j++)
		{
			fscanf(fp1, "%s", &stemp);
			for (int k = 1;stemp[k]!='\0';k++)
			{
				if (stemp[k] == '/')
				{
					strncpy(mkstr[mkn], stemp, k);
					mkstr[mkn++][k] = '\0';
				}
			}
			strcpy(mkstr[mkn++], stemp);
		}
		for (int j = 0; j < mkn; j++)
		{
			int existflag = 0;
			for (int k = 0; k < srn; k++)
			{
				if (strcmp(mkstr[j],srstr[k]) == 0) {
					existflag = 1;
					break;
				}
			}
			if (existflag == 0)
			{
				createnum ++;
				strcpy( srstr[srn++], mkstr[j]);
			}
		}
		fprintf(fp2, "Case #%d: %d\n", i, createnum);
	}
}