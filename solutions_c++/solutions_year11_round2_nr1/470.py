#include <iostream>
using namespace std;

#define MAXN 128

struct team {
	int w, l;
	double wp, owp, oowp;
} n[MAXN];

char g[MAXN][MAXN];
double wp[MAXN][MAXN];

int main() {

freopen("in.txt", "r", stdin);

int N, i, j, tmp, t, T;

cin >> T;

for (t=1; t<=T; t++) {

cin >> N;

for (i=0; i<N; i++) {
	n[i].w = n[i].l = 0;

	for (j=0; j<N; j++) {
		cin >> g[i][j];
		if (g[i][j] == '1') n[i].w++;
		else if (g[i][j] == '0') n[i].l++;
	}
}

for (i=0; i<N; i++) {
	for (j=0; j<N; j++) {
		if (g[i][j] == '1') {
			wp[i][j] = ((double)(n[i].w-1))/((double)(n[i].w+n[i].l-1));
		} else if (g[i][j] == '0') {
			wp[i][j] = ((double)n[i].w)/((double)(n[i].w+n[i].l-1));
		} else {
			wp[i][j] = ((double)n[i].w)/((double)(n[i].w+n[i].l));
		}
	}
	n[i].wp = wp[i][i];
}

for (i=0; i<N; i++) {
	n[i].owp = 0.0; tmp = 0;
	for (j=0; j<N; j++) {
		if (g[i][j] == '.') continue;

		n[i].owp += wp[j][i];
		tmp++;
	}
	n[i].owp /= tmp;
}

for (i=0; i<N; i++) {
	n[i].oowp = 0.0; tmp = 0;
	for (j=0; j<N; j++) {
		if (g[i][j] == '.') continue;

		n[i].oowp += n[j].owp;
		tmp++;
	}
	n[i].oowp /= tmp;
}

cout << "Case #" << t << ":" << endl;
for (i=0; i<N; i++) {
	printf("%.12lf\n", 0.25*n[i].wp + 0.5*n[i].owp + 0.25*n[i].oowp);
}

}

return 0;
}
