#include <cstdio>
#include <cstring>
using namespace std;

char Map[6][6];

void work()
{
     bool finish = 1;
     for (int i = 0;i < 4;++i)
     {
         scanf(" %s",Map[i]);
         for (int j = 0;j < 4;++j)
             if (Map[i][j] == '.')
                finish = 0;
     }
     int ans = 0;
     for (int i = 0;i < 4;++i)
     {
         int o = 0;
         int x = 0;
         int t = 0;
         for (int j = 0;j < 4;++j)
         {
             o += Map[i][j] == 'O';
             x += Map[i][j] == 'X';
             t += Map[i][j] == 'T';
         }
         if (o == 4 || o == 3 && t == 1) ans = 1;
         if (x == 4 || x == 3 && t == 1) ans = -1;
     }
     for (int j = 0;j < 4;++j)
     {
         int o = 0;
         int x = 0;
         int t = 0;
         for (int i = 0;i < 4;++i)
         {
             o += Map[i][j] == 'O';
             x += Map[i][j] == 'X';
             t += Map[i][j] == 'T';
         }
         if (o == 4 || o == 3 && t == 1) ans = 1;
         if (x == 4 || x == 3 && t == 1) ans = -1;
     }
     int o = 0;
     int x = 0;
     int t = 0;
     for (int i = 0;i < 4;++i)
     {
         o += Map[i][i] == 'O';
         x += Map[i][i] == 'X';
         t += Map[i][i] == 'T';
     } 
     if (o == 4 || o == 3 && t == 1) ans = 1;
     if (x == 4 || x == 3 && t == 1) ans = -1;    
     
     o = 0;
     x = 0;
     t = 0;
     for (int i = 0;i < 4;++i)
     {
         o += Map[i][3-i] == 'O';
         x += Map[i][3-i] == 'X';
         t += Map[i][3-i] == 'T';
     } 
     if (o == 4 || o == 3 && t == 1) ans = 1;
     if (x == 4 || x == 3 && t == 1) ans = -1;         
     if (!ans)
     {
              if (finish) puts("Draw");
              else puts("Game has not completed");
     }
     if (ans == 1) puts("O won");
     if (ans == -1) puts("X won");
}
         
         

int main()
{
    int times;
    scanf("%d",&times);
    for (int i = 1;i <= times;++i)
    {
        printf("Case #%d: ",i);
        work();
    }      
    return 0;
}
