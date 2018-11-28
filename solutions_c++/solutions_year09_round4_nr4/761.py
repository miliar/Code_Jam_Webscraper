#include<stdio.h>
#include<math.h>

int testcase, t;
int n, max_r;

typedef struct
{
    int x, y;
    int r;
}point;

point paint[50];

double get_ans(int ti, int tj)
{
    double tx, ty, dist;
    tx = paint[ti].x - paint[tj].x;
    ty = paint[ti].y - paint[tj].y;
    dist = sqrt(1.0 * tx * tx + ty * ty);
    return (paint[ti].r + paint[tj].r + dist) / 2.0;
}
int main()
{
    scanf("%d", &testcase);
    double ans, tmp;
    int i, j;
    for(t = 1; t <= testcase; t ++)
    {
        scanf("%d", &n);
        max_r = 0;
        for(i = 0; i < n; i ++)
        {
            scanf("%d%d%d", &(paint[i].x), &(paint[i].y), &(paint[i].r));
            if(paint[i].r > max_r)
                max_r = paint[i].r;
        }
        if(n < 3)
            printf("Case #%d: %d\n", t, max_r);
        else
        {
            ans = 1000000.0;
            for(i = 0; i < n; i ++)
                for(j = i + 1; j < n; j ++)
                {
                    tmp = get_ans(i, j);
                    if(tmp < ans)
                        ans = tmp;
                }
            if(ans < max_r)
                ans = max_r;
            printf("Case #%d: %.7lf\n", t, ans);
        }
    }
    return 0;
}
