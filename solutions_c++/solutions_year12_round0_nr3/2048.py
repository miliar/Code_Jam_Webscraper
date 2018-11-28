#include <cstdlib>
#include <cstdio>
#include <set>

#define max(x, y) ((x) > (y) ? (x) : (y))

const int MAX_SIZE = 20;
char v[MAX_SIZE];

unsigned int solve(const int a, const int b) 
{
	register unsigned int count = 0, wrChars, nSize;
	register int q, n, m;
	
	for (m = max(11, a+1); m <= b; m++)
	{
		std::set<int> cache;
		wrChars = sprintf(v, "%d%d", m, m);
		nSize = wrChars/2;
		for (q = nSize-1; q > 0; q--)
		{
			v[--wrChars] = '\0';
			if (v[q] != '0') {
				n = atoi(v+q);
				if (a <= n && n < m && cache.insert(n).second)
					count++;
			}
		}
	}
	return count;
}

int main()
{
	int cases;
	scanf("%d", &cases);
	for (int c = 1; c <= cases; c++)
	{
		int a, b;
		scanf("%d%d", &a, &b);
		printf("Case #%d: %u\n", c, solve(a, b));
	}
	return 0;	
}

