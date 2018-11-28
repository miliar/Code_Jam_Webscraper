#include <stdio.h>

int r;
int map[100][100];
int result;
int x1, y1, x2, y2;

void Init()
{
    result = 0;
}

void SetMap()
{
    for(int i = x1; i <= x2; i++)
    {
        for(int j = y1; j <= y2; j++)
        {
            map[j][i] = 1;
        }
    }
}

void Input()
{
    
    scanf("%d", &r);
    for(int i = 0; i < r; i++)
    {
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        x1--;
        y1--;
        x2--;
        y2--;
        SetMap();
    }
}

void Process()
{
    for(;;)
    {
        bool isEnd = true;
        for(int i = 0; i < 100 && isEnd; i++)
        {
            for(int j = 0; j < 100 && isEnd; j++)
            {
                if(map[i][j] == 1)
                {
                    isEnd = false;
                }
            }
        }
        if(isEnd) return;
        result++;
        for(int i = 99; i >= 0; i--)
        {
            for(int j = 99; j >= 0; j--)
            {
                if(map[j][i] == 1)
                {
                    if((i&&map[j][i-1])||(j&&map[j-1][i])) map[j][i] = 1;
                    else                                   map[j][i] = 0;
                }
                else
                {
                    if(i&&map[j][i-1]&&j&&map[j-1][i]) map[j][i] = 1;
                }
            }
        }
    }
}

int main()
{
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
        Init();
        Input();
        Process();
        printf("Case #%d: %d\n", i, result);
    }
}