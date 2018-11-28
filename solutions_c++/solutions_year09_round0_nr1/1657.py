#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>
#include <set>

using std::set;

typedef set<unsigned int> uint_set;

unsigned int get_next_token(char *buf, int len, FILE *f) {
	fread(buf, 1, 1, f);
	if (buf[0] != '(')
		return 1;
	unsigned int i = 0;
	do {
		++i;
		fread(buf + i, 1, 1, f);
	}
	while (buf[i] != ')');
	return (i + 1);
}

int main(int argc, char *argv[]) {
	FILE *f;
	char buf[30];
	unsigned int num_tokens, num_words, num_cases;
	char **words;

	f = fopen(argv[1], "r");
	fscanf(f, "%u %u %u\n", &num_tokens, &num_words, &num_cases);

	words = (char**)malloc(sizeof(char*) * num_words);
	for (unsigned int i = 0; i < num_words; ++i) {
		if (!fgets(buf, 20, f)) {
			fprintf(stderr, "Error reading word\n");
			exit(1);
		}
		buf[strlen(buf) - 1] = 0;
		assert(strlen(buf) == num_tokens);

		words[i] = strdup(buf);
	}

	for (unsigned int i = 0; i < num_cases; ++i) {
		uint_set candidate_words;
		for (unsigned int j = 0; j < num_words; ++j) {
			candidate_words.insert(j);
		}
		for (unsigned int k = 0; k < num_tokens; ++k) {
			//bzero(buf, 30);
			unsigned int len = get_next_token(buf, 30, f);
			//printf("token %d of len %d: %s\n", k, len, buf);

			uint_set::iterator w, next_w;
			for (w = candidate_words.begin(); w != candidate_words.end(); w = next_w) {
				next_w = w;
				++next_w;

				bool match = false;
				for (unsigned int j = 0; j < len; ++j) {
					if (buf[j] == '(' || buf[j] == ')')
						continue;
					if (words[*w][k] == buf[j]) {
						match = true;
						break;
					}
				}
				if (!match)
					candidate_words.erase(w);
			}
			if (candidate_words.size() == 0)
				break;
		}
		do {
			fread(buf, 1, 1, f); //read in newline
		}
		while (buf[0] != '\n');
		printf("Case #%d: %d\n", i + 1, candidate_words.size());
	}
}
