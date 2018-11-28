#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>

using namespace std;

int T,N;
char str[2000];
char scores[100][200];
int wins[100];
int totals[100];
double WP[100];
double OWP[100];
double OOWP[100];

double percentage(int a, int b) {
	return ((double) a) / ((double) b);
}

void tellen() {
	for (int i = 0; i < N; i++) {
		wins[i] = 0;
		totals[i] = 0;
		for (int j = 0; j < N; j++) {
			if (isdigit(scores[i][j])) { // '0' of '1'
				totals[i]++;
				if (scores[i][j] == '1')
					wins[i]++;
			}
		}
		WP[i] = percentage(wins[i], totals[i]);
	}
	for (int i = 0; i < N; i++) {
		double gemiddeld = 0.0;
		int som = 0;
		for (int j = 0; j < N; j++) {
			if (j == i)
				continue;
			if (scores[j][i] == '.')
				continue;
			som++;
			int w = wins[j];
			if (scores[j][i] == '1')
				w--;
			int t = totals[j] - 1;
			gemiddeld += percentage(w, t);
		}
		OWP[i] = gemiddeld / ((double) som);
	}
	for (int i = 0; i < N; i++) {
		double gemiddeld = 0.0;
		int som = 0;
		for (int j = 0; j < N; j++) {
			if (j == i)
				continue;
			if (scores[j][i] == '.')
				continue;
			som++;
			gemiddeld += OWP[j];
		}
		OOWP[i] = gemiddeld / ((double) som);
	}
}

int main() {
	fgets(str, 1000, stdin);
	sscanf(str, "%d", &T);
	for (int i = 0; i < T; i++) {
		fgets(str,1000,stdin);
		sscanf(str, "%d", &N);
		for (int j = 0; j < N; j++) {
			fgets(str,1000,stdin);
			strcpy(scores[j], str);
		}
		tellen();
		printf("Case #%d:\n", i + 1);
		for (int j = 0; j < N; j++) {
			printf("%.9f\n", 0.25 * WP[j] + 0.5 * OWP[j] + 0.25 * OOWP[j]);
		}
	}
	return 0;
}

