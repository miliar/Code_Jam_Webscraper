#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
	FILE *fin = fopen("A-large.in", "r");
	int N;
	fscanf(fin, "%d", &N);
	FILE *fout = fopen("A-large.out", "w");
	for(int i = 0; i < N; i++) {
		int n, A, B, C, D, x0, y0, M;
		fscanf(fin, "%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		int X = x0, Y = y0;
		int m[10];
		for(int j = 0; j < 9; j++)
			m[j] = 0;
		for(int j = 0; j < n; j++) {
			//cout << X << " " << Y << endl;
			m[X % 3 + 3 * (Y % 3)]++;
			X = ((long long)A * X + B) % M;
  			Y = ((long long)C * Y + D) % M;
		}
		long long b = 0;
		for(int i1 = 0; i1 < 9; i1++)
			for(int i2 = 0; i2 < 9; i2++)
				for(int i3 = 0; i3 < 9; i3++)
					if(((i1 % 3 + i2 % 3 + i3 % 3) % 3 == 0) && ((i1 / 3 + i2 / 3 + i3 / 3) % 3 == 0)) {
						if(i1 == i2 && i2 == i3)
							b += (long long)m[i1] * (m[i1] - 1) * (m[i1] - 2);
						else {
							if(i1 == i2)
								b += (long long)m[i1] * (m[i1] - 1) * m[i3];
							if(i2 == i3)
								b += (long long)m[i2] * (m[i2] - 1) * m[i1];
							if(i3 == i1)
								b += (long long)m[i1] * (m[i1] - 1) * m[i2];
						}
						if(i1 != i2 && i2 != i3 && i3 != i1)
							b += (long long)m[i1] * m[i2] * m[i3];
					}
		b /= 6;
		fprintf(fout, "Case #%d: %I64d\n", i + 1, b);
	}
	fclose(fin);
	fclose(fout);
	//system("pause");
	return 0;
}
