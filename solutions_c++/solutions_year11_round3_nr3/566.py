//acm header include 
#include<iostream>
#include<list>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("data.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    int T, t, n, l, h;
    int a[10000];

    scanf("%d", &T);
    for (t=1; t<=T;++t)
    {
        printf("Case #%d: ", t);
        scanf("%d %d %d", &n, &l, &h);
        for (int x = 0; x < n; ++x)
            scanf("%d" , &a[x]);
        int s;
        for (s = l; s <= h; ++s)
        {
            int i;
            for (i = 0; i < n; ++i)
            {
                if ((s % a[i]) == 0 || (a[i] % s) == 0)
                {
                    continue;
                }
                break;
            }
            if (i==n){
                printf("%d\n", s);
                break;
            }
        }
        if (s == h+1)
            printf("NO\n");
    }
	return 0;
}