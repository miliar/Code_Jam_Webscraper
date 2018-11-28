#include <cstdio>

int R, C;
bool map[50][50];
char ans[50][50];

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        scanf("%d %d ", &R, &C);
        
        for(int i = 0; i < R; ++i)
        {
            for(int j = 0; j < C; ++j)
            {
                char a;
                scanf("%c", &a);
                
                ans[i][j] = a;
                if(a == '.')
                    map[i][j] = false;
                else
                    map[i][j] = true;
                
            }
            scanf(" ");
        }
        
        for(int i = 0; i < R - 1; ++i)
        {
            for(int j = 0; j < C - 1; ++j)
            {
//                 printf("%d", map[i][j]);
                if(map[i][j] && map[i+1][j] && map[i][j+1] && map[i+1][j+1])
                {
                    map[i][j] = map[i+1][j] = map[i][j+1] = map[i+1][j+1] = false;
                    ans[i][j] = '/';
                    ans[i+1][j] = '\\';
                    ans[i][j+1] = '\\';
                    ans[i+1][j+1] = '/';
                }
            }
//             printf("\n");
        }
        
        bool possible = true;
        for(int i = 0; i < R; ++i)
            for(int j = 0; j < C; ++j)
                if(map[i][j])
                {
                    possible = false;
                }
         
        printf("Case #%d: \n", t);
        if(!possible)
        {
            printf("Impossible\n");
        }
        else
        {
            for(int i = 0; i < R; ++i)
            {
                for(int j = 0; j < C; ++j)
                    printf("%c", ans[i][j]);
                printf("\n");
            }
        }
    }
    return 0;
}