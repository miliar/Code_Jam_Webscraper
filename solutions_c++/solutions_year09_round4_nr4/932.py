#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define  INPUT_FILE_NAME "D-small-attempt2.in"
#define OUTPUT_FILE_NAME "D-small-attempt2.out"

// #define  INPUT_FILE_NAME "A-large.in"
// #define OUTPUT_FILE_NAME "A-large.out"

float dis(int x1, int y1, int r1, int x2, int y2, int r2)
{
	float ret = 0;
	
	float xx = (x2-x1)*(x2-x1);
	float yy = (y2-y1)*(y2-y1);
	ret = sqrt(xx+yy);
	
	ret += r1;
	ret += r2;

	return ret/2;
}


int main()
{
	int i,j,k,l;
	int ii,jj,kk,ll;
	FILE* fp1;
	FILE* fp2;
	int test_num;
	int len;
	float ret;
				float a1,a2,a3;
	
	char data[10000] = {0,};
	char temp[100];
	int tt[100][100];
	int t[10];
	int s[100];

	struct node* root;
	struct node* node;

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
		fscanf(fp1,"%d",&ii);

		for (j=0; j<ii; j++)
		{
			fscanf(fp1,"%d %d %d",&tt[j][0],&tt[j][1],&tt[j][2]);
		}

		if (ii == 1)
		{
			fprintf(fp2,"Case #%d: %.6f\n",i+1,(float)tt[0][2]);
		}
		else if ( ii == 2)
		{
			if (tt[0][2] >= tt[1][2])
				fprintf(fp2,"Case #%d: %.6f\n",i+1,(float)tt[0][2]);
			else fprintf(fp2,"Case #%d: %.6f\n",i+1,(float)tt[1][2]);
		}
		else if (ii==3)
		{


			a1 = dis(tt[0][0],tt[0][1],tt[0][2],tt[1][0],tt[1][1],tt[1][2]);
			a2 = dis(tt[0][0],tt[0][1],tt[0][2],tt[2][0],tt[2][1],tt[2][2]);
			a3 = dis(tt[1][0],tt[1][1],tt[1][2],tt[2][0],tt[2][1],tt[2][2]);

			if (a1 < tt[2][2]) a1 = tt[2][2];
			if (a2 < tt[1][2]) a2 = tt[1][2];
			if (a3 < tt[0][2]) a3 = tt[0][2];

			if (a1 <= a2 && a1 <= a3) 
				fprintf(fp2,"Case #%d: %.6f\n",i+1, a1);
			else if (a2 <= a1 && a2 <= a3) 
				fprintf(fp2,"Case #%d: %.6f\n",i+1, a2);
			else if (a3 <= a2 && a3 <= a1) 
				fprintf(fp2,"Case #%d: %.6f\n",i+1, a3);
		}
		else printf("error!!\n");
	}

	fclose(fp1);
	fclose(fp2);

	return 0;
}