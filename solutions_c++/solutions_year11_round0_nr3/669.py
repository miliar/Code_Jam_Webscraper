#include <cstdio>

void Open() {
	freopen ("Candy.in", "r", stdin);
	freopen ("Candy.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void Calc(int caseNo) {
	int N, tmp = 0, minv = (int)1e7, answer = 0;
	int *candy = new int[10000];
	scanf ("%d", &N);
	for (int i = 0; i < N; i++) {
		scanf ("%d", &candy[i]);
		tmp = candy[i] ^ tmp;
		if (candy[i] < minv) minv = candy[i];
		answer += candy[i];
	}

	if (tmp == 0) 
		printf ("Case #%d: %d\n", caseNo, answer - minv);
	else
		printf ("Case #%d: NO\n", caseNo);

	delete[] candy;
}

void Work() {
	int T;
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++)
		Calc(caseNo);
}

int main() {
	Open();
	Work();
	Close();
}
