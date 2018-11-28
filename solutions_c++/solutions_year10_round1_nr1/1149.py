# include <stdio.h>
# include <string.h>
# include <math.h>
# include <ctype.h>
# include <algorithm>

using namespace std;

int need,ma;
char a[100][100],c;

int trav(int x,int y)
{
    int i,j,k,l,r,s;

    // printf("*%c\n",a[x][y]);

    // down
    l = 0;
    for(i = x;i<=ma;i++)
    {
      if(a[x][y] != a[i][y])break;
      if(a[x][y] == a[i][y])++l;
      if(l == need)return 1;

    }

    // row;
    l = 0;
    for(i = y;i<=ma;i++)
    {
        if(a[x][y] != a[x][i])break;
        if(a[x][y] == a[x][i])++l;
        if(l == need)return 1;

    }

    //left dig
    l = 0;
    s = y;
    for(i=x;i<=ma;i++)
    {
       if(a[x][y] != a[i][s])break;
       if(a[x][y] == a[i][s])++l;
       --s;
       if(l == need)return 1;
       if(s < 0)break;

    }

    //right dig
    l = 0;
    s = y;
    for(i=x;i<=ma;i++)
    {
        if(a[x][y] != a[i][s])break;
        if(a[x][y] == a[i][s])++l;
        ++s;
        if(l == need)return 1;
        if(s > ma)break;


    }
   return 0;
}


int main()
{

   int test,i,j,k,l,co,m,n,r,s,red,blue;
   freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);

   scanf("%d",&test);


   for(k=1;k<=test;k++)
   {

        scanf("%d%d",&ma,&need);
        l = ma;

        for(i = 1;i <= ma;i++)
        {
         for(j = 1;j <= ma;j++)
          {
              scanf(" %c",&a[j][l]);

          }
          --l;
          scanf("%c",&c);
        }

      /*  for(i=1;i<=ma;i++)
        {
         for(j=1;j<=ma;j++)
          {
              printf("%c",a[i][j]);
          }
          printf("\n");
        }


       printf("*\n");*/

        for(i = ma-1;i>=1;i--)
        {
         for(j = 1;j<=ma;j++)
          {

              if(a[i][j] != '.')
              {
                 // printf(" %c",a[i][j]);
                  r = 0;
                  for(m=i+1;m<=ma;m++)
                  {
                    if(a[m][j] != '.')break;
                    r = m;
                  }
                 // printf("%d %dhere",r,j);
                  if(r != i && r != 0)
                  {
                     // flag[i][j] = 0;
                     // flag[m][j] = 1;
                     // printf("there");
                      a[r][j] = a[i][j];
                      a[i][j] = '.';
                  }
              }
          }
        }

      /*  for(i=1;i<=ma;i++)
        {
         for(j=1;j<=ma;j++)
          {
              printf("%c",a[i][j]);
          }
          printf("\n");
        }*/


        red = blue = 0;
        for(i=1;i<=ma;i++)
        {
         for(j=1;j<=ma;j++)
          {
             // printf("%c",a[i][j]);
              if(a[i][j] != '.')
              {
                 // printf("%c",a[i][j]);
                  s = trav(i,j);
                 // printf("s:%d ",s);
                  if(a[i][j] == 'R' && s == 1)++red;
                  if(a[i][j] == 'B' && s == 1)++blue;
              }
          }
          //printf("\n");
        }

       // printf("%d %d\n",red,blue);

        if(red == 0 && blue != 0)printf("Case #%d: Blue\n",k);
        else if(red != 0 && blue == 0)printf("Case #%d: Red\n",k);
        else if(red != 0 && blue != 0)printf("Case #%d: Both\n",k);
        else printf("Case #%d: Neither\n",k);



   }
   return 0;
}
