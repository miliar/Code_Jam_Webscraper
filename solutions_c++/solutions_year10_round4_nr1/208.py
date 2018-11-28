#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char d[102][102];

int size;

inline int caz(int i, int j)
{
    return i < 0 || j < 0 || i > 101 || j > 101 ? -1 : d[i][j];
}

inline int cor(int c1, int c2)
{
    return c1 == -1 ? c2 : c2 == -1 ? c1 : c1 == c2 ? c1 : -2;
}

inline int testcenter(int i, int j)
{
    int size2 = size + abs(i - size + 1) + abs(j - size + 1);
    //printf("tc\t%d\t%d\t%d\n", i, j, size2);
    for (int di = 0 ; di < size2 ; di++)
        for (int dj = 0 ; dj < size2 ; dj++)
            {
                int c = -1;
                c = cor(c, caz(i - di, j - dj));
                c = cor(c, caz(i + di, j - dj));
                c = cor(c, caz(i - di, j + dj));
                c = cor(c, caz(i + di, j + dj));
                if (c == -2)
                    return 99999999;
            }
    return size2*size2 - size*size;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1 ; t <= T ; t++)
        {
            scanf("%d", &size);
            memset(d, -1, sizeof(d));
            int c;
            for (int i = 0 ; i < size ; i++)
                {
                    for (int j = 0 ; j <= i ; j++)
                        {
                            scanf("%d", &c);
                            d[i][size-i-1+2*j] = c;
                            //printf("%d ", c);
                        }
                    //puts("");
                }
            for (int i = size - 2 ; i >= 0 ; i--)
                {
                    for (int j = 0 ; j <= i ; j++)
                        {
                            scanf("%d", &c);
                            d[2*(size-1)-i][size-i-1+2*j] = c;
                            //printf("%d ", c);
                        }
                    //puts("");
                }
            //            for (int i = 0 ; i < size * 2 - 1 ; i++)
            //  for (int j = 0 ; j < size * 2 - 1 ; j++)
            //      printf("%-d%c", d[i][j], j < size*2-2?' ':'\n');
            int res = 9999999;
            for (int i = 0 ; i < 2*size-1 ; i++)
                for (int j = 0 ; j < 2*size-1 ; j++)
                    res = min(res, testcenter(i, j));
            printf("Case #%d: %d\n", t, res);
        }
}
