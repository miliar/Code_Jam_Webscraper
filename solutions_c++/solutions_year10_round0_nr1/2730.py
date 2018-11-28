// codejam_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#define MAX 10005

int _tmain(int argc, _TCHAR* argv[])
{

	FILE* fread=fopen("e:\\A-large.in","rb");
	FILE* fwrite=fopen("e:\\A-large.out","wb");



	int n[MAX];
	int k[MAX];

	int i=0,j=0;
	int t;
	int e=0;

	int curr_num=1;


	fscanf(fread,"%d",&t);

	if(t<=0)
		return 0;

	for(i=0;i<t;i++)
	{
		if(fscanf(fread,"%d ",&n[i])==EOF||fscanf(fread,"%d\n",&k[i])==EOF)
			break;
	}
	for(j=0;j<i;j++)
	{
		curr_num=1;
		if(n[j]<=0||k[j]<n[j])
		{
			fprintf(fwrite,"Case #%d: OFF\n",j+1);
			continue;
		}
		
		for(e=0;e<n[j];e++)
		{
			curr_num*=2;
		}
		curr_num-=1;
	
		if(k[j]<curr_num)
		{
			fprintf(fwrite,"Case #%d: OFF\n",j+1);
			continue;
		}
		if((k[j]-curr_num)%(curr_num+1)==0)
		{
			fprintf(fwrite,"Case #%d: ON\n",j+1);
			continue;
		}
		
		fprintf(fwrite,"Case #%d: OFF\n",j+1);
			continue;


	}


	fclose(fread);
	fclose(fwrite);
	
	return 0;
}

