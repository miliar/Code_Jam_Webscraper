#include <iostream>
#include <stdlib.h>
#include <iomanip>
#include <algorithm>
using namespace std;

double r[10000];
double x[10000];
double y[10000];
int p[10000];

bool comp(int a, int b) {
	return r[a] > r[b];
}

int main() {
	int T;
	cin >> T;
	srand(time(NULL));
	for (int t = 1; t <= T; t++) {
		int N, W, L;
		cin >> N >> W >> L;
		cout << "Case #" << t << ":";
		cout << setprecision(12);
		for (int i = 0; i < N; i++) {
			cin >> r[i];
			p[i] = i;
		}
		sort(p, p+N, comp);
		for (int i = 0; i < N; i++) {
			bool good = false;
			while (!good) {
				x[p[i]] = (((double)rand())/RAND_MAX) * W;
				y[p[i]] = (((double)rand())/RAND_MAX) * L;
				good = true;
				for (int j = 0; j < i; j++) {
					if ((x[p[i]]-x[p[j]])*(x[p[i]]-x[p[j]])+(y[p[i]]-y[p[j]])*(y[p[i]]-y[p[j]]) < 1.01 * (r[p[i]] + r[p[j]]) * (r[p[i]] + r[p[j]])) {
						good = false;
						break;
					}
				}
			}
		}
		for (int i = 0; i < N; i++) {
			cout << ' ' << x[i] << ' ' << y[i];
		}
		cout << '\n';
	}
	return 0;
}
