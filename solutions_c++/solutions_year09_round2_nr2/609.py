#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <assert.h>

int compare_chars(const void *p1, const void *p2) {
	char *c1 = (char*)p1;
	char *c2 = (char*)p2;

	if (*c1 < *c2)
		return -1;
	else if (*c1 > *c2)
		return 1;
	else
		return 0;
}

int main(int argc, char *argv[]) {
	FILE *f;
	unsigned int num_cases;
	char number[30];

	f = fopen(argv[1], "r");
	fscanf(f, "%d\n", &num_cases);

	for (int i = 0; i < num_cases; ++i) {
		unsigned int num_zeros = 0;
		bzero(number, 30);
		if (!fgets(number, 30, f))
			break;
		number[strlen(number) - 1] = 0;

		int len = strlen(number);
		/*
		for (unsigned int j = len - 1; j >= 0; --j) {
			if (number[j] == '0') {
				++num_zeros;
				number[j] = 0;
				--len;
			}
			else
				break;
		}
		*/
		//printf("number = %s\n", number);
		int index = len - 2;
		while (index >= 0 && number[index] >= number[index + 1]) {
			--index;
		}
		if (index == -1) {
			qsort(number, strlen(number), 1, compare_chars);
			//printf("new_number = %s\n", number);
			for (int j = len - 1; j >= 1; --j)
				number[j+1] = number[j];
			number[1] = '0';
		}
		else {
			char min = '9' + 1;
			int min_index = index;
			for (int j = len - 1; j > index; --j) {
				if (number[j] < min && number[j] > number[index]) {
					min = number[j];
					min_index = j;
				}
			}
			char tmp = number[index];
			number[index] = number[min_index];
			number[min_index] = tmp;
			qsort(number + index + 1, len - (index + 1), 1, compare_chars);
		}

		index = 0;
		while (number[index] == '0')
			++index;
		if (index > 0) {
			number[0] = number[index];
			number[index] = '0';
		}

		printf("Case #%d: %s", i+1, number);
		for (int j = 0; j < num_zeros; ++j) {
			printf("0");
		}
		printf("\n");
	}
	
	fclose(f);
}
