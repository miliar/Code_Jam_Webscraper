#include <iostream.h>
#include <math.h>

#define NMAX 1000

void VSort (int *vns, int *vs, int n)
{
	int i, j, x[NMAX], vmin, jmin;

	for (i = 0; i < n; i++) x[i] = 0;

	for (i = 0; i < n; i++) {	// vs[i]
		jmin = -1;
		for (j = 0; j < n; j++) {
			if (!x[j]) {	// if x, I can do nothing
				if (jmin == -1 || vns[j] < vmin) {
					jmin = j;
					vmin = vns[j];
				}
			}
		}
		vs[i] = vmin;
		x[jmin] = 1;
	}
}

main()
{
	int ix, N, P, K, L, i, ip, ik;
	int Freq[NMAX], Fs[NMAX];
	long long Res;

	cin >> N;

	for (ix = 1; ix <= N; ix++) {
		cin >> P >> K >> L;

		for (i = 0; i < L; i++) cin >> Freq[i];

		VSort (Freq, Fs, L);
		Res = 0;
		for (i = 0; i < L; i++) {
			ip = i/K;
			ik = i%K;
			Res += (1+ip)*Fs[L-1-ik-ip*K];
		}

		cout << "Case #" << ix << ": ";
		cout << Res;
		cout << "\n";
	}
}
