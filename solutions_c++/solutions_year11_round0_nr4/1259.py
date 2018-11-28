#include <iostream>
 
int main()
{
        int testnum;
        scanf("%d", &testnum);
        for (int tc = 0; tc < testnum; tc++)
        {
                int n;
                scanf("%d", &n);
                int res = 0;
                for (int i = 0; i < n; i++)
                {
                        int p;
                        scanf("%d", &p);
                        res += p != i + 1;
                }
                printf("Case #%d: %d\n", tc + 1, res);
        }
        return 0;
}