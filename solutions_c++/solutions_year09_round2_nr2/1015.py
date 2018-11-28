#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INFILE	"B-small-attempt1.in"
#define OUTFILE "B-small-attempt1.out"

char line[24];
int len;

int main()
{
	FILE *fpIn = freopen(INFILE, "r", stdin);
	FILE *fpOut = fopen(OUTFILE, "w");

	int T;
	scanf("%d", &T);
	gets(line);
	for (int cnt1 = 0; cnt1 < T; cnt1++)
	{
		gets(line);
		len = strlen(line);
		int idx1 = 0;
		int flag = 0;
		for (int i = len-1; i > 0; i--){
			if (line[i] > line[i-1])
			{
				idx1 = i-1;
				flag = 1;
				break;
			}
		}

		// 不加 0 的情况：
		if (flag == 1)
		{
			int idx2 = 0;
			for (int i = len-1; i > idx1; i--){
				if (line[i] > line[idx1])
				{
					idx2 = i;
					break;
				}
			}
			char tmp;
			tmp = line[idx1];
			line[idx1] = line[idx2];
			line[idx2] = tmp;

			for (int i = idx1 + 1; i < len-1; i++){
				for (int j = idx1 + 1; j < len-1; j++)
				{
					if (line[j] > line[j+1])
					{
						tmp = line[j]; line[j] = line[j+1];  line[j+1] = tmp;
					}
				}
			}
		}
		else // 需要加 0 的情况：
		{
			char line2[24];
			int idx2 = 0;
			for (int i = len-1; i >= 0; i--)
				if (line[i] > '0')
				{
					idx2 = i;
					break;
				}
			line2[0] = line[idx2];
			line2[1] = '0';
			for (int i = 2, j = len-1; j >= 0; j--)
				if (j != idx2)
				{
					line2[i] = line[j];
					i++;
				}
			line2[len+1] = 0;
			memcpy(line, line2, len+2);
		}

		fprintf(fpOut, "Case #%d: %s\n", cnt1+1, line); 
	} // for (int cnt1 = 0; cnt1 < T; cnt1++)

	fclose(fpIn);
	fclose(fpOut);
}