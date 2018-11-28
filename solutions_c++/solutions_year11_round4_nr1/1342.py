#include<stdio.h>
#include<stdlib.h>
typedef struct tnode
{
    int sta, end;
    int w;
}node;

node A[1010];
int cmp(const void *a, const void *b)
{
    node *ta, *tb;
    ta = (node *)a; tb = (node *)b;
    return (ta -> w) - (tb -> w);
}

int main()
{
    int T, X, S, R, N, sum, test, i;
    double ans, len, t;
    scanf("%d", &T);
    for(test = 1; test <= T; test ++)    
    {
        scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);
        sum = 0;
        for(i = 0; i < N; i ++){
            scanf("%d%d%d", &(A[i].sta), &(A[i].end), &(A[i].w));
            sum = sum + A[i].end - A[i].sta;
        }
        A[N].sta = 0; A[N].end = X - sum; A[N].w = 0;
        N ++;
        qsort(A, N, sizeof(node), cmp);
        ans = 0;
        for(i = 0; i < N; i ++)
        {
            len = A[i].end - A[i].sta;
            if(len / (A[i].w + R) < t)
            {
                t -= len / (A[i].w + R);
                ans += len / (A[i].w + R);
            }
            else
            {
                ans = ans + t + (len - t * (A[i].w + R)) / (A[i].w + S);
                t = 0;
                i ++;
                break;
            }
        }
        for(; i < N; i ++)
        {
            len = A[i].end - A[i].sta;
            ans = ans + len / (A[i].w + S);
        }
        printf("Case #%d: %.8lf\n", test, ans);
    }
    return 0;
}
