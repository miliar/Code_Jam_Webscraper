
#include <cstdio>

using namespace std;

int main() {
	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-out.txt", "w");

	int T;
	fscanf(fin, "%d", &T);

	for(int t = 1; t <= T; t++) {
		int N, K;
		fscanf(fin, "%d%d", &N, &K);
		fprintf(fout, "Case #%d: ", t);
		if((K + 1) % (1 << N))
			fprintf(fout, "OFF\n");
		else
			fprintf(fout, "ON\n");
	}

	return 0;
}
