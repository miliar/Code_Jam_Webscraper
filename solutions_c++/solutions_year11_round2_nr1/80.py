#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <math.h>
using namespace std;

int T;
char ar[100][1000];
long double WP[100];
long double OWP[100];

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d:\n", test+1);
		int N;
		scanf("%d ", &N);
		for (int y = 0; y < N; y++) {
			scanf("%s ", ar[y]);
		}
		for (int y = 0; y < N; y++) {
			int WPsum = 0, opponents = 0;
			OWP[y] = 0;
			for (int x = 0; x < N; x++) {
				if (ar[y][x] != '.') {
					opponents++;
					int OWPsum = 0, OWPanz = 0;
					for (int z = 0; z < N; z++) {
						if (z == y)
							continue;
						if (ar[x][z] != '.')
							OWPanz++;
						if (ar[x][z] == '1')
							OWPsum++;
					}
					OWP[y] += (long double)OWPsum/OWPanz;
				}
				if (ar[y][x] == '1')
					WPsum++;
			}
			WP[y] = (long double)WPsum/opponents;
			OWP[y] /= opponents;
		}
		for (int y = 0; y < N; y++) {
			long double OOWPsum = 0;
			int opponents = 0;
			for (int x = 0; x < N; x++) {
				if (ar[y][x] != '.') {
					opponents++;
					OOWPsum += OWP[x];
				}
			}
			OOWPsum /= opponents;
			printf("%.15Lf\n", 0.25*WP[y]+0.5*OWP[y]+0.25*OOWPsum);
		}
	}
	return 0;
}
