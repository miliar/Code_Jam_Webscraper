#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//#define  INPUT_FILE_NAME "B-small-attempt0.in"
//#define OUTPUT_FILE_NAME "B-small-attempt0.out"

//#define  INPUT_FILE_NAME "test.in"
//#define OUTPUT_FILE_NAME "test.out"

#define  INPUT_FILE_NAME "B-large.in"
#define OUTPUT_FILE_NAME "B-large.out"

int main()
{
	int i,j=0,k,l,m,n,jj;
	char name[1000][100];
	int data[1000][2];
	int num[1000];
	char in[1000];
	char ins[1000];
	FILE *fp;
	FILE *wfp;
	int test_len;
	int tt,tr,tb;
	int dir1,dir2,dirp;
	int fr=0,fb=0;
	int count=1;
	double test;
	
	// read data
	fp = fopen(INPUT_FILE_NAME,"r");
	if (fp == NULL) return -1;

	wfp = fopen(OUTPUT_FILE_NAME,"w+");
	if (wfp == NULL) return -1;
	
	fscanf(fp,"%d",&test_len);

	for (i=0;i<test_len;i++)
	{
		count=0;
		fscanf(fp,"%d %d %d",&l,&m,&n);

		for (j=1; j<1000; j++)
		{
			test=pow(n,j);
			if (test * l >= m) break;
		}

		for (jj=0; jj<1000; jj++)
		{
			test=pow(2,jj);
			if (test >=j) break;
		}
		fprintf(wfp,"Case #%d: %d\n",i+1,jj);
	}

	fclose(fp);
	fclose(wfp);
	
	return 0;
}