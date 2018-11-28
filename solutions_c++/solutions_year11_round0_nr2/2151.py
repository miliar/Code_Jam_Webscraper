#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

void solve()
{
	int C, D, N;
	int comb[26][26];
	bool den[26][26];

	memset(comb, -1, sizeof(comb));
	memset(den, 0, sizeof(den));

	scanf("%d", &C);
	for (int i = 0; i < C; ++i)
	{
		char st[4];
		scanf("%s", &st[0]);

		comb[st[0]-'A'][st[1]-'A'] = st[2]-'A';
		comb[st[1]-'A'][st[0]-'A'] = st[2]-'A';
	}

	scanf("%d", &D);
	for (int i = 0; i < D; ++i)
	{
		char st[3];
		scanf("%s", &st[0]);

		den[st[0]-'A'][st[1]-'A'] = true;
		den[st[1]-'A'][st[0]-'A'] = true;
	}

	char seq[101];
	scanf("%d%s", &N, &seq[0]);

	int q[100], sz = 0;
	for (int i = 0; i < N; ++i)
	{
		q[sz++] = seq[i]-'A';
		while (sz > 1 && comb[q[sz-1]][q[sz-2]] != -1)
		{
			q[sz-2] = comb[q[sz-1]][q[sz-2]]; --sz;
		}

		for (int j = 0; j < sz; ++j)
			if (den[q[j]][q[sz-1]]) { sz = 0; break; }
	}

	printf("[");
	for (int i = 0; i < sz; ++i)
	{
		printf("%c", (char)(q[i]+'A'));
		if (i+1 < sz) printf(", ");
	}

	printf("]\n");
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

    return 0;
}
