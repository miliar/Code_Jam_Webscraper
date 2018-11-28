#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

FILE *fp_r, *fp_w;
int t, n;
char arr[40][50];
vector<int> v;
int chk[40];
int cnt;

int main() {
	fp_r = fopen("a.in", "r");
	fp_w = fopen("a.out", "w");

	fscanf(fp_r, "%d", &t);
	for(int i = 0; i < t; ++i) {
		fscanf(fp_r, "%d", &n);
		v.clear();
		for(int j = 0; j < n; ++j) {
			fscanf(fp_r, "%s", arr[j]);
			v.push_back(0);
			for(int k = 0; k < n; ++k)
				if (arr[j][k] == '1') v[j] = k;
		}

		memset(chk, 0, sizeof(chk));
		for(int j = 0; j < n; ++j) {
			for(int k = 0; k < n; ++k) {
				if (v[k] == j) {
					if (chk[j] == 0) chk[j] = 1;
					else ++v[k];
				}
			}
		}

		cnt = 0;
		for(int j = 0; j < n; ++j) {
			for(int k = j+1; k < n; ++k) {
				if (v[j] > v[k]) {
					++cnt;
					swap(v[j], v[k]);
				}
			}
		}

		fprintf(fp_w, "Case #%d: %d\n", i+1, cnt);		
	}

	fclose(fp_w);
	fclose(fp_r);	

	return 0;
}