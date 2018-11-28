#include <cstdio>
using namespace std;


int K; 

int ds[512][512];

int get(int size, int x, int y, int i, int j)
{
    if(i < x || i >= x + K)
        return -1;

    if(j < y || j >= y + K)
        return -1;

    return ds[i - x][j - y];
}

bool check(int size, int x, int y)
{
    for(int i = 0; i < size; i++)
        for(int j = 0; j < size; j++)
        {
            int a = get(size, x, y, i, j);
            int b = get(size, x, y, size - 1 - j, size - 1 - i);
            int c = get(size, x, y, j, i);
            
            if(a != -1 && b != -1 && a != b)
                return false;
            if(a != -1 && c != -1 && a != c)
                return false;            
        }

    return true;
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);
        scanf("%d", &K);

        for(int i = 0; i < 2 * K - 1; i++)
        {
            int x, y;

            if(i < K)
                x = i, y = 0;
            else
                x = K - 1, y = i - K + 1;

            while(x >= 0 && y < K)
            {
                scanf("%d", &ds[x][y]);
                x--;
                y++;
            }
        }
/*
        printf("\n");
        for(int i = 0; i < K; i++, printf("\n"))
            for(int j =0 ; j < K; j++)
                printf("%d ", ds[i][j]);
  */      
        int ans = -1;
        for(int s = K; ans == -1; s++)
        {
            for(int i = 0; ans == -1 && i <= s - K; i++)
                for(int j = 0; ans == -1 && j <= s - K; j++)
                    if(check(s, i, j))
                    {
                        ans = s;
                        break;
                    }
        }

        printf("%d\n", ans * ans - K * K);
    }
    return 0;
}
