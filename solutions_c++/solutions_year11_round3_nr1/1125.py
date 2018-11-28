#include<cstdio>
#include<iostream>
#include<memory.h>

using namespace std;

int r,c;
char a[52][52];
int tile(int);

int main()
{
    int T;
    cin >>T;
    for (int num=1; num<=T; num++)
        tile(num);
    return 0;
}

int tile(int num)
{
    memset(a,0,sizeof(a));
    printf("Case #%d:\n",num);
    int r,c;
    cin >>r >>c;
    int i,j;
    char ch;
    ch = getchar();
    int blue = 0;
    for (i=0; i<r; i++)
    {
        for (j=0; j<c; j++)
        {
            cin >>a[i][j];
            if (a[i][j]=='#')
                blue++;
        }
        ch = getchar();
    }
    if (blue % 4 != 0)
    {
        printf("Impossible\n");
        return 0;
    }
    bool flag = true;
    int k;
    while (blue && flag)
    {
        k=0;
        while (k<r*c)
        {
            i=k/c, j=k%c;
            if (a[i][j]=='#')
                break;
            k++;
        }
        if (k < r*c)
        {
            a[i][j] = '/';
            if (i+1==r || j+1==c)
                flag = false;
            else if (a[i+1][j]!='#' || a[i][j+1]!='#')
                flag = false;
            else if (a[i+1][j+1]!='#')
                flag = false;
            else
            {
                a[i+1][j] = '\\';
                a[i][j+1] = '\\';
                a[i+1][j+1] = '/';
            }
        }
        blue -= 4;
    }
    if (!flag)
        printf("Impossible\n");
    else
    {
        for (i=0; i<r; i++)
        {
            for (j=0; j<c; j++)
                printf("%c",a[i][j]);
            printf("\n");
        }
    }
    return 0;
}
