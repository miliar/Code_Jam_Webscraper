#include <cstdio>
#include <cstdlib>
#include <cstring>

#define MAXN 1000

using namespace std;

int n;
int a[MAXN + 1], b[MAXN + 1];
void Solve(int id)
{
    scanf("%d", &n);
    for (int i = 1; i <= n; i ++)
	scanf("%d%d", &a[i], &b[i]);
    int ans = 0;
    for (int i = 1; i <= n; i ++)
    {
	for (int j = 1; j < i; j ++)
	{
	    ans += ((a[i] > a[j]) ^ (b[i] > b[j]));
	}
    }
    printf("Case #%d: %d\n", id, ans);
}

int main()
{
    freopen("1.in", "r", stdin);
    freopen("1.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++)
	Solve(i);
    return 0;
}

