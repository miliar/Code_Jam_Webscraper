#include <cstdio>
#include <cstring>
#include <string>

#define MAXN 120

using namespace std;

long double wp[MAXN][MAXN], owp[MAXN], oowp[MAXN];
int Win[MAXN], Lose[MAXN];
char S[MAXN][MAXN];
int N;
int main () {

	freopen ("rpi.in", "r", stdin);
	freopen ("rpi.out", "w", stdout);

	int tests;
	scanf ("%d\n", &tests);
	for (int t = 1; t <= tests; t++) {
		scanf ("%d\n", &N);
		
		memset (wp, 0, sizeof (wp));
		memset (owp, 0, sizeof (owp));
		
		for (int i = 1; i <= N; i++)
			Win[i] = Lose[i] = 0;
		int i, j, opp;
		long double s;

		for (i = 1; i <= N; i++) {
			gets (S[i] + 1);
			for (j = 1; j <= N; j++) {
				if (S[i][j] == '1') Win[i] += 1;
				if (S[i][j] == '0') Lose[i] += 1;
			}
		}
		
		for (i = 1; i <= N; i++) {
			wp[i][0] = Win[i] / (long double)(Lose[i] + Win[i]);
			
			for (j = 1; j <= N; j++) {
				int t = 0;
				if (S[i][j] == '.') continue;
				if (S[i][j] == '1') t = 1;
				
				wp[i][j] = (Win[i] - t)/ (long double)(Lose[i] + Win[i] - 1);
			}
		}
		for (i = 1; i <= N; i++) {
			opp = s = 0;
			for (j = 1; j <= N; j++) {
				if (S[i][j] != '.') {
					s += wp[j][i];
				}
			}
			owp[i] = s / (long double)(Lose[i] + Win[i]);
		}

		printf ("Case #%d:\n", t);
		for (i = 1; i <= N; i++) {
			s = 0;
			for (j = 1; j <= N; j++) {
				if (S[i][j] != '.') 
					s += owp[j];
			}
			
			oowp[i] = s /(long double)(Lose[i] + Win[i]);
			//printf ("s de boss %Lf\n", s);
			//printf ("%d %Lf %Lf %Lf\n", i, wp[i][0], owp[i], oowp[i]);
			long double res = 0.25 * wp[i][0] + 0.50 * owp[i] + 0.25 * oowp[i];
			printf ("%Lf\n", res);
		}
	}
				
	return 0;
}
					
