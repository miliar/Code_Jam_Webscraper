#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 100;

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        int a[MAXN];
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
        {
            char s[100];
            scanf("%s", s);
            a[i] = 0;
            for (int j = n - 1; j >= 0; j--)
                if (s[j] == '1')
                {
                    a[i] = j;
                    break;
                }
        }
        int res = 0;
        for (int i = 0; i < n; i++)
        {
            if (a[i] > i)
            {
                for (int j = i + 1; j < n; j++)
                    if (a[j] <= i)
                    {
                        for (int k = j - 1; k >= i; k--)
                        {
                            swap(a[k], a[k + 1]);
                            res++;
                        }
                        break;
                    }
            }
        }
/*        for (int i = 0; i < n; i++)
        {
            if (a[i] > i)
            {
                bool flag = false;
                for (int j = i + 1; j < n; j++)
                    if (a[j] <= i && a[i] <= j)
                    {
                        swap(a[i], a[j]);
                        res++;
                        flag = true;
                        break;
                    }
                if (flag)
                    continue;
                for (int j = i + 1; j < n; j++)
                    if (a[j] <= i)
                    {
                        swap(a[i], a[j]);
                        res++;
                        break;
                    }
            }
        }*/
        printf("Case #%d: %d\n", cas, res);
    }
    return 0;
}
