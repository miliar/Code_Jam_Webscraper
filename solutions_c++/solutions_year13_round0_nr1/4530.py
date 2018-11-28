#include <iostream>
#include <cstdio>
using namespace std;

char check();
void read();

char a[5][5], c;
int T, x, y;
bool completed;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin>>T;
    for(int t = 1; t <= T; t++)
    {
        read();
        a[x][y] = 'X';
        c = check();
        if (c != 0)
        {
            printf("Case #%d: %c won", t, c);
            //if (t < T)
                printf("\n");
            continue;
        }
        a[x][y] = 'O';
        c = check();
        if (c != 0)
        {
            printf("Case #%d: %c won", t, c);
            //if (t < T)
                printf("\n");
            continue;
        }

        if (completed)
            printf("Case #%d: Draw", t);
        else
            printf("Case #%d: Game has not completed", t);
        //if (t < T)
            printf("\n");
    }


    return 0;
}

char check()
{
    bool flag = false;
    for(int i = 0; i < 4; i++)
    {
        if (a[i][0] != '.')
        {
            flag = true;
            for(int j = 1; j < 4; j++)
                if (a[i][j] != a[i][0])
                    flag = false;
            if (flag)
                return a[i][0];
        }

        if (a[0][i] != '.')
        {
            flag = true;
            for(int j = 1; j < 4; j++)
                if (a[j][i] != a[0][i])
                    flag = false;
            if (flag)
                return a[0][i];
        }
    }

    if (a[0][0] != '.')
    {
        flag = true;
        for(int i = 1; i < 4; i++)
            if (a[i][i] != a[0][0])
                flag = false;
        if (flag)
            return a[0][0];
    }


    if (a[0][3] != '.')
    {
        flag = true;
        for(int i = 1; i < 4; i++)
            if (a[i][3-i] != a[0][3])
                flag = false;
        if (flag)
            return a[3][0];

    }

    return 0;
}

void read()
{
    x = y = 4;
    completed = true;
    for(int i = 0; i < 4; i++)
    {
        scanf("%s\n", a[i]);
        for(int j = 0; j < 4; j++)
            if (a[i][j] == 'T')
            {
                x = i;
                y = j;
            }
            else if (a[i][j] == '.')
                completed = false;
    }
    scanf("\n");
}
