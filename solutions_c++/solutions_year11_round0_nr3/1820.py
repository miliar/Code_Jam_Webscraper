#include <stdio.h>
#include <string.h>

#define MAX_LINE_LENGTH	50000
#define MAX_VALORES	2000

void get_input(FILE* fid, long *valores, int &cant);
void print_output(FILE* fid, char* result);
long sum(long* nums,int amount);
long min(long* nums,int amount);

main()
{
	char first_line[MAX_LINE_LENGTH];
	int num_cases;
	int i,j;
	FILE *fid_input;
	FILE *fid_output;
	int amount;
	long valores[MAX_VALORES];
	long xoreado=0;
	long max_adv;
	char res[MAX_LINE_LENGTH];

	fid_input=fopen("info.txt","r");
	fid_output=fopen("res.txt","a");

	fgets(first_line,MAX_LINE_LENGTH,fid_input);
	sscanf(first_line,"%d",&num_cases);

	for(i=0;i<num_cases;i++)
	{
		xoreado=0;
		get_input(fid_input,valores,amount);

		for(j=0;j<amount;j++)
			xoreado=xoreado^valores[j];

		if(xoreado)
			strcpy(res,"NO");
		else
			sprintf(res,"%ld",sum(valores,amount)-min(valores,amount));

		print_output(fid_output,res);
	}
		
	fclose(fid_output);
	fclose(fid_input);
}

void get_input(FILE* fid, long *valores, int &cant)
{
	char line[MAX_LINE_LENGTH];
	char *ptr;
	int i;

	fgets(line,MAX_LINE_LENGTH,fid);
	sscanf(line,"%d",&cant);
	fgets(line,MAX_LINE_LENGTH,fid);

	ptr=line;
	for(i=0;i<cant;i++)
	{
		sscanf(ptr,"%ld",&valores[i]);
		ptr=strstr(ptr," ")+1;
	}
}

void print_output(FILE* fid, char* result)
{
	static int n=1;
	fprintf(fid,"Case #%d: %s\n",n++,result);
}

long sum(long* nums,int amount)
{
	long suma=0;
	int i;
	
	for(i=0;i<amount;i++)
		suma+=nums[i];
	return suma;
}

long min(long* nums,int amount)
{
	long minim=nums[0];
	int i;
	
	for(i=1;i<amount;i++)
	{
		if(nums[i]<minim)
			minim=nums[i];
	}
	return minim;
}
