#include <stdio.h>
#include <math.h>

bool Solve(int *S, int P, int N)
{
	int flag = false;
	int S_flag = false;
	for (int i=0; i<=30; i++) {
		for (int k=0; k<=30; k++) {
			for (int m=0; m<=30; m++) {
				if (i+k+m != N)
					continue;

				if (i < P && k < P && m < P)
					continue;

				int a = abs(i-k);
				int b = abs(k-m);
				int c = abs(m-i);

				if (a > 2 || b > 2 || c > 2)
					continue;

				if (a == 2 || b == 2 || c == 2)
					S_flag = true;
				else
					flag = true;
			}
		}
	}

	if (flag == true)
		return true;

	if (S_flag == true) {
		if (*S > 0) {
			*S = *S - 1;

			return true;
		}
	}

	return false;
}

int main()
{
	FILE *fp = fopen("B-large.in", "r");
	FILE *fout = fopen("output.txt", "w");

	int T;

	fscanf(fp, "%d", &T);
	for (int i=0; i<T; i++) {
		int N, S, P;
		fscanf(fp, "%d %d %d", &N, &S, &P);

		int result=0;
		for (int i=0; i<N; i++) {
			int temp;
			fscanf(fp, "%d", &temp);

			if (Solve(&S, P, temp) == true)
				result++;
		}

		fprintf(fout, "Case #%d: %d\n", i+1, result);
	}

	return 0;
}