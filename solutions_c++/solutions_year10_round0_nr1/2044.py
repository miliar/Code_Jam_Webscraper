#include <cstdio>

bool calc(int n, int k)
{
	while (k && n)
	{
		if ((k & 1)==0)
			return false;
		k>>=1;
		n--;
	}
	return n == 0;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		bool b = calc(N,K);
		printf("Case #%d: ", t);
		if (b)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}