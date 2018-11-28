#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

const int MaxN = 101;

int n;
int gde[MaxN][2];
int order[MaxN];

int main() {
	FILE *f = fopen("A.in", "r");
	FILE *fout = fopen("A.out", "w");

	int t; fscanf(f, "%d", &t);
	for (int test = 1; test <= t; test++){
		fscanf(f, "%d", &n);
		int k0 = 0, k1 = 0;
		for (int i = 0; i < n; i++) {
			char ch; int gg;
			fscanf(f, " %c %d", &ch, &gg);
			if (ch == 'O') gde[k0++][0] = gg;
			else gde[k1++][1] = gg;

			order[i] = ch == 'O' ? 0 : 1;
		}

		int time = 0;

		int p0 = 0, p1 = 0;
		int poz0 = 1, poz1 = 1;
		int iOrd = 0;
		while (iOrd < n) {
			time++;

			if (order[iOrd] == 0) {
				if (poz0 != gde[p0][0]){
					if (poz0 > gde[p0][0]) poz0--;
					else poz0++;
				}
				else{
					//cout << iOrd << " = " << time << endl;
					iOrd++;
					p0++;
				}

				// move bot 2
				if (p1 < k1){
					if (poz1 > gde[p1][1]) poz1--;
					else if (poz1 < gde[p1][1]) poz1++;
				}
			}
			else {
				if (poz1 != gde[p1][1]){
					if (poz1 > gde[p1][1]) poz1--;
					else poz1++;
				}
				else{
					//cout << iOrd << " = " << time << endl;
					iOrd++;
					p1++;
				}

				// move bot 2
				if (p0 < k0){
					if (poz0 > gde[p0][0]) poz0--;
					else if (poz0 < gde[p0][0]) poz0++;
				}
			}
		}

		fprintf(fout, "Case #%d: %d\n", test, time);
	}

	fclose(fout);
	fclose(f);

	return 0;
}
