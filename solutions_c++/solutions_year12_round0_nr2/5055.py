#include<stdio.h>

int main()
{
    int t;
    int n, s, p;
    int tt, i;
    int c;
    int ans, point, tp;

    freopen("B-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);

    scanf("%d", &t);
    for( tt = 1; tt <= t; tt++)
    {
        scanf("%d %d %d", &n, &s, &p);
        c = 0;
        ans = 0;

        for( i = 1; i <= n; i++)
        {
            scanf("%d", &point);
            tp = point / 3;

            if( point % 3 != 0)tp++;

            if( tp >= p)ans++;
            else if( tp + 1 >= p && c < s && point >= 2)
            {
                c++;
                ans++;
            }
        }
        printf("Case #%d: %d\n", tt, ans);
    }
}
