#include <stdio.h>


int main(){
int cases;
int number,sup,p,curp;
int counter;
int i,j;
FILE *input;
FILE *output;
input = fopen("B-large.in","r");
output = fopen("output1.txt", "w");
fscanf(input, "%d", &cases);
for(i=0;i<cases;i++){
	counter=0;
	fscanf(input, "%d %d %d", &number, &sup, &p);
	for(j=0;j<number;j++){
		fscanf(input, "%d", &curp);
		if(curp>3*(p-1)){
			counter++;
		}else if(curp>=3*p-4 && curp<=3*p-3 && sup>0 && p>1){
			counter++;
			sup--;
		}
	}
	fprintf(output,"Case #%d: %d\n",i+1,counter);
}


//fprintf(output, "%d %d %d %d", cases,number,sup,points);
fclose(input);
fclose(output);

	return 0;
}