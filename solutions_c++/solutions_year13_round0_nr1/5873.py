#include <cstdio>

int T, k = 1;

int main()
{
	for (scanf ("%d", &T); T--;)
	{
		int Xwin = 0, Owin = 0, Comp = 1;
		char f[11][11] = {};
		int N = 4;
		for (int i=0; i<N; i++) {
			scanf ("%s", f[i]);
			for (int j=0; j<N; j++) Comp &= (f[i][j] != '.');
		}
		for (int i=0; i<N; i++) {
			int lineX = 0, lineT = 0, lineO = 0;
			for (int j=0; j<N; j++) {
				lineX += (f[i][j] == 'X');
				lineT += (f[i][j] == 'T');
				lineO += (f[i][j] == 'O');
			}
			if ((lineX == 3 && lineT) || lineX == 4) {
				Xwin = 1;
			} else if ((lineO == 3 && lineT) || lineO == 4) {
				Owin = 1;
			}
		}
		for (int i=0; i<N; i++) {
			int lineX = 0, lineT = 0, lineO = 0;
			for (int j=0; j<N; j++) {
				lineX += (f[j][i] == 'X');
				lineT += (f[j][i] == 'T');
				lineO += (f[j][i] == 'O');
			}
			if ((lineX == 3 && lineT) || lineX == 4) {
				Xwin = 1;
			} else if ((lineO == 3 && lineT) || lineO == 4) {
				Owin = 1;
			}
		}
		int lineX = 0, lineT = 0, lineO = 0;
		lineX = 0, lineT = 0, lineO = 0;
		for (int i=0; i<N; i++) {
			lineX += (f[i][i] == 'X');
			lineT += (f[i][i] == 'T');
			lineO += (f[i][i] == 'O');
		}
		if ((lineX == 3 && lineT) || lineX == 4) {
				Xwin = 1;
			} else if ((lineO == 3 && lineT) || lineO == 4) {
				Owin = 1;
			}
		lineX = 0, lineT = 0, lineO = 0;
		for (int i=0; i<N; i++) {
			lineX += (f[i][3-i] == 'X');
			lineT += (f[i][3-i] == 'T');
			lineO += (f[i][3-i] == 'O');
		}
		if ((lineX == 3 && lineT) || lineX == 4) {
				Xwin = 1;
			} else if ((lineO == 3 && lineT) || lineO == 4) {
				Owin = 1;
			}
		printf ("Case #%d: ", k++);
		puts (!Owin && Xwin ? "X won" : !Xwin && Owin ? "O won" : Comp ? "Draw" : "Game has not completed");
	}
	return 0;
}