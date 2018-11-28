#include <cstdio>
#include <algorithm>
using namespace std;

int yihuo(int x, int y)
{
    return (x | y) & (~(x & y));
}

unsigned int arr[1005];

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T, C;
    scanf("%d", &T);
    int cnt = 0;

    while(T--)
    {
        cnt ++;
        scanf("%d", &C);

        unsigned int ret = 0;
        unsigned int min_v = 100000000;
        int sum = 0;
        for(int i = 0; i < C; ++ i)
        {
            scanf("%d", &arr[i]);
            ret = yihuo(ret, arr[i]);

            sum += arr[i];
            if(arr[i] < min_v)
            {
                min_v = arr[i];
            }
        }



        if(ret)
        {
            printf("Case #%d: NO\n", cnt);
        }
        else
        {
            printf("Case #%d: %d\n", cnt, sum - min_v);
        }
    }
    return 0;
}
