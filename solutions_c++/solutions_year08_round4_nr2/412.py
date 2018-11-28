#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iostream>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define DBG(a) cerr << a << endl;
#define DEBUG 1

int tc, n, m, a, nm;
int x1, x2, x3, y1, y2, y3;
int found;

int find(int a1, int b1, int a2, int b2, int a3) // find b3
{
	int tmp = 0, t1;
	
	// a +
	tmp = a1 * b2 + a3 * b1 - a2 * b1 - a3 * b2;
	t1 = a2 - a1;
//	fprintf(stderr, "Coba [%d, %d] [%d, %d] %d: %d %d\n", a1, b1, a2, b2, a3, tmp, t1);
	if (t1 && abs(a - tmp) % abs(t1) == 0 && ((a - tmp) / t1) >= 0 && ((a - tmp) / t1) < m) // yay
	{
		x1 = a1; x2 = a2; x3 = a3;
		y1 = b1; y2 = b2; y3 = (a - tmp) / t1;
		return 1;
	}

	// a -
	if (t1 && abs(-a - tmp) % abs(t1) == 0 && ((-a - tmp) / t1) >= 0 && ((-a - tmp) / t1) < m) // yay
	{
		x1 = a1; x2 = a2; x3 = a3;
		y1 = b1; y2 = b2; y3 = (-a - tmp) / t1;
		return 1;
	}
	
	return 0;
}

int main()
{
	int i,j,k,t;

	scanf("%d", &tc);
	FOR(t, tc)
	{
		found = 0;
		scanf("%d %d %d", &n, &m, &a); 
		if (a <= n * m)
		{
			n++; m++;
			nm = n * m;
			FOR(i, nm)
				FORI(j, i + 1, nm - 1)
					FOR(k, n)
					{
						found = find(i % n, i / n, j % n, j / n, k);
						if (found) goto done;
					}
		}
done:
		
		printf("Case #%d: ", t+1);
		if (!found) printf("IMPOSSIBLE\n");
		else printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
	}
	return 0;
}

