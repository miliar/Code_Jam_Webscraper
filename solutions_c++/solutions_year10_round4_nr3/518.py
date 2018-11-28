#include <stdio.h>
int it,t,n,x,y,rd,i,svla,x1,y1,x2,y2;
int mas[1000][1000];
int main()
{
freopen("C-small-attempt1.in","r",stdin);
freopen("C-small.out","w",stdout);
scanf("%d",&t);
for(it=1;it<=t;it++)
   {
   scanf("%d",&n);
   for(x=0;x<=100;x++)
      for(y=0;y<=100;y++)
         mas[y][x]=0;
   for(rd=i=0;i<n;i++)
      {
      scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
      for(x=x1;x<=x2;x++)
         for(y=y1;y<=y2;y++)
            if(!mas[y][x])
               {
               rd++;
               mas[y][x]=1;
               }
      }
   svla=0;
   while(rd)
      {
      svla++;
      for(x=100;x;x--)
         for(y=100;y;y--)
            {
            if(mas[y][x-1]&&mas[y-1][x])
               {
               if(!mas[y][x])
                  {
                  mas[y][x]=1;
                  rd++;
                  }
               }
            if(! (mas[y][x-1]||mas[y-1][x]) )
               if(mas[y][x])
                  {
                  rd--;
                  mas[y][x]=0;
                  }
            }
      }
   printf("Case #%d: %d\n",it,svla);
   }
return 0;
}
