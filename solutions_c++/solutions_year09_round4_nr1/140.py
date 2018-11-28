#include <iostream>
#include <cstring>

using namespace std;

const int MaxN = 50;
const int Infinity = 100000000;

int TCase, N, S[MaxN], Ans;
char S1[MaxN];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &TCase);
	for (int Case = 1; Case <= TCase; Case++) {
		scanf("%d\n", &N);
		for (int i = 1; i <= N; i++) {
			S[i] = 0;
			gets(S1);
			for (int j = 0; j < N; j++)
				if (S1[j] == '1') S[i] = j + 1;
		}
		Ans = 0;
		for (int i = 1; i <= N; i++)
		{
			int j;
			for (j = i; j <= N; j++)
				if (S[j] <= i) break;
			int Tmp = S[j];
			for (int k = j; k > i; k--) S[k] = S[k - 1];
			S[i] = S[j];
			Ans += j - i;
		}
		printf("Case #%d: %d\n", Case, Ans);
	}
	return 0;
}
