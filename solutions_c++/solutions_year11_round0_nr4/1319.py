#include <cstdio>
using namespace std;

const int N = 1050;
int a[N];

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int testcase = 1; testcase <= T; testcase++)
    {
        int n;
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
            scanf("%d", &a[i]);
        int ret = 0;
        for (int i = 1; i <= n; i++)
        	if (a[i] != i)
        	{
        		ret++;
        	}
        printf("Case #%d: %d.000000\n", testcase, ret);
    }
}
