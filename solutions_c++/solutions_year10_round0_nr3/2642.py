#include <stdio.h>

int R, k, n, grpm[50], front, rear, q[10000];

void enq(int x)
{
    q[rear]=x;
    rear++;
}
int deq()
{
    int x;
    x = q[front];
    front++;
    return x;
}

int calc()
{
    int i, s, sum, p, c;

    //front = rear = 0;
    for(i=0;i<n;i++)
    {
        enq(grpm[i]);
    }
    sum=0;
    for(i=0;i<R;i++)
    {
        s=0;
        c=0;
        while(s+q[front]<=k && c<n)
        {
            c++;
            p = deq();
            s=s+p;
            enq(p);
        }
        sum+=s;
    }
    return sum;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C_small.out", "w", stdout);
    int test, cs=1, i, res;

    scanf("%d", &test);

    while(test--)
    {
        scanf("%d %d %d", &R, &k, &n);
        for(i=0;i<n;i++)
        {
            scanf("%d", &grpm[i]);
        }
        front = rear = 0;
        res = calc();

        printf("Case #%d: %d\n", cs++, res);
    }
    return 0;
}
