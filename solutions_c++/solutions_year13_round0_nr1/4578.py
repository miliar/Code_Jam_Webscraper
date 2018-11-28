#include <stdio.h>
int t;
char s[100][100];
char tmp[100];
bool won(char c)
{
int sc1 = 0, sc2 = 0;
for(int i=0;i<4;i++)
   {
   int sc = 0;
   for(int j=0;j<4;j++)
      sc += (s[i][j] == c || s[i][j] == 'T');
   if(sc == 4) return 1;
   sc = 0;
   for(int j=0;j<4;j++)
      sc += (s[j][i] == c || s[j][i] == 'T');
   if(sc == 4) return 1;
   sc1 += (s[i][i] == c || s[i][i] == 'T');
   sc2 += (s[3-i][i] == c || s[3-i][i] == 'T');
   }
if(sc1 == 4 || sc2 == 4) return 1;
return 0;
}
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d",&t);
for(int it=1;it<=t;it++)
   {
   gets(tmp);
   printf("Case #%d: ",it);
   int wc = 0;
   for(int i=0;i<4;i++)
      {
      gets(s[i]);
      for(int j=0;j<4;j++)
         if(s[i][j] == '.')
            wc++;
      }
   if(won('X'))
      printf("X won\n");
   else
      if(won('O'))
         printf("O won\n");
      else
         if(wc)
            printf("Game has not completed\n");
         else
            printf("Draw\n");
   }
return 0;
}
