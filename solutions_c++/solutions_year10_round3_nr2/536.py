#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char inputFile[1024];
char outputFile[1024];

FILE *reader=NULL,*writer=NULL;

int testCases=0;
int L=0;
int P=0;
int C=0;
int temp=0;
int segments=0;
int trials=0;

int main(int argc,char *argv[]){

	time_t start,end;
	int i=0,j=0,k=0,l=0;
	int testCounter=0;

	start = time(NULL);
	sprintf(inputFile,"B-small-attempt0.in");
	sprintf(outputFile,"B-small-attempt0.out");

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
		//printf("Case #%d:\n",testCounter+1);
		fprintf(writer,"Case #%d: ",testCounter+1);

		fscanf(reader,"%d",&L);
		fscanf(reader,"%d",&P);
		fscanf(reader,"%d",&C);
		//printf("%d %d %d\n",L,P,C);
		segments=0;
		temp=L;
		trials=0;
		if(L*C<P){
			do {
				temp=temp*C;
				segments++;
			}while(temp<P);
			segments--;
			//printf("segments=%d\n",segments);
			if(segments==1){
				trials=1;
			}
			else {
				do {
					trials++;
					segments=segments/2;
				}while(segments!=1);
				trials++;
			}
		}

		//printf("trials=%d\n\n",trials);
		fprintf(writer,"%d\n",trials);
	}
	
	fclose(writer);
	fclose(reader);
	end = time(NULL);
	//printf("Time taken = %lds\n",end-start);
	return 0;
}