#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//#define  INPUT_FILE_NAME "A-small-attempt0.in"
//#define OUTPUT_FILE_NAME "A-small-attempt0.out"

//#define  INPUT_FILE_NAME "test.in"
//#define OUTPUT_FILE_NAME "test.out"

#define  INPUT_FILE_NAME "A-large.in"
#define OUTPUT_FILE_NAME "A-large.out"

int main()
{
	int i,j=0,jj,k,l;
	char box[100][100];
	char rotate[100][100];
	FILE *fp;
	FILE *wfp;
	int test_len;
	int tt,tr,tb;
	int fr=0,fb=0;
	
	// read data
	fp = fopen(INPUT_FILE_NAME,"r");
	if (fp == NULL) return -1;

	wfp = fopen(OUTPUT_FILE_NAME,"w+");
	if (wfp == NULL) return -1;
	
	fscanf(fp,"%d",&test_len);

	for (i=0;i<test_len;i++)
	{
		fscanf(fp,"%d %d",&k, &l);
		for (j=0; j<k; j++)
		{
			fscanf(fp,"%s",box[j]);
		}
		for (j=0; j<k; j++)
		{
			for(jj=0;jj<k; jj++)
			{
				rotate[jj][k-j-1] = box[j][jj];
			}
		}
		for (j=0; j<k; j++)
		{
			tt=k-1;
			for (jj=0; jj<k; jj++)
			{
				if (rotate[k-jj-1][j]!='.') 
				{
					if (tt!=k-jj-1)
					{
						rotate[tt][j]=rotate[k-jj-1][j];
						rotate[k-jj-1][j]='.';
					}
					tt--;
				}
			}
		}
//		for (j=0;j<k;j++)
//		{
//			for(jj=0;jj<k;jj++)
//			{
//				printf("%c",rotate[j][jj]);
//			}
//			printf("\n");
//		}
		fr=0;
		fb=0;

		for (j=0;j<k;j++)
		{
			tr=0;
			tb=0;
			for(jj=0;jj<k;jj++)
			{
				if (rotate[j][jj]=='R')
				{
					tr++;
					tb=0;
					if (tr>=l) fr=1;
				}
				else if (rotate[j][jj]=='B')
				{
					tb++;
					tr=0;
					if (tb>=l) fb=1;
				}
				else
				{
					tr=0;
					tb=0;
				}
			}
		}

		for (j=0;j<k;j++)
		{
			tr=0;
			tb=0;
			for(jj=0;jj<k;jj++)
			{
				if (rotate[jj][j]=='R')
				{
					tr++;
					tb=0;
					if (tr>=l) fr=1;
				}
				else if (rotate[jj][j]=='B')
				{
					tb++;
					tr=0;
					if (tb>=l) fb=1;
				}
				else
				{
					tr=0;
					tb=0;
				}
			}
		}

		for (j=0;j<k;j++)
		{
			tr=0;
			tb=0;
			for(jj=0;jj<k-j;jj++)
			{
				if (rotate[jj][jj+j]=='R')
				{
					tr++;
					tb=0;
					if (tr>=l) fr=1;
				}
				else if (rotate[jj][jj+j]=='B')
				{
					tb++;
					tr=0;
					if (tb>=l) fb=1;
				}
				else
				{
					tr=0;
					tb=0;
				}
			}
		}

		for (j=1;j<k;j++)
		{
			tr=0;
			tb=0;
			for(jj=0;jj<k-j;jj++)
			{
				if (rotate[jj+j][jj]=='R')
				{
					tr++;
					tb=0;
					if (tr>=l) fr=1;
				}
				else if (rotate[jj+j][jj]=='B')
				{
					tb++;
					tr=0;
					if (tb>=l) fb=1;
				}
				else
				{
					tr=0;
					tb=0;
				}
			}
		}

		for (j=0;j<k;j++)
		{
			tr=0;
			tb=0;
			for(jj=0;jj<k-j;jj++)
			{
				if (rotate[k-jj-1][jj+j]=='R')
				{
					tr++;
					tb=0;
					if (tr>=l) fr=1;
				}
				else if (rotate[k-jj-1][jj+j]=='B')
				{
					tb++;
					tr=0;
					if (tb>=l) fb=1;
				}
				else
				{
					tr=0;
					tb=0;
				}
			}
		}

		for (j=1;j<k;j++)
		{
			tr=0;
			tb=0;
			for(jj=0;jj<k-j;jj++)
			{
				if (rotate[k-jj-j-1][jj]=='R')
				{
					tr++;
					tb=0;
					if (tr>=l) fr=1;
				}
				else if (rotate[k-jj-j-1][jj]=='B')
				{
					tb++;
					tr=0;
					if (tb>=l) fb=1;
				}
				else
				{
					tr=0;
					tb=0;
				}
			}
		}

		if ((fr==1) && (fb==1))
			fprintf(wfp,"Case #%d: Both\n",i+1);
		else if ((fr==0) && (fb==0))
			fprintf(wfp,"Case #%d: Neither\n",i+1);
		else if ((fr==0) && (fb==1))
			fprintf(wfp,"Case #%d: Blue\n",i+1);
		else if ((fr==1) && (fb==0))
			fprintf(wfp,"Case #%d: Red\n",i+1);
	}

	fclose(fp);
	fclose(wfp);
	
	return 0;
}