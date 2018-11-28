#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
const int Max=15;
char Map[Max][Max];
int x[Max],y[Max];
 int n,m;
using namespace std;
int main()
{
    freopen("D:\\input.txt","r",stdin);
    freopen("D:\\output.txt","w",stdout);
     int t,i,j;
     scanf("%d",&t);
     int x,o,p,s,x1,o1,ncase=1;
     while(t--)
     {
       x=0;o=0;p=0;
       for(i=0;i<4;i++)
       {
           scanf("%s",Map[i]);
       }

       for(i=0;i<4;i++)
       {
           x1=0;o1=0;s=0;
        for(j=0;j<4;j++)
         {
           if(Map[i][j]=='X') x1++;
           if(Map[i][j]=='O') o1++;
           if(Map[i][j]=='T') s++;
           if(Map[i][j]=='.') p=1;
         }
         if((x1+s)==4)
            x=1;
         if((o1+s)==4)
            o=1;
       }
       for(i=0;i<4;i++)
       {
           x1=0;o1=0;s=0;
        for(j=0;j<4;j++)
         {
           if(Map[j][i]=='X') x1++;
           if(Map[j][i]=='O') o1++;
           if(Map[j][i]=='T') s++;
         }
        if((x1+s)==4)
            x=1;
         if((o1+s)==4)
            o=1;
       }
       x1=0;o1=0;s=0;
       for(i=0;i<4;i++)
       {
           if(Map[i][i]=='X') x1++;
           if(Map[i][i]=='O') o1++;
           if(Map[i][i]=='T') s++;
       }
      if((x1+s)==4)
            x=1;
         if((o1+s)==4)
            o=1;
     x1=0;o1=0;s=0;
       for(i=0;i<4;i++)
       {
           if(Map[i][3-i]=='X') x1++;
           if(Map[i][3-i]=='O') o1++;
           if(Map[i][3-i]=='T') s++;
       }
      if((x1+s)==4)
            x=1;
         if((o1+s)==4)
            o=1;
       if(x==1)
       {
           printf("Case #%d: X won\n",ncase++);continue;
       }
       if(o==1)
       {
           printf("Case #%d: O won\n",ncase++);continue;
       }
       if(p==1)
       {
           printf("Case #%d: Game has not completed\n",ncase++);continue;
       }
       else
       {
           printf("Case #%d: Draw\n",ncase++);continue;
       }
     }
}
