#include <cstdio>
#include <cstdlib>

using namespace std;

int main() {
	char map[26] = 	{'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i',
		'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm',
		'a', 'q'};
	char buffer[300];
	char res[300];
	int n;

	FILE* in = fopen("A-small-attempt0.in", "r");
	FILE* out = fopen("A-small-attempt0.out", "w");

	fscanf(in, "%d", &n);
	for(int i = 0; i < n; ++i) {
		fscanf(in, "\n%[^\n]", buffer);

		int j;
		for(j = 0; buffer[j]; ++j) {
			if(buffer[j] == ' ')
				res[j] = ' ';
			else
				res[j] = map[buffer[j] - 'a'];
		}
		res[j] = '\0';

		fprintf(out, "Case #%d: %s\n", i+1, res);
	}

	fclose(in);
	fclose(out);

	return 0;
}

