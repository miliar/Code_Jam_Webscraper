#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int T, N, K;
	scanf("%d", &T);
	freopen("A.out", "w", stdout);
	for (int t = 0; t < T; t++)
	{
		scanf("%d%d", &N, &K);
		long long P = 1LL << N;
		string res;
		if (K % P == (P - 1))
			res = "ON";
		else
			res = "OFF";
		printf("Case #%d: %s\n", t + 1, res.c_str());
	}
	fclose(stdout);
	return 0;
}