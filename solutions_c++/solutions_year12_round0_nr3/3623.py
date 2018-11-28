#include <cstdio>
#include <cstdlib>
#include <string.h>

int movenum(int number, int from)
{
    char tnumber[10];
    char treturn[10];
    itoa(number, tnumber, 10);
    int size = strlen(tnumber);
    int x = 0;
    for (int i = from; i < size; i++)
    {
        treturn[x] = tnumber[i];
        x++;
    }
    for (int j = 0; j < from; j++)
    {
        treturn[x] = tnumber[j];
        x++;
    }
    return atoi(treturn);
}

int main(int argc, char *argv[])
{
    freopen("C:\\input.in", "r", stdin);
    freopen("C:\\result.out", "w", stdout);
    int linhas;
    scanf("%d\n", &linhas);
    for (int l = 1; l <= (int)linhas; l++)
    {
        int a, b, x, r = 0, t;
        scanf("%d %d\n", &a, &b);
        char jt[8];
        itoa(a, jt, 10);
        x = strlen(jt);
        for (int i = b; i > a; i--)
        {
            for (int j = a; j < b; j++)
            {
                for (int k = 1; k < x; k++)
                {
                    t = movenum(j, k);
                    if (t == i)
                    {
                        r++;
                        break;
                    }
                }
            }
            b--;
        }
        printf("Case #%d: %d\n", l, r);
    }
    return 0;
}
