#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

int P, K, L;
int freq[1005];
vector<int> ans[1005];

int cmp(const void *a, const void *b) {
	int *aa = (int *)a;
	int *bb = (int *)b;
	if (*bb < *aa) return -1;
	else if (*bb == *aa) return 0;
	else return 1;
}

void init() {
	for (int i = 0; i < 1005; i++) ans[i].clear();
}

int main()
{
	int kase, numOfCase;
	cin >> numOfCase;
	for (kase = 1; kase <= numOfCase; kase++) {
		int i, j;
		cin >> P >> K >> L;
		init();
		for (i = 0; i < L; i++) cin >> freq[i];
		qsort(freq, L, sizeof(int), cmp);

		j = 0;
		for (i = 0; i < L; i++) {
			ans[j].push_back(freq[i]);
			j = (j + 1) % K;
		}

		long long result = 0;
		for (i = 0; i < K; i++)
			for (j = 0; j < ans[i].size(); j++)
				result += ans[i][j] * (j + 1);

		cout << "Case #" << kase << ": " << result << endl;
	}
return 0;
}

