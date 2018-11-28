#include <stdio.h>
#include <string.h>
int width = 0;
int height = 0;
int current_label;
int source[102][102];
int dest[102][102];

int label(int i, int j)
{
    int a, b, c, d, e;
    if (dest[i][j] > 0)
    {
        return 0;
    }
    a = source[i - 1][j];
    b = source[i][j - 1];
    c = source[i][j + 1];
    d = source[i + 1][j];
    e = source[i][j];
    if (e <= a && e <= b && e <= c && e <= d)
    {
        dest[i][j] = current_label;
        current_label++;
    }
    else if (a <= b && a <= c && a <= d)
    {
        label(i - 1, j);
        dest[i][j] = dest[i - 1][j];
    }
    else if (b <= c && b <= d)
    {
        label(i, j - 1);
        dest[i][j] = dest[i][j - 1];
    }
    else if (c <= d)
    {
        label(i, j + 1);
        dest[i][j] = dest[i][j + 1];
    }
    else
    {
        label(i + 1, j);
        dest[i][j] = dest[i + 1][j];
    }
    return 0;
}
int cal(int case_n)
{
    scanf("%d%d", &height, &width);
    memset(source, 0x7f, sizeof(source));
    for (int i = 1; i <= height; i++)
        for (int j = 1; j <= width; j++)
        {
            scanf("%d", &source[i][j]);
        }

    current_label = 1;
    memset(dest, 0x00, sizeof(dest));
    for (int i = 1; i <= height; i++)
        for (int j = 1; j <= width; j++)
        {
            label(i, j);
        }
    for (int i = 1; i <= height; i++)
    {
        for (int j = 1; j <= width; j++)
        {
            if (j == width)
                printf("%c", 'a' + dest[i][j] - 1);
            else
                printf("%c ", 'a' + dest[i][j] - 1);
        }
        printf("\n");
    }

    return 0;
}

int main()
{
    int a;
    scanf("%d", &a);
    for (int i = 0; i < a; i++)
    {
        printf("Case #%d:\n", i + 1);
        cal(i);
    }
}
