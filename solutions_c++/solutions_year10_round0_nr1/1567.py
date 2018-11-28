#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char inputFile[1024];
char outputFile[1024];
FILE *reader=NULL,*writer=NULL;

int testCases=0;
int snappers=0;
unsigned int flips=0;

int main(int argc,char *argv[]){

	time_t start,end;
	int i=0;
	int testCounter=0;
	unsigned int null=0;
	unsigned int portions=0;
	unsigned int usefulFlips=0;

	start = time(NULL);
	sprintf(inputFile,"A-large.in");
	sprintf(outputFile,"A-large.out");

	reader = fopen(inputFile,"rb");
	if(reader==NULL){
		printf("Cannot find inputfile\n");
		exit(1);
	}
	writer = fopen(outputFile,"wb");
	if(writer==NULL){
		exit(1);
	}
	
	fscanf(reader,"%d",&testCases);

	for(testCounter=0;testCounter<testCases;testCounter++){
//		printf("Case #%d:\n",testCounter+1);
		fprintf(writer,"Case #%d: ",testCounter+1);
		fscanf(reader,"%d",&snappers);
		fscanf(reader,"%u",&flips);

		//printf("%d %u\n",snappers,flips);
		null=1;
		for(i=0;i<snappers;i++){
			null*=2;
		}
		
		portions=flips/null;
		usefulFlips=flips-portions*null;
		//printf("null = %u\n",null);
		//printf("portions = %u\n",portions);
		//printf("usefulFlips = %u\n",usefulFlips);

		if((usefulFlips+1)==null){
			fprintf(writer,"ON\n");
		}
		else {
			fprintf(writer,"OFF\n");
		}
	}
	
	fclose(writer);
	fclose(reader);
	end = time(NULL);
	//printf("Time taken = %lds\n",end-start);
	return 0;
}