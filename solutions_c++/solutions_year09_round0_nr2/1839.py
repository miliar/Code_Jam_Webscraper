#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// #define  INPUT_FILE_NAME "B-small-attempt0.in"
// #define OUTPUT_FILE_NAME "B-small-attempt0.out"

#define  INPUT_FILE_NAME "B-large.in"
#define OUTPUT_FILE_NAME "B-large.out"

int main()
{
	int i,j,k;
	FILE* fp1;
	FILE* fp2;
	int test_num;
	int x,y;
	int tx,ty;
	int count;
	int next, nextd, nextc;
	
	int data[100][100] = {0,};
	char result[100][100] = {0,};
	

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
		fscanf(fp1,"%d %d",&x,&y);

		for (j=0; j<x; j++)
		{
			for (k=0; k<y; k++)
			{
				fscanf(fp1,"%d",&(data[j][k]));
				result[j][k] = 0;
			}
		}

		count = 0;
		result[0][0] = 'a';
		for (j=0; j<x; j++)
		{
			for (k=0; k<y; k++)
			{
				if ((j || k) && result[j][k] != 0) continue;
				
				
				tx = j;
				ty = k;
				nextc = 0;

				while(1)
				{
					next = data[tx][ty];
					nextd = 0;

					// direction
					if (tx != 0)
					{
						if (next > data[tx-1][ty])
						{
							nextd = 1;
							next = data[tx-1][ty];
						}
					}
					if (ty != 0)
					{
						if (next > data[tx][ty-1])
						{
							nextd = 2;
							next = data[tx][ty-1];
						}
					}
					if (ty + 1 < y)
					{
						if (next > data[tx][ty+1])
						{
							nextd = 3;
							next = data[tx][ty+1];
						}
					}
					if (tx + 1 < x)
					{
						if (next > data[tx+1][ty])
						{
							nextd = 4;
							next = data[tx+1][ty];
						}
					}

					if (nextd == 0) break;

					if (nextd == 1) tx--;
					else if (nextd == 2) ty--;
					else if (nextd == 3) ty++;
					else if (nextd == 4) tx++;
					else printf("error!!\n");

					if (result[tx][ty] != 0)
					{
						nextc = result[tx][ty];
						break;
					}

				}

				tx = j;
				ty = k;

				if (nextc == 0)
				{
					nextc = count + 'a';
					count++;
				}
				
				result[tx][ty] = nextc;
				
				while(1)
				{
					next = data[tx][ty];
					nextd = 0;
					
					// direction
					if (tx != 0)
					{
						if (next > data[tx-1][ty])
						{
							nextd = 1;
							next = data[tx-1][ty];
						}
					}
					if (ty != 0)
					{
						if (next > data[tx][ty-1])
						{
							nextd = 2;
							next = data[tx][ty-1];
						}
					}
					if (ty + 1 < y)
					{
						if (next > data[tx][ty+1])
						{
							nextd = 3;
							next = data[tx][ty+1];
						}
					}
					if (tx + 1 < x)
					{
						if (next > data[tx+1][ty])
						{
							nextd = 4;
							next = data[tx+1][ty];
						}
					}
					
					if (nextd == 0) break;
					
					if (nextd == 1) tx--;
					else if (nextd == 2) ty--;
					else if (nextd == 3) ty++;
					else if (nextd == 4) tx++;
					else printf("error!!\n");
					
					if (result[tx][ty] != 0)
					{
						break;
					}
					
					result[tx][ty] = nextc;
				}
			}
		}

		fprintf(fp2,"Case #%d:\n",i+1);
		for (j=0; j<x; j++)
		{
			for (k=0; k<y; k++)
			{
				fprintf(fp2,"%c",result[j][k]);
				if (k+1 < y) fprintf(fp2," ");
			}
			fprintf(fp2,"\n");
		}
	}

	fclose(fp1);
	fclose(fp2);

	return 0;
}