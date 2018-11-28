#define _CRT_SECURE_NO_DEPRECATE

#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

typedef vector<int> vi;

vi freq;
int P, K, L;

int main(void)
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int N;
	scanf("%d", &N);
	for (int case_num = 1; case_num <= N; case_num++)
	{
		scanf("%d%d%d", &P, &K, &L);
		freq.resize(L);
		for (int i = 0; i < L; i++)
		{
			scanf("%d", &freq[i]);
		}
		sort(freq.begin(), freq.end(), greater<int>());
		long long res = 0;
		for (int i = 0; i < L; i++)
		{
			res += (i/K + 1) * freq[i];
		}
		printf("Case #%d: %I64d\n", case_num, res);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
