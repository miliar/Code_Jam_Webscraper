#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <list>
#include <set>
#include <queue>
#include <algorithm>

using namespace std;

int main(void)
{
	FILE *fp;
	FILE *fp2;
	
	fp = fopen("C:\\B-large.in", "r+");
	fp2 = fopen("C:\\B-large.out", "w+");

	int tc;
	int t, i, j, cnt;
	char num[100];
	char num2[100];
	char num3[100];
	
	fscanf(fp, "%d", &tc);

	for(t=1; t<=tc; t++)
	{
		memset(num, 0, sizeof(num));
		memset(num2, 0, sizeof(num2));
		memset(num3, 0, sizeof(num3));
		fscanf(fp, "%s", num);
		strcpy(num2, num);
		next_permutation(num, num+strlen(num));
		if(num[0] == '0')
		{
			strcpy(num3, num);
			i = 0;
			while(num3[i]=='0')
			{
				i++;
			}
			num[0] = num3[i];
			j = 1;
			cnt = i+1;
			while(cnt--)
			{
				num[j++] = '0';
			}
			for(i=i+1;i<strlen(num3); i++)
				num[j++] = num3[i];

			num[j] = 0;
		}
		else if(strcmp(num, num2) <= 0)
		{
			strcpy(num3, num);
			memset(num, 0, sizeof(num));
			num[0] = num3[0];
			num[1] = '0';
			for(i=1; i<strlen(num3); i++)
			{
				num[i+1] = num3[i];
			}
		}
		
		fprintf(fp2, "Case #%d: %s\n", t, num);
	}
	
	return 0;
}