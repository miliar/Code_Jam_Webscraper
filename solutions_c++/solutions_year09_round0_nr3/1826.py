#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define  INPUT_FILE_NAME "C-small-attempt0.in"
#define OUTPUT_FILE_NAME "C-small-attempt0.out"

// #define  INPUT_FILE_NAME "C-large.in"
// #define OUTPUT_FILE_NAME "C-large.out"

int  result;

void findWelcome(char* msg, char* wel)
{
	if (*wel == 0)
	{
		result++;
		return;
	}
	if (*msg == 0) return;
	
	if (*msg != *wel) findWelcome(msg+1,wel);
	else 
	{
		findWelcome(msg+1,wel+1);
		if (msg[1] != 0) findWelcome(msg+1,wel);
	}
}

int main()
{
	int i;
	FILE* fp1;
	FILE* fp2;
	int test_num;

	char data[30] = "welcome to code jam";
	char testdata[600] = {0,};

	// read data
	fp1 = fopen(INPUT_FILE_NAME,"r");
	fp2 = fopen(OUTPUT_FILE_NAME,"w+");
	if (fp1 == NULL || fp2 == NULL) 
	{
		printf("file open error\n");
		return -1;
	}

	fgets(testdata,550,fp1);
	test_num = atoi(testdata);

	for (i=0; i<test_num; i++)
	{
		memset(testdata,0,600);
		fgets(testdata,550,fp1);
		testdata[strlen(testdata)-1] = 0;

		result = 0;

		findWelcome(testdata,data);

		// write answer
		fprintf(fp2,"Case #%d: %04d\n",i+1,result);
	}
	
	fclose(fp1);
	fclose(fp2);

	return 0;
}