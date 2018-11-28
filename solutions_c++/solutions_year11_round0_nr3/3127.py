#include <cstdio>
#include <fstream>
using namespace std;

const int N = 1010;
const int INF = 99999999;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n;
    scanf("%d", &t);
    for (int k = 1; k <= t; k++)
    {
        scanf("%d", &n);
        int tmp, minnum = INF, sumd = 0, sumb = 0;
        while (n--)
        {
            scanf("%d", &tmp);
            sumb ^= tmp;
            sumd += tmp;
            if (minnum > tmp)
                minnum = tmp;
        }
        printf("Case #%d: ", k);
        if (sumb != 0)
            printf("NO\n");
        else printf("%d\n", sumd - minnum);
    }
}
