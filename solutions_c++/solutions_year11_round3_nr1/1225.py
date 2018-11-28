#include <vector>
#include <string>
#include <algorithm>

using namespace std;



bool right(vector <vector <int> > tab2, int R, int C) {
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			if (tab2[i][j] == 0) {
				if (tab2[i][j+1] != 1 || tab2[i+1][j] != 2 || tab2[i+1][j+1] != 3)
					return false;
			}
		}
	}

	return true;
}

int main() {
	int T;
	scanf("%d", &T);

	for (int caso = 1; caso <= T; caso++) {
		int R, C;
		scanf("%d %d", &R, &C);

		vector <vector <char> > tab(R, vector <char> (C));
		vector <vector <int> > tab2(R, vector <int> (C));

		getchar(); //\n
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				tab[i][j] = getchar();
				tab2[i][j] = -1;
			}
			getchar(); //\n
		}

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (tab[i][j] == '#') {
					if (j > 0 && tab2[i][j-1] == 0) {
						tab[i][j] = '\\';
						tab2[i][j] = 1;
					}
					else if (i > 0 && tab2[i-1][j] == 0) {
						tab[i][j] = '\\';
						tab2[i][j] = 2;
					}
					else if (i > 0 && tab2[i-1][j] == 1) {
						tab[i][j] = '/';
						tab2[i][j] = 3;
					}
					else {
						tab[i][j] = '/';
						tab2[i][j] = 0;
					}
				}
			}
		}

		printf("Case #%d:\n", caso);
		if (!right(tab2, R, C)) {
			printf("Impossible\n");
		}
		else {
			for (int i = 0; i < R; i++) {
				for (int j = 0; j < C; j++) {
					printf("%c", tab[i][j]);
				}
				printf("\n");
			}
		}
	}

	return 0;
}
