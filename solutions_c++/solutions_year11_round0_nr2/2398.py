#include <cstdio>
using namespace std;

#define INPUT "B-large.in"
#define OUTPUT "B-large.out"

#define NMAX 101

void solve()
{
	char C[26][26], D[26][26], S[NMAX], a, b, c;
	int n, k = -1;

	for(int i = 0; i < 26; ++i)
		for(int j = 0; j < 26; ++j)
			C[i][j] = D[i][j] = 0;

	scanf("%d", &n);
	while(n--)
	{
		scanf(" %c%c%c", &a, &b, &c);
		C[a - 'A'][b - 'A'] = C[b - 'A'][a - 'A'] = c;
	}

	scanf("%d", &n);
	while(n--)
	{
		scanf(" %c%c", &a, &b);
		D[a - 'A'][b - 'A'] = D[b - 'A'][a - 'A'] = 1;
	}

	scanf("%d ", &n);
	while(n--)
	{
		++k;
		scanf("%c", S + k);
		if(k == 0)
			continue;
		if(C[S[k] - 'A'][S[k - 1] - 'A'])
		{
			S[k - 1] = C[S[k] - 'A'][S[k - 1] - 'A'];
			--k;
			continue;
		}
		for(int i = 0; i < k; ++i)
			if(D[S[k] - 'A'][S[i] - 'A'])
			{
				k = -1;
				break;
			}
	}

	if(k == -1)
	{
		printf("[]\n");
		return;
	}

	printf("[");
	for(int i = 0; i < k; ++i)
		printf("%c, ", S[i]);
	printf("%c]\n", S[k]);
}

int main()
{
	int nt;

	freopen(INPUT, "r", stdin);
	freopen(OUTPUT, "w", stdout);

	scanf("%d", &nt);

	for(int t = 1; t <= nt; ++t)
	{
		printf("Case #%d: ", t);
		solve();
	}

	return 0;
}
