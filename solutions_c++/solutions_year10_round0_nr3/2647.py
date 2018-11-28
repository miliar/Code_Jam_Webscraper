// codejam_C2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#define MAX 2000



int R=0,K=0,N=0;
int g[MAX];


int calculate(int head,int times,int N,int totalnum)
{
	int carry=0;
	int total=0;

	int t=0;
	int i=head;
	while(t<times)
	{
		if(carry+g[i]<=K && carry+g[i]<=totalnum)
		{
			carry+=g[i];
			i++;
		}
		else
		{
			t++;
			total+=carry;
			carry=0;

		}
		if(i==N)
		{
			i=0;
		}

	}
	return total;
}


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* fread=fopen("e:\\C-small-attempt1.in","rb");
	FILE* fwrite=fopen("e:\\C-small-attempt1.out","wb");

	int case_num=0;
	
	int i=0,j=0;
	
	int heads[MAX];
	int heads_num=0;
	int curr_carry=0;
	
	int curr_head=0,next_head=0;
	bool easy=false;
	int loop_head=0,loop_end=0;
	int pre_looptime=0;
	int pre_loop_carry=0;
	int times_in_one_loop=0;
	int totalnum=0;
	int curr_case_num=0;

	fscanf(fread,"%d\n",&case_num);
	for(curr_case_num=0;curr_case_num<case_num;curr_case_num++)
	{
		
		if(fscanf(fread,"%d ",&R)==EOF
			|| fscanf(fread,"%d ",&K)==EOF
			|| fscanf(fread,"%d\n",&N)==EOF)
		{
			break;
		}
		totalnum=0;
		for(j=0;j<N-1;j++)
		{
			fscanf(fread,"%d ",&g[j]);
			totalnum+=g[j];
		}
		fscanf(fread,"%d\n",&g[j]);
		totalnum+=g[j];
		//done read a case


		
		
		fprintf(fwrite,"Case #%d: %d\n",curr_case_num+1,calculate(0,R,N,totalnum));
		continue;




	}







	


	
	fclose(fread);
	fclose(fwrite);
	return 0;
}

