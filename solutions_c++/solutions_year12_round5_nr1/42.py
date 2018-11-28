#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

int n;
int nt;
int L[1000], P[1000], o[1000];

bool cmp(int i, int j)
{
	/*if (P[i] != P[j]) return P[i] > P[j];
	if (P[i] == 0) return i < j;
	if (L[i] != L[j]) return L[i] < L[j];*/

	int ci = 100 * L[i] + L[j] * (100 - P[i]);
	int cj = 100 * L[j] + L[i] * (100 - P[j]);

	if (ci != cj) return ci < cj;

	return i < j;
}

int main()
{
	scanf("%d", &nt);
	
	for(int tt = 1; tt <= nt; tt++)
	{	
		printf("Case #%d: ", tt);
		
		scanf("%d", &n);
		
		for(int i = 0; i < n; i++) scanf("%d", &L[i]);
		for(int i = 0; i < n; i++) { scanf("%d", &P[i]); o[i] = i;}

		sort(o, o + n, cmp);

		for(int i = 0; i < n; i++)
		{
			if (i) printf(" ");
			printf("%d", o[i]);
		}
		puts("");
	}
	
	return 0;
}
