#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// #define  INPUT_FILE_NAME "B-small-attempt1.in"
// #define OUTPUT_FILE_NAME "B-small-attempt1.out"

#define  INPUT_FILE_NAME "B-large.in"
#define OUTPUT_FILE_NAME "B-large.out"

int main()
{
	int i,j,k,l;
	int ii,jj,kk,ll;
	FILE* fp1;
	FILE* fp2;
	int test_num;
	int len;
	
	char data[100] = {0,};
	int t[10];
	int s[100];
	
	// read data
	fp1 = fopen(INPUT_FILE_NAME,"r");
	fp2 = fopen(OUTPUT_FILE_NAME,"w+");
	if (fp1 == NULL || fp2 == NULL) 
	{
		printf("file open error\n");
		return -1;
	}

	fscanf(fp1,"%d",&test_num);

	for (i=0;i<test_num;i++)
	{
		memset(data,0,100);
		fscanf(fp1,"%s",data);

		len = strlen(data);
		for(j=0;j<10;j++) t[j] = 0;
		for(j=0;j<100;j++) s[j] = 0;

		for (j=1;j<len;j++)
		{
			if (data[j-1] < data[j]) break;
		}
		if(j == len) 
		{
			fprintf(fp2,"Case #%d: ",i+1);
			for (j=0;j<len;j++)
				s[data[j]-'0']++;
			for (j=1;j<10;j++)
			{
				if (s[j] >0)
				{
					fprintf(fp2,"%c",j+'0');
					s[j]--;
					break;
				}
			}
			
			fprintf(fp2,"0");

			for (j=0;j<10;j++)
			{
				while (s[j] >0)
				{
					fprintf(fp2,"%c",j+'0');
					s[j]--;
				}
			}
			fprintf(fp2,"\n");
			continue;
		}
		


		
		k=0;
		for (j=len-1; j>=0; j--)
		{
			t[data[j]-'0']++;
			s[k] = data[j]-'0';
			for(l=0;l<k;l++)
			{
				if (s[k] < s[l])
				{
					data[j] = s[l] + '0';
					t[s[l]]--;
					for (jj=0; jj<10; jj++)
					{
						while(t[jj] >0)
						{
							t[jj]--;
							j++;
							data[j] = jj + '0';
						}
					}
					fprintf(fp2,"Case #%d: %s\n",i+1, data);
					l=k+1;
					j=-1;
				}
			}
			k++;
		}
		if (j==0)
		{
			fprintf(fp2,"!!!!!!!!!Case #%d: %s\n",i+1, data);
		}
	}

	fclose(fp1);
	fclose(fp2);

	return 0;
}