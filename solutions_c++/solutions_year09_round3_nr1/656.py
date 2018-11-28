#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define NONE 128

int main(int argc, char *argv[]) {
	char *in_name, *out_name;
	FILE *in_file, *out_file;
	
	if (argc != 3) {
		printf("Usage: %s <infile> <outfile>\n", argv[0]);
		return 1;
	}
	
	in_name = argv[1];
	out_name = argv[2];
	
	in_file = fopen(in_name, "r");
	out_file = fopen(out_name, "w");
	
	int T;
	char cases[100][62];
	int sizes[100];
	
	fscanf(in_file, "%d", &T);
	
	for (int i = 0; i < T; i++) {
		fscanf(in_file, "%s", cases[i]);
		sizes[i] = strlen(cases[i]);
	}
	
	for (int i = 0; i < T; i++) {
		char *test = cases[i];
		
		unsigned char values[36], base;
		bool found[36];
		for (int j = 0; j < 36; j++) {
			found[j] = false;
			values[j] = NONE;
		}
		
		for (int j = 0; j < sizes[i]; j++) {
			if (test[j] > '9')
				found[test[j] - 'a' + 10] = true;
			else
				found[test[j] - '0'] = true;
		}
		
		base = 0;
		for (int j = 0; j < 36; j++) {
			if (found[j]) {
				base++;
			}
		}
		if (base == 1)
			base++;
		
		int counter = 0;
		for (int j = 0; j < sizes[i]; j++) {
			int idx = (test[j] > '9') ? (test[j] - 'a' + 10) : test[j] - '0';
			if (values[idx] == NONE) {
				if (counter == 0) {
					values[idx] = 1;
				} else if (counter == 1) {
					values[idx] = 0;
				} else {
					values[idx] = counter;
				}
				counter ++;
			}
		}
		
		unsigned int min = 0;
		for (int j = 0; j < sizes[i]; j++) {
			int idx = (test[j] > '9') ? (test[j] - 'a' + 10) : test[j] - '0';
			min = min * base + values[idx];
		}
		fprintf(out_file, "Case #%d: %d\n", i + 1, min);
	}
	
	fclose(in_file);
	fclose(out_file);
	
	return 0;
}