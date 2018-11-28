#include <iostream.h>

int Str2Time (char *c)
{
	return (c[0]-'0')*600 + (c[1]-'0')*60 + (c[3]-'0')*10 + c[4]-'0';
}

main()
{
	int ix, i, j, N, T, NA, NB;
	int A[1440], B[1440];
	int Amin, Bmin;
	char c;
	char Uhr1[6], Uhr2[6];
	int u1, u2;

	cin >> N;

	for (ix = 1; ix <= N; ix++) {
		cout << "Case #" << ix << ": ";
		for (i = 0; i<1440; i++) {
			A[i] = 0;
			B[i] = 0;
		}
		Amin = Bmin = 0;
		cin >> T >> NA >> NB;
		cin.get(c);

		for (i = 0; i < NA; i++) {
			cin.getline (Uhr1, 6, ' ');
			cin.getline (Uhr2, 6);
			u1 = Str2Time (Uhr1);
			u2 = Str2Time (Uhr2);
			for (j = u1; j < 1440; j++) A[j]--;
			for (j = u2+T; j < 1440; j++) B[j]++;
		}

		for (i = 0; i < NB; i++) {
			cin.getline (Uhr1, 6, ' ');
			cin.getline (Uhr2, 6);
			u1 = Str2Time (Uhr1);
			u2 = Str2Time (Uhr2);
			for (j = u1; j < 1440; j++) B[j]--;
			for (j = u2+T; j < 1440; j++) A[j]++;
		}

		for (i = 0; i<1440; i++) {
			if (A[i] < Amin) Amin = A[i];
			if (B[i] < Bmin) Bmin = B[i];
		}
		cout << -Amin << ' ' << -Bmin;
		cout << "\n";
	}
}
