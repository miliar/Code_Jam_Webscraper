#include <iostream.h>
#include <math.h>

main()
{
	int ix, T, n, A, B, C, D, x0, y0, M, i, j, k;
	long long X[100000], Y[100000];
	long long Res;
	int BariX, BariY;

	cin >> T;

	for (ix = 1; ix <= T; ix++) {
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		Res = 0;

		X[0] = x0;
		Y[0] = y0;
		for (i = 1; i < n; i++) {
			X[i] = (A * X[i-1] + B) % M;
			Y[i] = (C * Y[i-1] + D) % M;
		}
		for (i = 0; i < n; i++)
			for (j = 0; j != i && j < n; j++)
				for (k = 0; k != i && k != j && k < n; k++) {
				BariX = (X[i]+X[j]+X[k]) % 3;
				BariY = (Y[i]+Y[j]+Y[k]) % 3;
				if (!BariX && !BariY) Res++;
		}

		cout << "Case #" << ix << ": ";
		cout << Res;
		cout << "\n";
	}
}
