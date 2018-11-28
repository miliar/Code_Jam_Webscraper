#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char inputFile[1024];
char outputFile[1024];
int posL[1000];
int posR[1000];

FILE *reader=NULL,*writer=NULL;

int testCases=0;
int windows=0;
int crosses=0;

int main(int argc,char *argv[]){

	time_t start,end;
	int i=0,j=0,k=0,l=0;
	int testCounter=0;

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
		//printf("Case #%d:\n",testCounter+1);
		fprintf(writer,"Case #%d: ",testCounter+1);

		fscanf(reader,"%d",&windows);
		crosses=0;

		for(i=0;i<windows;i++){
			fscanf(reader,"%d",&posL[i]);
			fscanf(reader,"%d",&posR[i]);
			//printf("%d %d\n",posL[i],posR[i]);
		}

		for(j=0;j<windows;j++){
			for(k=j+1;k<windows;k++){
				//printf("%d * %d = %d\n",posL[j]-posL[k],posR[j]-posR[k],(posL[j]-posL[k])*(posR[j]-posR[k]));getchar();
				if((posL[j]-posL[k])*(posR[j]-posR[k])< 0){
					crosses++;
				}
			}
		}
		
		fprintf(writer,"%d\n",crosses);
	}
	
	fclose(writer);
	fclose(reader);
	end = time(NULL);
	//printf("Time taken = %lds\n",end-start);
	return 0;
}