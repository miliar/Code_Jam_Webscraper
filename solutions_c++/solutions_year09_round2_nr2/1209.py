#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int charCompare(const void *v1, const void *v2) {
	const char *c1 = (const char *) v1;
	const char *c2 = (const char *) v2;
	return *c1 - *c2;
}

int main(int argc, char *argv[]) {
	char cases[500][23];
	int sizes[500];
	int T;
	
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
	
	fscanf(in_file, "%d", &T);
	
	for (int i = 0; i < T; i++) {
		fscanf(in_file, "%s", cases[i]);
		sizes[i] = strlen(cases[i]);
	}
	
	for (int i = 0; i < T; i++) {
		char *test = cases[i];
		bool found = false;
		for (int j = sizes[i] - 1; j > 0; j--) {
			if (test[j - 1] < test[j]) {
				char s1 = j - 1, s2 = j;
				for (int k = j + 1; k < sizes[i]; k++) {
					if (test[k] > test[s1] && test[k] < test[s2]) {
						s2 = k;
					}
				}
				char tmp = test[s1];
				test[s1] = test[s2];
				test[s2] = tmp;
				qsort(&test[j], sizes[i] - j, sizeof(char), charCompare);
				found = true;
				break;
			}
		}
		if (!found) {
			char reverse[25];
			for (int j = 0; j < sizes[i]; j++) {
				reverse[sizes[i] - j] = test[j];
			}
			reverse[0] = '0';
			reverse[sizes[i] + 1] = '\0';
			for (int k = 0; k < sizes[i] + 1; k++) {
				if (reverse[k] != '0') {
					reverse[0] = reverse[k];
					reverse[k] = '0';
					break;
				}
			}
			
			strcpy(cases[i], reverse);
		}
	}
	
	for (int i = 0; i < T; i++) {
		fprintf(out_file, "Case #%d: %s\n", i + 1, cases[i]);
	}
	
	fclose(in_file);
	fclose(out_file);
	
	return 0;
}