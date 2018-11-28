#include <iostream>
#include <stdlib.h>

using namespace std;

int h[][2] =
{
{ -1, 0 },
{ -1, 1 },
{ 2, 1 },
{ 2, 1 },
{ 2, 2 },
{ 3, 2 },
{ 3, 2 },
{ 3, 3 },
{ 4, 3 },
{ 4, 3 },
{ 4, 4 },
{ 5, 4 },
{ 5, 4 },
{ 5, 5 },
{ 6, 5 },
{ 6, 5 },
{ 6, 6 },
{ 7, 6 },
{ 7, 6 },
{ 7, 7 },
{ 8, 7 },
{ 8, 7 },
{ 8, 8 },
{ 9, 8 },
{ 9, 8 },
{ 9, 9 },
{ 10, 9 },
{ 10, 9 },
{ 10, 10 },
{ -1, 10 },
{ -1, 10 }
};

int cmp (const void *a, const void *b) {

	return *(int*)a - *(int*)b;
}

int main () {

	int i, j, t, n, s, p;
	int v[100], nro, teste;

	cin >> t;
	teste = 1;
	while (t-- > 0) {
		cin >> n >> s >> p;
		for (i = 0; i < n; i++)
			cin >> v[i];
		qsort(v, n, sizeof(int), cmp);
		nro = 0;
		for (i = 0; i < n && s > 0; i++)
			if (h[v[i]][0] >= p) {
				s--;
				v[i] = -1;
				nro++;
			}

		if (s > 0) {
			for (i = 0; i < n; i++)
				if (v[i] != -1 && h[v[i]][0] == -1)
					v[i] = -1;
		}
		for (i = 0; i < n; i++)
			if (v[i] != -1 && h[v[i]][1] >= p)
				nro++;
		cout << "Case #" << teste++ << ": " << nro << endl;
	}

	return 0;
}
