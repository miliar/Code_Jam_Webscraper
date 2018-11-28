#include <stdio.h>
#define noofsnap 30
typedef unsigned long num_t;

int isOn(num_t noOfDevices,num_t maxSnaps)
{
	//	rep = 2^noOfDevices-1
	if(noOfDevices==0)
	{
		printf("Error");
		return 0;
	}
		
	num_t rep=1;
	for(int i=0;i<noOfDevices-1;i++)
	{
		rep= rep<<1;
		rep |= 1;
	}
	if(maxSnaps<rep)
		return 0;
	if(maxSnaps%(rep+1)==rep)
		return 1;
	return 0;
}
int main()
{
	FILE*fp= fopen("input.txt","r");
	FILE*outfp= fopen("output.txt","w");
	if(fp)
	{
		num_t noOfLines,noOfDevices,maxSnaps;
		fscanf(fp,"%lu",&noOfLines);
		printf("%lu lines\n",noOfLines);
		for(int i=0;i<noOfLines;i++){
			fscanf(fp,"%lu %lu",&noOfDevices,&maxSnaps);
			printf("%lu %lu\n",noOfDevices,maxSnaps);
			fprintf(outfp,"Case #%d: %s\n",i+1,(isOn(noOfDevices,maxSnaps)?"ON":"OFF"));
		}
	}
	else
		printf("Error opening file\n");
	fclose(outfp);
	fclose(fp);
	return 0;
}