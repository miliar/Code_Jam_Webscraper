#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))

#define MAXN 1001

int sieve[MAXN];
vi prime;
int tc, A, B, P;
int s[MAXN];
int used[MAXN];

int find(int x)
{
	if (s[x] != x) s[x] = find(s[x]);
	return s[x];
}
void uni(int x, int y)
{
	int xr = find(x);
	int yr = find(y);
	s[xr] = yr;
}

int main()
{
	int t, i,j,k;
	FORI(i, 2, 1000)
		if (!sieve[i])
		{
			for (j = i + i; j <= 1000; j+=i) sieve[j] = 1;
			prime.push_back(i);
		}
//	fprintf(stderr, "ok\n");
	scanf("%d", &tc);
	FOR(t, tc)
	{
		scanf("%d %d %d", &A, &B, &P);
		FORI(i, A, B) s[i] = i;
		ZERO(used);
		FOR(i, prime.size())
			if (prime[i] >= P)
			{
				FORI(j, A, B)
				{
					FORI(k, j+1, B)
						if (j % prime[i] == 0 && k % prime[i] == 0) 
							uni(k, j);
				}
			}
		k = 0;
		FORI(i, A, B) if (s[i] == i) { /*printf("%d\n", i);*/ k++; }
		printf("Case #%d: %d\n", t + 1, k);
	}
	return 0;
}

