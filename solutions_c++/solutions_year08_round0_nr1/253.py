#include <cstring>
#include <cstdio>
#include <string>

using namespace std;

const int inf = 1000000000;

int N, S, Q;
string S_names[100], Q_values[1000];
int d[1001][100];

void read_data () {
	char temp[200];

	scanf ("%d\n", &S);
	for (int i = 0; i < S; ++i) { gets (temp); S_names[i] = temp; }

	scanf ("%d\n", &Q);
	for (int i = 0; i < Q; ++i) { gets (temp); Q_values[i] = temp; }
}

void solve () {
	for (int i = 0; i < S; ++i) d[0][i] = 0;

	for (int c = 1; c <= Q; ++c) {
		int ns = inf;
		for (int i = 0; i < S; ++i) if (S_names[i] == Q_values[c-1]) { ns = i; break; }

		for (int i = 0; i < S; ++i) {
			if (ns == i) { d[c][i] = inf; continue; }
			d[c][i] = d[c-1][i];

			if (ns != inf && d[c][i] > d[c-1][ns]+1) d[c][i] = d[c-1][ns]+1;
		}
	}

	int res = inf;
	for (int i = 0; i < S; ++i)
		if (res > d[Q][i]) res = d[Q][i];

	printf ("%d\n", res);
}

int main () {
	scanf ("%d\n", &N);

	for (int t = 0; t < N; ++t) {
		printf ("Case #%d: ", t+1);

		read_data ();
		solve ();
	}

	return 0;
}
