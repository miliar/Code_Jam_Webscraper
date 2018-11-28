#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <stack>
#include <string>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

#define FOR(i, k, n) for(int i = (k); i < (n); i++)
#define FORZ(i, n) FOR(i, 0, n)
#define pb push_back
#define sz(x) x.size()
#define all(x) x.begin(), x.end()
#define cl(x) memset(x, 0, sizeof(x))

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, N, M;
	long long A;
	scanf("%d", &n);
	FORZ(i, n)
	{
		scanf("%d%d%lld", &N, &M, &A);
		A = A * A;
		N++;
		M++;
		printf("Case #%d: ", i + 1);
		FORZ(j, N)
			FORZ(k, M)
			{
				if(j != 0 || k != 0)
				{
					double a = sqrt(double(j) * j + k * k);
					FORZ(l, N)
						FORZ(m, M)
						{
							double b = sqrt(double(l) * l + m * m);
							double c = sqrt(double(j - l) * (j - l) + (m - k) * (m - k));
							double p = (a + b + c) / 2.0;
							if(fabs(double(A) - 4 * p * (p - a) * (p - b) * (p - c)) < 1e-6)
							{
								printf("%d %d %d %d %d %d\n", 0, 0, j, k, l, m);
								goto end;
							}
						}
					}
			}
		printf("IMPOSSIBLE\n");
end:	;
	}	
	return 0;
}