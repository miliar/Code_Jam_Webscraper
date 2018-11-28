#include <cstdio>

void Open() {
	freopen ("GoroSort.in", "r", stdin);
	freopen ("GoroSort.out", "w", stdout);
}

void Close() {
	fclose(stdin);
	fclose(stdout);
}

void Calc(int caseNo) {
	int N, num[10000], answer = 0;
	bool visited[10000];
	scanf ("%d", &N);
	for (int i = 0; i < N; i++) 
		scanf ("%d", &num[i]), num[i]--;
	
	for (int i = 0; i < N; i++) visited[i] = 0;

	for (int i = 0; i < N; i++) {
		if (visited[i]) continue;
		int j = i, count = 0;
		while (!visited[j]) {
			visited[j] = 1;
			j = num[j];
			count++;
		}
		if (count > 1) answer += count;
	}

	printf ("Case #%d: %0.6lf\n", caseNo, (double)answer);
}

void Work() {
	int T;
	scanf ("%d", &T);
	for (int caseNo = 1; caseNo <= T; caseNo++) {
		Calc(caseNo);
	}
}

int main() {
	Open();
	Work();
	Close();
	return 0;
}
