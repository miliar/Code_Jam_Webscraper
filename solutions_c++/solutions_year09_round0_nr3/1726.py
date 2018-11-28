#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	FILE *f;
	char *sentence = "welcome to code jam";
	unsigned int sentence_len;
	char string[550];
	unsigned int positions[27][4];
	unsigned int num_positions[27];
	unsigned int num_cases;

	sentence_len = strlen(sentence);
	f = fopen(argv[1], "r");
	fscanf(f, "%d\n", &num_cases);

	bzero(positions, 27 * 4 * sizeof(unsigned int));
	bzero(num_positions, 27 * sizeof(unsigned int));
	for (unsigned int i = 0; i < sentence_len; ++i) {
		if (sentence[i] == ' ') {
			positions[26][num_positions[26]] = i;
			++num_positions[26];
		}
		else {
			positions[sentence[i] - 97][num_positions[sentence[i] - 97]] = i;
			++num_positions[sentence[i] - 97];
		}
	}

	for (unsigned int t = 0; t < num_cases; ++t) {
		unsigned long long *counts[4];
		bzero(string, 550);
		if (!fgets(string, 550, f))
			break;
		string[strlen(string) - 1] = 0;

		unsigned int string_len = strlen(string);
		for (int i = 0; i < 4; ++i) {
			counts[i] = (unsigned long long*)malloc(sizeof(unsigned long long) * string_len);
			bzero(counts[i], sizeof(unsigned long long) * string_len);
		}
		for (int i = string_len - 1; i >= 0; --i) {
			if (string[i] != ' ' && (string[i] < 'a' || string[i] > 'z'))
				continue;
			//printf("Processing '%c' at index %d\n", string[i], i);
			unsigned int c;
			if (string[i] == ' ')
				c = 26;
			else
				c = string[i] - 97;
			if (num_positions[c] == 0)
				continue;
			for (unsigned int j = 0; j < num_positions[c]; ++j) {
				if (positions[c][j] == sentence_len - 1) {
					counts[j][i] = 1;
					continue;
				}
				for (unsigned int k = i + 1; k < string_len; ++k) {
					if (string[k] != ' ' && (string[k] < 'a' || string[k] > 'z'))
						continue;
					if (string[k] != sentence[positions[c][j] + 1])
						continue;
					unsigned int c2;
					if (string[k] == ' ')
						c2 = 26;
					else
						c2 = string[k] - 97;
					for (unsigned int m = 0; m < num_positions[c2]; ++m) {
						if (positions[c2][m] == positions[c][j] + 1) {
							counts[j][i] += counts[m][k];
							break;
						}
					}
				}
				//printf("counts[%d] set to %lld\n", j, counts[j][i]);
			}
		}

		unsigned long long total_count = 0;
		for (unsigned int i = 0; i < string_len; ++i) {
			if (string[i] == 'w')
				total_count += counts[0][i];
		}
		for (int i = 0; i < 4; ++i) {
			free(counts[i]);
		}
		printf("Case #%d: %04d\n", t + 1, total_count % 10000);
	}
}
