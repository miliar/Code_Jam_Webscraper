#include<stdio.h>

int mat[52][52],mata[52][52][6];
int stack[52][52];
int top[52];
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);

   int n,k,i,j,t,count,rt,bt;
   int a,b,c,d,cas,p;
   p=0;
   char ch;

   scanf("%d",&cas);

   while(cas--)
   {

    scanf("%d%d\n",&n,&k);
    k--;
    rt=bt=0;

    count=0;
    t=-1;
    count=0;

    for(i=0;i<n;i++)
     { for(j=0;j<n;j++)
       {
           scanf("%c",&ch);
           if(ch!='.' && t!=i)
           {
               t=i;
               count++;
               }

           if(ch=='R')
            stack[count][++top[count]]=1;
           else if(ch=='B')
            stack[count][++top[count]]=2;
        }
        scanf("%c",&ch);
     }

    for(i=1;i<=count;i++)
     {
         t=0;
         for(j=top[i];j>=0;j--)
       {
         mat[i][++t]=stack[i][j];

       }
     }



    a=b=c=d=0;

    for(i=1;i<=count;i++)
     for(j=1;j<=top[i];j++)
     {

         if (mat[i-1][j-1]==mat[i][j])
            mata[i][j][1]=mata[i-1][j-1][1]+1;


          if (mat[i-1][j+1]==mat[i][j])
            mata[i][j][2]=mata[i-1][j+1][2]+1;


          if (mat[i-1][j]==mat[i][j])
            mata[i][j][3]=mata[i-1][j][3]+1;


          if (mat[i][j-1]==mat[i][j])
            mata[i][j][4]=mata[i][j-1][4]+1;

         a=mata[i][j][1];
         b=mata[i][j][2];
         c=mata[i][j][3];
         d=mata[i][j][4];

         if(a==k || b==k || c==k || d==k)
         {
             if(mat[i][j]==1)
              rt=1;
             else
              bt=1;
        }



         }
        printf("Case #%d: ",++p);

        if(rt==1 && bt==1)
         printf("Both");
        else if(rt==1)
         printf("Red");
        else if(bt==1)
         printf("Blue");
        else
         printf("Neither");

    printf("\n");

    for(i=1;i<=count;i++)
     {for(j=1;j<=top[i];j++)
     {
         mat[i][j]=0;
         mata[i][j][1]=0;
         mata[i][j][2]=0;
         mata[i][j][3]=0;
         mata[i][j][4]=0;
         }
        top[i]=0;
     }
   }
    return 0;
    }
