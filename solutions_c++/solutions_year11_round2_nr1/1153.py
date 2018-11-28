#include <cstdio>

#define TRACE(x) 
#define PRINT(x...) TRACE(printf(x))

using namespace std;

int T, N;
char mat[110][110];
double WP[110];
double OWP[110];
double OOWP[110];
int win[110];
int lost[110];
int tot[110];

int main()
{
	scanf("%d", &T);
	for(int _42 = 1; _42 <= T; ++_42) {
		printf("Case #%d:\n", _42);
		scanf(" %d", &N);

		for(int i = 0; i < N; ++i) {
			scanf("%s", mat[i]);
		}

		for(int i = 0; i < N; ++i) {
			win[i] = 0;
			tot[i] = 0;
			for(int j = 0; j < N; ++j) {
				if(mat[i][j] == '.') continue;
				else if(mat[i][j] == '1') win[i]++;
				else lost[i]++;
				tot[i]++;
			}
			PRINT("%d/%d\n", win[i], tot[i]);
		}

		for(int i = 0; i < N; ++i) {
			WP[i] = win[i]/(double)tot[i];
			OWP[i] = 0;
			int ops = 0;
			for(int j = 0; j < N; ++j) {
				if(j == i) continue;
				if(mat[i][j] == '.') continue;
				int w = win[j];
				int t = tot[j]-1;
				if(mat[j][i] == '1') w--;
				PRINT("%d/%d ", w, t);
				OWP[i] += w/(double)t;
				ops++;
			}
			PRINT("\n");
			OWP[i]/=ops;
			PRINT("%lf %lf\n", WP[i], OWP[i]);
		}

		for(int i = 0; i < N; ++i) {
			OOWP[i] = 0;
			int ops = 0;
			for(int j = 0; j < N; ++j) {
				if(i == j) continue;
				if(mat[i][j] == '.') continue;
				OOWP[i] += OWP[j];
				ops++;
			}
			OOWP[i] /= ops;
		}

		for(int i = 0; i < N; ++i) {
			printf("%.10lf\n", 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]);
		}
		printf("\n");

	}
	return 0;
}
