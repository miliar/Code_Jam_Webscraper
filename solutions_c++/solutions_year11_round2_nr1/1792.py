#include <stdio.h>
#include <iostream>

using namespace std;


int t, tmp, i, j, n;
int a[110][110];
double rpi[110], wp[110], owp[110], oowp[110];

void read() {

	freopen("rpi.in", "r", stdin);
	freopen("rpi.out","w",stdout);

	scanf("%d", &t);

}

void write(int test);


void solve() {

	for (int test=1; test<=t; ++test) {

		scanf("%d ", &n);
		int tmp;
		for (i=0; i<n; ++i) {
			for (j=0; j<n; ++j) {
				scanf("%c", &a[i][j]);
			}
			scanf("%c", &tmp);
		}

		for (i=0; i<n; ++i) {
			double won = 0, lost = 0;
			for (j=0; j<n; ++j) {
				if (a[i][j] == '0') {
					lost += 1;
				} else if (a[i][j] == '1') {
					won += 1;
				}
			}
			wp[i] = won/(won+lost);
		}

		for (i=0; i<n; ++i) {
			double tempWP = 0;
			double noWP = 0;
			for (j=0; j<n; ++j) {
				if (a[i][j] != '.') {
					noWP += 1;
					double won = 0, lost = 0;
					for (int k=0; k<n; ++k) {
						if (j != i && k != i){
							if (a[j][k] == '0') {
								lost += 1;
							} else if (a[j][k] == '1') {
								won += 1;
							}
						}
					}
					tempWP += (won/(won+lost));

				}

			}
			owp[i] = tempWP/noWP;
		}

		for (i=0; i<n; ++i) {
			double tempOWP = 0;
			double noOWP = 0;
			for (j=0; j<n; ++j) {
				if (a[i][j] != '.') {
					noOWP += 1;
					tempOWP += owp[j];
				}
			}
			oowp[i] = tempOWP/noOWP;
		}

		for (i=0; i<n; ++i) {
			rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		}


		write(test);
	}

}


void write(int test) {

	printf("Case #%d:\n", test);
	for (i=0; i<n; ++i) {
		printf("%lf\n", rpi[i]);
	}

}


int main() {

	read();
	solve();

	fclose(stdin);
	fclose(stdout);

	return 0;
}


