#include <iostream.h>

int SaveUniv (int *Queries, int NQ, int L)
{
	int i, j, Nx;
	int X[100];
	int Switch = 0;
	int q;

	Nx = 0;
	for (i = 0; i < L; i++) X[i] = 0;

	for (i = 0; i < NQ; i++) {
		q = Queries[i];
		if (!X[q]) {
			Nx++;
			X[q]++;
		}
		if (Nx == L) {
			Switch++;
			Nx = 1;
			for (j = 0; j < L; j++) X[j] = 0;
			X[q]++;
		}
	}

	return Switch;
}

main()
{
	int ix, i, j, N, S, Q, Y;
	int Que[1000];
	char c;
	char Names[100][101];
	char Query[101];
	char Nichts[101];

	for (i = 0; i < 101; i++) Nichts[i] = '\0';

	cin >> N;


	for (ix = 1; ix <= N; ix++) {
		// preliminary cleaning
		for (i = 0; i < 100; i++) strcpy (Names[i], Nichts);
		strcpy (Query, Nichts);
		for (i = 0; i < 1000; i++) Que[i] = -1;

		cin >> S;
		cin.get (c);
		for (i = 0; i < S; i++) {
			cin.getline (Names[i], 101);
		}

		cin >> Q;
		cin.get (c);
		for (i = 0; i < Q; i++) {
			cin.getline (Query, 101);
			for (j = 0; j < S; j++) {
				if (!strcmp (Query, Names[j])) Que[i] = j;
			}
		}

		cout << "Case #" << ix << ": ";

		Y = SaveUniv (Que, Q, S);
		cout << Y << "\n";
	}
}
