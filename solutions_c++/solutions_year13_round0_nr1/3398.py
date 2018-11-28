#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>

using namespace std;
int N;
int T;
int tab[4][4];
const int dirs[8][2] = { {-1, 0}, {0, -1}, {1, 1}, {-1, -1}, {0, 1}, {1, 0}, {1, -1}, {-1, 1} };

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

   scanf("%d", &T);
   getchar();

   for(int i = 0; i < T; i++)
   {
       for(int j = 0; j < 4; j++)
       {
           for(int k = 0; k < 4; k++)
           {
               tab[j][k]=getchar();
           }
           getchar();
       }
       if(i!=T-1)
        getchar();

       char win=-1;
       for(int j = 0; j < 4; j++)
       {
           for(int k = 0; k < 4; k++)
           {
               if(tab[j][k]=='.')win=max(win, (char)0);
               if(tab[j][k]=='X' || tab[j][k]=='O')
               {
                   for(int d = 0; d < 8; d++)
                   {
                       bool same = true;
                       for(int co=1; co< 4; co++)
                       {
                           int px = k+dirs[d][0]*co;
                           int py = j+dirs[d][1]*co;

                           if(px < 0 || px >= 4 || py < 0 || py >= 4 || (tab[py][px] != tab[j][k] && tab[py][px]!='T'))
                           {
                               same=false;
                               break;
                           }
                       }
                       if(same)
                        {
                            win=tab[j][k];
                        }
                   }
               }
           }
       }

       printf("Case #%d: ", i+1);

       if(win==-1)
        printf("Draw\n");
       else if(win==0)
        printf("Game has not completed\n");
    else printf("%c won\n", win);
   }

    return 0;
}
