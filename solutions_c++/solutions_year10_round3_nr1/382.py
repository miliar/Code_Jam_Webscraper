// codelastA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#define EQUAL ==
int a[1001],b[1001];

int how_many_points(int start,int end)
{
	int sum=0;
	for(int i=start+1;i<end;i++)
	{
		if(a[start]<a[i] && b[start]>b[i])
		{
			sum++;
		}
		else if(a[start]>a[i] && b[start]<b[i])
		{
			sum++;
		}
	}
	return sum;

}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fread=fopen("E:/codejamc/A-large.in","r");
	FILE* fwrite=fopen("E:/codejamc/A-large.out","w");

	
	int case_num=0;
	int curr_case_num=0;
	int n=0;
	int num=0;
	
	int i=0,j=0;;

	fscanf(fread,"%d\n",&case_num);

	for(curr_case_num=0;curr_case_num<case_num;curr_case_num++)
	{
		
		if(fscanf(fread,"%d\n ",&n) EQUAL EOF)
		{
			break;
		}
		
		for(i=0;i< n;i++)
		{
			if(fscanf(fread,"%d ",&a[i]) EQUAL EOF
				||fscanf(fread,"%d\n",&b[i]) EQUAL EOF)
			{
				break;
			}

		}


		num=0;
		for(j=0;j<i-1;j++)
		{
			num+=how_many_points(j,i);
		}

		//done read a case


		
		
		fprintf(fwrite,"Case #%d: %d\n",curr_case_num+1,num);

		continue;




	}







	


	
	fclose(fread);
	fclose(fwrite);
	return 0;
}

