#include <iostream>

using namespace std;

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int test, n, i, j, cnt, cs=1, a[1005], b[1005], x, y, mx;
    scanf("%d", &test);
    while(test--)
    {
        scanf("%d", &n);
        for(i=0;i<n;i++)
        {
            scanf("%d %d", &a[i], &b[i]);
        }
        cnt=0;
        mx=0;
        for(i=0;i<n;i++)
        {
            cnt=0;
            for(j=0; j<n; j++)
            {
                if(i==j)continue;
                if((a[i]>a[j] && b[i]<b[j])||(a[i]<a[j] && b[i]>b[j]))
                cnt++;
            }
            if(cnt>mx)
            mx=cnt;
        }
        printf("Case #%d: %d\n", cs++, mx);
    }
    return 0;
}

