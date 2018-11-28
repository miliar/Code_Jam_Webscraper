#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;


#define L first.first
#define P first.second

const int MAXN = 1007;

pair < pair <int, int>, int > a[MAXN];

bool opr_sort(const pair < pair <int, int>, int > &i, const pair < pair <int, int>, int > &j)
{
	return make_pair(i.L * j.P, i.second) < make_pair(j.L * i.P, j.second);
}

int main()
{
    freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);

    int test;
    scanf("%d", &test);
    for (int t = 1; t <= test; t++)
    {
    	printf("Case #%d:", t);
    	int n;
    	scanf("%d", &n);
    	for (int i = 0; i < n; i++) scanf("%d", &a[i].L);
    	for (int i = 0; i < n; i++) scanf("%d", &a[i].P);
    	for (int i = 0; i < n; i++) a[i].second = i;
    	sort(a, a + n, opr_sort);
    	for (int i = 0; i < n; i++)
    		printf(" %d", a[i].second);
    	printf("\n");
    }

    fprintf(stderr, "Time execute: %.3lf\n", clock() / (double)CLOCKS_PER_SEC);
    return 0;
}
