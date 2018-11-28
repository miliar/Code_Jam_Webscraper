#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void){

	int T, i, j;
	char input[200], output[200];
	char table[30]="yhesocvxduiglbkrztnwjpfmaq";

	FILE *input_fp, *output_fp;

	input_fp = fopen("input.txt", "r");
	output_fp = fopen("output.txt", "w");

	/* input */
	fscanf(input_fp, "%d ", &T);
	for(i=0; i<T; i++){

		memset(input, '\0', sizeof(input));
		memset(output, '\0', sizeof(output));
		
		fgets(input, 200, input_fp);
		for(j=0; j<strlen(input); j++){
			if(input[j] == ' ')		output[j]=' ';
			else					output[j]=table[input[j]-0x61];

		}
		output[j-1]='\0';
		fprintf(output_fp, "Case #%d: %s\n", i+1, output);

	}

	fclose(input_fp);
	fclose(output_fp);

	return 0;

}