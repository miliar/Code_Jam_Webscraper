#include <stdio.h>
class TPoint
{
    public:
    int x, y;
    TPoint(int X = 0, int Y = 0)
    {
        x = X;
        y = Y;
    }
    bool test(int X, int Y)
    {
        return x>=0 && x<X && y>=0 && y<Y;
    }
};

TPoint k[4] = {TPoint(0, -1), TPoint(-1, 0), TPoint(1, 0), TPoint(0, 1)};

TPoint operator +(TPoint a, TPoint b)
{
    return TPoint(a.x + b.x, a.y + b.y);
}

int INF = 1000000000;

int main()
{
    int T, test;
    scanf("%d", &T);
    for (test = 1;test<=T;test++)
    {
        int Y, X, i, j, evel[100][100], st[100][100];

        for (i=0;i<100;i++)
            for (j=0;j<100;j++)
                st[i][j] = -1;

        scanf("%d%d", &Y, &X);

        for (i=0;i<Y;i++)
            for (j=0;j<X;j++)
                scanf("%d", &evel[i][j]);

        int colors = 0;
        for (i=0;i<Y;i++)
            for (j=0;j<X;j++)
                if (st[i][j] == -1)
                {
                    int Min, a, b;
                    TPoint curr(j, i), p, minPos;
                    bool f;
                    do
                    {
                        f = true;

                        if (st[curr.y][curr.x]==-1)
                        {
                            st[curr.y][curr.x] = colors;
                        }
                        else
                        {
                            for (a=0;a<Y;a++)
                                for (b=0;b<X;b++)
                                    if (colors==st[a][b]) st[a][b] = st[curr.y][curr.x];
                            break;
                        }

                        Min = evel[curr.y][curr.x];
                        for (a=0;a<4;a++)
                        {
                            p = curr + k[a];
                            if (p.test(X, Y) && evel[p.y][p.x]<Min)
                            {
                                Min = evel[p.y][p.x];
                                minPos = p;
                            }
                        }

                        if (Min<evel[curr.y][curr.x])
                            curr = minPos;
                        else
                        {
                            colors++;
                            break;
                        }

                    }
                    while(f);
                }
        printf("Case #%d:\n", test);
        for (i=0;i<Y;i++)
        {
            for (j=0;j<X;j++)
            {
                if (j) printf(" ");
                printf("%c", st[i][j] + 'a');
            }
            printf("\n");
        }
    }

    return 0;
}
