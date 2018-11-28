#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//#define  INPUT_FILE_NAME "A-small-attempt0.in"
//#define OUTPUT_FILE_NAME "A-small-attempt0.out"

 #define  INPUT_FILE_NAME "A-large.in"
 #define OUTPUT_FILE_NAME "A-large.out"

int main()
{
	int i,j,k,l;
	FILE *fp;
	int msg_len, code_len, test_len;
	int count1, count2;
	char flag2;

	char data[6000][20] = {0,};
	char testdata[600][500] = {0,};
	short result[6000] = {0,};
	char temp[600][20][50] = {0,};

	// read data
	fp = fopen(INPUT_FILE_NAME,"r");
	if (fp == NULL) return -1;

	fscanf(fp,"%d %d %d",&msg_len,&code_len,&test_len);

	for (i=0;i<code_len;i++)
	{
		fscanf(fp,"%s",data[i]);
	}

	for (i=0;i<test_len;i++)
	{
		fscanf(fp,"%s",testdata[i]);
	}
	fclose(fp);

	// data process
	for (i=0; i<test_len; i++)
	{
		count1 = 0;
		count2 = 0;
		for (j=0; j<(int)strlen(testdata[i]); j++)
		{
			if (testdata[i][j] != '(')
			{
				temp[i][count1][count2] = testdata[i][j];
				temp[i][count1][count2+1] = '\0';
				count1++;
				count2 = 0;
			}
			else
			{
				j++;
				while (testdata[i][j] != ')')
				{
					temp[i][count1][count2] = testdata[i][j];
					j++;
					count2++;
				}
				temp[i][count1][count2] = '\0';
				count1++;
				count2 = 0;
			}
		}
	}

	for (i=0; i<test_len; i++)
	{
		//decode
		for (j=0; j<code_len; j++)
		{
			for (k=0;k<msg_len;k++)
			{
				flag2 = 0;
				for (l=0; l<(int)strlen(temp[i][k]); l++)
				{
					if (temp[i][k][l] == data[j][k])
					{
						flag2 = 1;
						break;
					}
				}
				if (flag2 == 0) break;
			}
			if (flag2 == 1) result[i]++; 
		}
	}

	// write answer
	fp = fopen(OUTPUT_FILE_NAME,"w+");
	if (fp == NULL) return -1;
	
	for (i=0;i<test_len;i++)
	{
		fprintf(fp,"Case #%d: %d\n",i+1,result[i]);
	}
	fclose(fp);

	return 0;
}