#include<stdio.h>

int map[102][102], tmp[102][102];
int min_x, max_x, min_y, max_y;
bool imitate()
{
    bool ans = false;
    
    int i, j;
    for(i = min_x; i <= max_x; i ++)
        for(j = min_y; j <= max_y; j ++)
        {
            if(map[i][j] == 1)
            {
                ans = true;
                if(map[i - 1][j] == 0 && map[i][j - 1] == 0)
                    tmp[i][j] = 0;
                else
                    tmp[i][j] = 1;
            }
            else
            {
                if(map[i - 1][j] == 1 && map[i][j - 1] == 1)
                    tmp[i][j] = 1;
                else
                    tmp[i][j] = 0;
            }
        }
    
    
    return ans;
}


void mcopy()
{
    
    int i, j;
    for(i = min_x; i <= max_x; i ++)
        for(j = min_y; j <= max_y; j ++)
            map[i][j] = tmp[i][j];
}

void print()
{
    int i, j;
    for(i = min_x; i <= max_x; i ++, printf("\n"))
        for(j = min_y; j <= max_y; j ++)
            printf("%d", map[i][j]);    
    printf("\n");
}
int main()
{
    int T, test, R, ans;
    
    int i, j, x1, x2, y1, y2;
    bool flag;
    scanf("%d", &T);
    for(test = 1; test <= T; test ++)
    {
        scanf("%d", &R);
        for(i = 1; i <= 100; i ++)
            for(j = 1; j <= 100; j ++)
                map[i][j] = 0;
        min_x = min_y = 100;
        max_x = max_y = 1;
        while(R --)
        {
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            if(min_x > x1)
                min_x = x1;
            if(min_y > y1)
                min_y = y1;
            if(max_x < x2)
                max_x = x2;
            if(max_y < y2)
                max_y = y2;                
            for(i = x1; i <= x2; i ++)
                for(j = y1; j <= y2; j ++)
                    map[i][j] = 1;
        }
//        printf("minx = %d  miny = %d maxx = %d  maxy = %d\n", min_x, min_y, max_x, max_y);
        flag = true;
            
        ans = 0;
        while(true)
        {
            flag = imitate();
            mcopy();
            if(!flag)
                break;
            ans ++;
        }
        printf("Case #%d: %d\n", test, ans);
    }
    
    return 0;
}
