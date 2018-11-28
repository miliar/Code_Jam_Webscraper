#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

//#define  INPUT_FILE_NAME "A-small-attempt1.in"
//#define OUTPUT_FILE_NAME "A-small-attempt1.out"

//#define  INPUT_FILE_NAME "test.in"
//#define OUTPUT_FILE_NAME "test.out"

#define  INPUT_FILE_NAME "A-large.in"
#define OUTPUT_FILE_NAME "A-large.out"

int main()
{
	int i,j=0,k,l;
	FILE *fp;
	FILE *wfp;
	int test_len;
	
	// read data
	fp = fopen(INPUT_FILE_NAME,"r");
	if (fp == NULL) return -1;

	wfp = fopen(OUTPUT_FILE_NAME,"w+");
	if (wfp == NULL) return -1;
	
	fscanf(fp,"%d",&test_len);

	for (i=0;i<test_len;i++)
	{
		fscanf(fp,"%d %d",&k, &l);
		if ((l % ((int)pow(2.0,k))) == ((int)pow(2.0,k) - 1))
			fprintf(wfp,"Case #%d: ON\n",i+1);
		else
			fprintf(wfp,"Case #%d: OFF\n",i+1);
	}

	fclose(fp);
	fclose(wfp);
	
	return 0;
}