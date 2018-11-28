#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int main() {
	int T;
	scanf("%d", &T);

	for (int caso = 1; caso <= T; caso++) {
		int N;

		scanf("%d", &N);

		int tab[N][N];
		vector <double> WP(N,0), WP2(N,0), OWP(N,0), OOWP(N,0);
		vector <int> vict(N,0), opp(N,0);

		getchar(); // \n
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				char c;
				switch(c = getchar()) {
					case '1':
						tab[i][j] = 1;
						break;
					case '0':
						tab[i][j] = 0;
						break;
					case '.':
						tab[i][j] = -1;
						break;
				}
			}
			getchar(); // \n
		}

		for (int i = 0; i < N; i++) {
			double sum = 0;
			int qty = 0;

			for (int j = 0; j < N; j++) {
				if (tab[i][j] != -1) {
					sum += tab[i][j];
					qty++;
					if (tab[i][j] == 1)
						vict[i]++;
				}
			}

			opp[i] = qty;
			WP[i] = sum / qty;
		}

		for (int i = 0; i < N; i++) {
			double sum = 0;
			int qty = 0;

			for (int j = 0; j < N; j++) {
				if (tab[i][j] == 1) {
					sum += (double) ((double) vict[j] / (double) (opp[j]-1));
					qty++;
				}
				else if (tab[i][j] == 0) {
					sum += (double) ((double) (vict[j]-1) / (double) (opp[j]-1));
					qty++;
				}
			}

			OWP[i] = (double) ((double) sum / (double) qty);
		}

		for (int i = 0; i < N; i++) {
			double sum = 0;

			for (int j = 0; j < N; j++) {
				if (tab[i][j] != -1) {
					sum += OWP[j];
				}
			}

			OOWP[i] = sum / opp[i];
		}

		printf("Case #%d:\n", caso);
		for (int i = 0; i < N; i++) {
//printf("OWP: %lf\n", OWP[i]);
			printf("%.12lf\n", (0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i]));
		}
	}

	return 0;
}
