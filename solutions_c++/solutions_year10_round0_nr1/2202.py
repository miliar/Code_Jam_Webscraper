#include <cstdio>
#define input "A.in"
#define output "A.out"
using namespace std;

int main()
{
	int t, n, k;
	int i;
	int onstat;

	FILE *fin = fopen(input, "r");
	FILE *fout = fopen(output, "w");

	fscanf(fin, "%d", &t);
	for (i = 0; i < t; i++) {
		fscanf(fin, "%d %d", &n, &k);
		fprintf(fout, "Case #%d: ", i + 1);
		if ((k + 1) % (2 << (n - 1)) == 0) fprintf(fout, "ON\n"); else fprintf(fout, "OFF\n");
	}

	fclose(fout);
	fclose(fin);
}