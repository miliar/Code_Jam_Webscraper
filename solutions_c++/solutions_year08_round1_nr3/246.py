#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int val[31] = {0, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};
//5.2360679774997896964091736687313

FILE *fp_r, *fp_w;
int t, n, i;

int main() {

	fp_r = fopen("C-small.txt", "r");
	fp_w = fopen("C.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d", &n);
		fprintf(fp_w, "Case #%d: %03d\n", i+1, val[n]);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}