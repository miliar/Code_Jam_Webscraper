#include <fstream>

using namespace std;

void rotiraj(int mapa[51][51], int n) {
	for (int a = 1; a <= n; a++) {
		int j = n;
		for (int b = n; b > 0; b--) {
			if (mapa[a][b] == 1 || mapa[a][b] == 2) {
				if (b!=j) {
					mapa[a][j] = mapa[a][b];
					mapa[a][b] = 0;
				}
				j--;
			}
		}
	}
}

bool provera(int mapa[51][51], int n, int k, int trazeni) {

	for (int a = 1; a <= n; a++) {
		int kolona = 0, red = 0;
		for (int b = 1; b <= n; b++) {
			if (mapa[a][b] == trazeni) {
				red++;
				if (red >= k) return true;
			} else red = 0;
			if (mapa[b][a] == trazeni) {
				kolona++;
				if (kolona >= k) return true;
			} else kolona = 0;
		}
	}

	int x = 1, y = 1;
	do {
		int d1 = 0;
		for (int i = x, j = y; (i > 0) && (j <= n); i--, j++) {
			if (mapa[i][j] == trazeni) {
				d1++;
				if (d1 >= k) return true;
			} else d1 = 0;
		}

		if (x < n) x++;
		else y++;
	} while (!((x==n)&&(y==n)));

	x = 1; y = n;
	do {
		int d1 = 0;
		for (int i = x, j = y; (i <= n) && (j <= n); i++, j++) {
			if (mapa[i][j] == trazeni) {
				d1++;
				if (d1 >= k) return true;
			} else d1 = 0;
		}

		if (y > 1) y--;
		else x++;
	} while (!((x==n)&&(y==1)));


	return false;
}

void main(int argc, char *argv[]) {
	if (argc!=3) exit(-1);

	ifstream ulaz(argv[1]);
	if (!ulaz) exit(-1);
	ofstream izlaz(argv[2]);
	if (!izlaz) exit(-1);
	
	int mapa[51][51];
	int t, k, n;
	char c;

	ulaz >> t;

	for (int i = 1; i <= t; i++) {
		ulaz >> n >> k;
		for (int a = 1; a <= n; a++)
			for (int b = 1; b <= n; b++) {
				ulaz >> c;
				switch (c) {
					case 'R': case 'r':
						mapa[a][b] = 1; break;
					case 'B': case 'b':
						mapa[a][b] = 2; break;
					default: mapa[a][b] = 0;
				}
			}
			izlaz << "Case #" << i << ": ";
		rotiraj(mapa, n);
		bool crveni = provera(mapa, n, k, 1), plavi = provera(mapa, n, k, 2);
		if (crveni) {
			if (plavi) izlaz << "Both";
			else izlaz << "Red";
		} else if (plavi) izlaz << "Blue";
		else izlaz << "Neither";
		izlaz << endl;
	}

	ulaz.close(); izlaz.close();
}