#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char inputFile[1024];
char outputFile[1024];
FILE *reader=NULL,*writer=NULL;

int testCases=0;
unsigned int rides=0;
unsigned int capacity=0;
unsigned long long earnings=0;
int numGroups=0;
unsigned int groups[1000];

bool  knownEarnings[1000];
unsigned int earningsCache[1000];
int cacheEndPos[1000];

unsigned int tempEarnings=0;
unsigned int filled=0;
int groupsIn=0;
int pos=0;

int main(int argc,char *argv[]){

	time_t start,end;
	int i=0;
	unsigned int ridesCounter=0;
	int startingPos=0;
	int testCounter=0;

	start = time(NULL);
	sprintf(inputFile,"C-large.in");
	sprintf(outputFile,"C-large.out");

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

		fscanf(reader,"%u",&rides);
		fscanf(reader,"%u",&capacity);
		fscanf(reader,"%d",&numGroups);


		//printf("%u %u %d\n",rides,capacity,numGroups);
		for(i=0;i<numGroups;i++){
			fscanf(reader,"%d",&groups[i]);
		}

		for(i=0;i<numGroups;i++){
			knownEarnings[i]=false;
			//earningsCache[1000];
		}

		pos=0;
		startingPos=0;
		earnings=0;
		for(ridesCounter=0;ridesCounter<rides;ridesCounter++){
			filled=0;
			groupsIn=0;
			if(knownEarnings[pos]){
				earnings+=earningsCache[pos];
				pos=cacheEndPos[pos];
				continue;
			}
			tempEarnings=0;
			do {
				filled+=groups[pos];
				tempEarnings+=groups[pos];
				
				pos++;
				if(pos==numGroups){
					pos=0;
				}
				groupsIn++;
				if(groupsIn==numGroups){
					break;
				}
			}while(groups[pos]<=capacity-filled);

			knownEarnings[startingPos]=true;
			earningsCache[startingPos]=tempEarnings;
			cacheEndPos[startingPos]=pos;
			startingPos=pos;
			earnings+=tempEarnings;

			//printf("got %d groups in!\n",groupsIn);
			//printf("current pos = %d\n",pos);
			//printf("current $ = %llu\n",earnings);getchar();
		}
		
		//for(i=0;i<numGroups;i++){
		//	printf("%d ",groups[i]);
		//}
		//printf("\n");

		fprintf(writer,"%llu\n",earnings);
	}
	
	fclose(writer);
	fclose(reader);
	end = time(NULL);
	//printf("Time taken = %lds\n",end-start);
	return 0;
}