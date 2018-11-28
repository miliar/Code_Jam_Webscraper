#include <vector>
#include <string>
#include <algorithm>

using namespace std;


int mysort(vector <int> v) {
	int size = v.size();
	int count = 0;

	for (int i = 0; i < size-1; i++) {
		if (v[i] <= i) continue;

		int j, ant = v[i];
		for (j = i+1; v[j] > i && j < size; j++) {
			int aux = v[j];
			v[j] = ant;
			ant = aux;
			count++;
		}
		count++;

		v[i] = v[j];
		v[j] = ant;
	}

	return count;
}


int main() {
	int T;
	scanf("%d", &T);

	for (int cases = 1; cases <= T; cases++) {
		int N;
		scanf("%d", &N);
		int ans = 0;
		vector <int> zeros(N, -1);
		getchar(); // \n

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				char c;
				c = getchar();

				if (c == '1')
					zeros[i] = j;
			}
			getchar(); // \n
		}

		ans = mysort(zeros);
		printf("Case #%d: %d\n", cases, ans);
	}

	return 0;
}
