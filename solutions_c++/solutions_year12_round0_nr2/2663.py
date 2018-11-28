#include <stdio.h>
#define MAX 100

FILE *f_input, *f_output;

int gPeople, gSurprise, gMoreThis;
int gScore[MAX];
int gCount;

void work();
int main(){
	int tmp;
	
	f_input = fopen("B-small-attempt1.in", "r");
	f_output = fopen("second.out", "w");

	fscanf(f_input, "%d\n", &tmp);

	for(int i=0; i<tmp; i++){

		gCount = 0;
		fscanf(f_input, "%d %d %d", &gPeople, &gSurprise, &gMoreThis);

		fprintf(f_output, "Case #%d: ", i+1);
		work();
		fprintf(f_output, "%d\n", gCount);
	}

	fclose(f_input);
	fclose(f_output);
}

void work(){

	int tmp;
	int Quotient, Remainder;

	for(int i=0; i<gPeople; i++){
		//fscanf(f_input, "%d",gScore[i]);
		fscanf(f_input, "%d", &tmp);

		Quotient = tmp/3;
		Remainder = tmp%3;

		switch(Remainder){

			case 0:

				if(Quotient >= gMoreThis){
					gCount++;
					break;
				}

				if(gSurprise != 0){
					if(Quotient != 0){
						if(Quotient+2 >= gMoreThis){
							gCount++;
							gSurprise--;
						}
					}
				}
				else{
					if(Quotient >= gMoreThis) gCount++;
				}
				break;

			case 1:
				if(Quotient+1 >= gMoreThis) gCount++;
				break;

			case 2:

				if(Quotient >= gMoreThis){
					gCount++;
					break;
				}

				if(gSurprise != 0){
					if(Quotient+2 >= gMoreThis){
						gCount++;
						gSurprise--;
					}
				}
				else{
					if(Quotient+1 >= gMoreThis) gCount++;
				}
				break;

		}
	}

}