#include <stdio.h>
int main()
{
//    freopen("A1.in","r",stdin);
//    freopen("A1.txt","w",stdout);
    int t,i,j,k,k1,k3,r=1,flag2,sum1,sum2;
    char a[8][8],flag[20],flag1[20];
    scanf("%d",&t);
    getchar();
    while(t--)
    {
     int sum[20]={0};
     for(i=1;i<=4;i++)
     {
      //getchar();
      for(j=1;j<=4;j++)
     {
      scanf("%c",&a[i][j]);
     }
     getchar();
     }
     getchar();
     printf("Case #%d: ",r);
     k3=5;
     for(i=1;i<=4;i++)
     {
      for(j=1;j<=4;j++)
      {
       if(a[i][j]=='X'||a[i][j]=='O')
       {flag[i]=a[i][j];}
       if(a[j][i]=='X'||a[j][i]=='O')
       {
           flag[k3]=a[j][i];
       }
      }
      k3++;
     }
     k=5;
     for(i=1;i<=4;i++)
     {
     for(j=1;j<=4;j++)
     {
       if(flag[i]==a[i][j]||a[i][j]=='T') sum[i]++;
       if(flag[k]==a[j][i]||a[j][i]=='T') sum[k]++;
     }
     k++;
     }
     //printf("**%c",flag[5]);
     k1=4;
     for(i=1;i<=4;i++)
     {
      if(a[i][i]=='X'||a[i][i]=='O')
        {flag[9]=a[i][i];}
      if(a[i][k1]=='X'||a[i][k1]=='O')
        {flag[10]=a[i][k1];}
        k1--;
     }
     //printf("**%c",flag[10]);
     k1=4;
     for(i=1;i<=4;i++)
     {
      if(a[i][i]==flag[9]||a[i][i]=='T')
        sum[9]++;
        if(a[i][k1]==flag[10]||a[i][k1]=='T')
        sum[10]++;
        k1--;
     }
     k1=1;
     for(i=1;i<=10;i++)
     {
      if(sum[i]==4) {flag1[k1]=flag[i];k1++;}
     }
     if(k1==1)
     {
         flag2=0;
         for(i=1;i<=4;i++)
         {
             for(j=1;j<=4;j++)
             {
                 if(a[i][j]=='.') {flag2=1;break;}
             }
             if(flag2==1) break;
         }
         if(flag2==1)
         printf("Game has not completed\n");
         else
         printf("Draw\n");
     }
     else
     {
         sum1=0;sum2=0;
         for(i=1;i<k1;i++)
         {
          if(flag1[i]=='X') {sum1++;}
          else
            {sum2++;}
         }
         if(sum1>sum2) printf("X won\n");
         else if(sum1<sum2) printf("O won\n");
         else printf("Draw\n");
     }
     r++;
    }
    return 0;
}
