// codelastC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "math.h"
#define EQUAL ==

__int64 cal(__int64 a,__int64 x)
{
	if(x EQUAL 0)
	{
		return 1;
	}
	__int64 n=a;

	for(int i=0;i<x-1;i++)
	{
		n*=a;
	}

	return n;

}
int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fread=fopen("E:/codejamc/B-large.in","r");
	FILE* fwrite=fopen("E:/codejamc/B-large.out","w");

	
	int case_num=0;
	int curr_case_num=0;
	__int64 L=0,P=0,C=0;

	fscanf(fread,"%d\n",&case_num);

	for(curr_case_num=0;curr_case_num<case_num;curr_case_num++)
	{
		
	
		if(fscanf(fread,"%I64d ",&L) EQUAL EOF
			|| fscanf(fread,"%I64d ",&P) EQUAL EOF
			|| fscanf(fread,"%I64d\n",&C) EQUAL EOF)
		{
			break;
		}

		__int64 Li=L;
		__int64 n=0;
		while(Li<P)
		{
			Li*=C;
			n++;
		}

		n-=1;

		int num=0;
		
		if( n EQUAL 0)
		{
			num=0;
		}
		else if(n EQUAL 1)
		{
			num=1;
		}
		else
		{
			__int64 x=0;

			while(cal(2,x)<=n)
			{
				x++;
			}
			num=x;
		}


		//done read a case


		
		
		fprintf(fwrite,"Case #%d: %d\n",curr_case_num+1,num);

		continue;




	}







	


	
	fclose(fread);
	fclose(fwrite);
	return 0;
}

