#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE *f_input, *f_output;

char gCharArr[8];
bool gBool[2000001];
int gTmp[8];
int gTmpIndex;

void work();
int Recycle(int j, int length);
int Multiple(int multi);
void ResetGTmp(){
	for(int i=0; i<8; i++) gTmp[i] = 0;

	gTmpIndex = 0;
}

bool PushGTmp(int val){
	for(int i=0; i<8; i++){
		if(gTmp[i] == val) return 0;
	}

	gTmp[gTmpIndex++] = val;

	return 1;
}

int main(){
	int tmp;
	
	f_input = fopen("C-large.in", "r");
	f_output = fopen("third.out", "w");

	fscanf(f_input, "%d\n", &tmp);

	for(int i=0; i<tmp; i++){
		for(int j=0; j<2000001; j++) gBool[j] = 0;
		fprintf(f_output, "Case #%d: ", i+1);
		work();
	}

	fclose(f_input);
	fclose(f_output);
}

void work(){
	int inputA, inputB;
	int length;
	int tmp;
	int count = 0;

	fscanf(f_input, "%d %d", &inputA, &inputB);
	sprintf(gCharArr, "%d", inputA);

	length =strlen(gCharArr);

	for(int i=inputA; i<=inputB; i++){

		sprintf(gCharArr, "%d", i);
	
		ResetGTmp();		

		for(int j=1; j<length; j++){
			tmp = Recycle(j, length);

			if(PushGTmp(tmp) != 0){
				if(tmp >= inputA && tmp <= inputB){
					if(i != tmp){
						if(gBool[tmp]==0){
							count++;
							gBool[i]=1;
							//fprintf(f_output,"%d %d\n", i, tmp);
						}
					}
				}
			}
		}
		
	}
	
	fprintf(f_output, "%d\n", count);

}

int Recycle(int j, int length){

	int sum=0;
	int multi; 
	

	multi = 0;
	for(int i = j-1; i>=0; i--){
		sum += (gCharArr[i]-48) * Multiple(multi);
		multi++;
	}

	//////////////////

	multi = length-1;
	for(int i = j; i<length; i++){
		sum += (gCharArr[i]-48) * Multiple(multi);
		multi--;
	}


	return sum;
}

int Multiple(int multi){

	int sum=10;

	if(multi == 0) return 1;

	for(int i=0; i<multi-1; i++) sum *= 10;

	return sum;

}