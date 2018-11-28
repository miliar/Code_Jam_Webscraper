#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

FILE *fp_r, *fp_w;
int t, n;
int x, y, i, j;
vector<int> v1, v2;
int sum;

int main() {

	fp_r = fopen("A-small.txt", "r");
	fp_w = fopen("A.out", "w");

	fscanf(fp_r, "%d", &t);
	for(i = 0; i < t; i++) {
		fscanf(fp_r, "%d", &n);
		v1.clear();
		for(j = 0; j < n; j++) {
			fscanf(fp_r, "%d", &x);
			v1.push_back(x);
		}
		v2.clear();
		for(j = 0; j < n; j++) {
			fscanf(fp_r, "%d", &y);
			v2.push_back(y);
		}

		sort(v1.begin(), v1.end());
		sort(v2.rbegin(), v2.rend());

        sum = 0;
		for(j = 0; j < n; j++)
			sum += v1[j] * v2[j];
		fprintf(fp_w, "Case #%d: %d\n", i+1, sum);
	}

	fclose(fp_r);
	fclose(fp_w);

	return 0;
}