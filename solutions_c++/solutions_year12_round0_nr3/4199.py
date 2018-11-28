#include <cstdlib>
#include <cstdio>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int debug = 0;

int no_repeated(char* number){
	if(debug == 1) printf("no repeated ---> ");
	char *current = NULL;
	char *previous = NULL;
	int repetitions = 0;
	int number_size = 0;

	previous = &number[0];
	if(*previous != '\0'){
		current = &number[1];
	}else{
		return -1;
	}
	while(*current != '\n' && *current != '\0'){
		if(*current == *previous) repetitions++;
		number_size++;
		current++;		
	}

	if(repetitions == number_size)return -1;

	return 1;
}

int find_pair(char* original_number, int ini){
	if(debug == 1) printf("find pair ---> ");
	int counter = 0;
	int str_num_size = 0;
	char *index = &original_number[0];
	int i, j, k ;
	int combinations = 0;

	while(*index != '\0' && *index != '\n'){
		str_num_size++;
		index++;
	}
	char new_number[str_num_size];
	int previous_number = 0;

	for(i = str_num_size-1; i > 0; i--){
		for(k = 0; k < str_num_size-i; k++)new_number[k] = original_number[i+k];
		j = k;
		for(k = k; k < str_num_size; k++)new_number[k] = original_number[k-j];

		new_number[str_num_size] = '\0';

		if(debug == 1)printf("\n%s\n", new_number);
		if(new_number[0] != '0'){
			int current_number = atoi(new_number);
			if(current_number < atoi(original_number) && current_number >= ini){
				if(debug == 1)printf("%s > [%s]\n", original_number, new_number);
				if(previous_number != current_number){
					previous_number = current_number;
					counter++;
				}
			}
		}

	}

	//if(counter > 1)counter = 1;

	return counter;

}


char* tostring(int number){
	int aux_number =  number;
	int base = 10;
	int res = 0;
	int size = 0;

	while(aux_number > 0){
		aux_number /= 10;
		size++;
	}

	char *new_number = (char*)malloc(sizeof(char)*size);
	size--;

	aux_number = number;

	while(aux_number > 0){
		res = aux_number%base;
		aux_number /= base;
		new_number[size--] = 48 + res;
	}
	if(debug == 1) printf("tostring [%s]", new_number);

	return new_number;

}


int main(int argc, char* argv[]){

	//printf("%s\n", argv[1]);

	//int pairs = find_pair(argv[1]);
	//printf("%i", pairs);

	int cases = 0;
	int case_counter = 1;
	int ini = 0, end = 0;
	int i, j, k;
	int pairs = 0;
	char number[100];

	//pairs = find_pair(argv[1]);
	//printf("tostring [%s]", tostring(i));


	scanf("%i", &cases);
	while(cases--){
		//printf("cases %i\n", cases);
		scanf("%i", &ini);
		scanf("%i", &end);
		char *str_number;
		pairs = 0;
		for(i = ini; i < end+1; i++){
			str_number = tostring(i);
			if(no_repeated(str_number) == 1)pairs += find_pair(str_number, ini);
			if(debug == 1)printf(" pairs ----> %i\n", pairs);
		}
		if(debug == 1)printf("========================pairs======================================================= %i\n", pairs);
		printf("Case #%i: %i", case_counter++, pairs);
		if(cases)printf("\n");
	}



	return 0;

}
