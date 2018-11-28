#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>

//test case structure
static struct testcase{
	//run R times a day
	int R;
	//hold k people once
	int k;
	//n groups
	int N;
	//the real number of people in each group
	int group[10];
	//the euros get today
	int euros;
};

//test case number
static int number;
//all test cases
static struct testcase allcases[100];
//FILE *output = fopen("test.out","w");

void readIn(){
	FILE *input = fopen("C-small-attempt2.in","r");
	//get testcase number
	fscanf(input,"%d\n",&number);

	//get all testcases
	for (int i = 0 ; i< number ;i++){

		//get the basic infomation for the testcase
		fscanf(input,"%d %d %d\n",&allcases[i].R,&allcases[i].k,&allcases[i].N);

		//get people in each group
		for (int j = 0 ; j < allcases[i].N;j++){
			fscanf(input,"%d",&allcases[i].group[j]);
		}
	}
	fclose(input);
}

void calculate(){
	
	int euroCount = 0;
	//number of people get in every round
	int peopleOnce = 0;
	//number of groups get in
	//int groupNum = 0;
	//current position of the pointer in group
	int curPosition = 0;
	int groupUsed = 0;
	int tmp;

	//each testcase
	for(int i=0;i<number;i++){
		//run R times a day
		for(int j=0;j<allcases[i].R;j++){
			//get enough people
			//fprintf(output,"people Max %d\n", allcases[i].k);
			//fprintf(output,"group Max %d\n", allcases[i].N);
			while(peopleOnce < allcases[i].k){
				tmp = peopleOnce + allcases[i].group[curPosition];	
				//more than the maximum number, do not add
				if(tmp > allcases[i].k){
					break;
				}else{
					peopleOnce += allcases[i].group[curPosition];
					//fprintf(output,"peopleOnce %d\n", peopleOnce);
					groupUsed ++;
					//fprintf(output,"groupUsed %d\n\n", groupUsed);
					if(groupUsed == allcases[i].N){
						break;
					}
					//move position
					curPosition ++;
					//the end of groups, switch to begin
					if(curPosition >= allcases[i].N){
						curPosition = 0;
					}
				}
			}
			//fprintf(output,"end round\n\n");
			//record
			euroCount += peopleOnce;
			//reset
			peopleOnce = 0;
			groupUsed = 0;
		}
		//fprintf(output,"end day\n\n");
		//record
		allcases[i].euros = euroCount;
		//reset
		euroCount = 0;
		curPosition = 0;
	}
}

void readOut(){
	FILE *output = fopen("test.out","w");

	//put result from all testcases
	for (int i = 0 ; i< number ;i++){
		//fprintf(output,"%d ",allcases[i].R);
		//fprintf(output,"%d ",allcases[i].k);
		//fprintf(output,"%d\n",allcases[i].N);
		//for(int j=0; j<allcases[i].N; j++){
		//	fprintf(output,"%d ",allcases[i].group[j]);
		//}
		//fprintf(output,"\n");
		fprintf(output,"Case #%d: %.lu\n",i+1,allcases[i].euros);
	}
	
	
	fflush(output);
	fclose(output);
}

int main(int argc, char* argv[])
{
	readIn();
	calculate();
	readOut();
}