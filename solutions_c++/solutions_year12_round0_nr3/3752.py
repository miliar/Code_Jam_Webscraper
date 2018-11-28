#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(void){

	int T, i, j, k, l, idx, from, to, count, cmp;
	FILE *input, *output;
	char arr[10], copyarr[10];
	int data[50];
	int flag;

	input = fopen("input.txt", "r");
	output = fopen("output.txt", "w");

	fscanf(input, "%d", &T);
	for(i=0; i<T; i++){

		fscanf(input, "%d%d", &from, &to);
		memset(arr, '\0', sizeof(arr));
		count = 0;

		for(j=from; j<=to; j++){
			itoa(j, arr, 10);
			idx=0;
			memset(data, '\0', sizeof(data));

			if(from > 9){
				for(k=0; k<strlen(arr); k++){
					
					memset(copyarr, '\0', sizeof(copyarr));

					strncat(copyarr, &arr[k], strlen(arr)-k);
					strncat(copyarr, arr, k);
					cmp = atoi(copyarr);					

					if((from <= cmp) && (cmp <= to) && (cmp != j)){
						flag=0;
						for(l=0;l<idx; l++){
							if(cmp == data[l]) {
								flag=1;
								break;
							}
						}
						if(!flag) {
							data[idx++]=cmp;
							count++;
						}
						
					}
				}
			}		
		}
		fprintf(output, "Case #%d: %d\n", i+1, (count/2));
	}
	fclose(input);
	fclose(output);

	return 0;
}