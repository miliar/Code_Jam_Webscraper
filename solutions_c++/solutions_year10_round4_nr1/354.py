#include <stdio.h>
#include <stdlib.h>
int t;
int si;
int atx,aty;
int r1,r2;
int t1,t2;
int ra;
int op;
int am;
int tab[1000][1000];
int A[5000][5000];
int B[5000][5000];
bool chk(int a)
{
int cnt1=0;
int cnt2=0;
// printf("start\n");
       for(int p=1;p<=a;p++)
     {
      for(int q=1;q<=a;q++)
      {
        if(A[p][q]!=(-1))
        {
         if(A[p][q]!=A[q][p])
         {
          if(A[q][p]==(-1)){A[q][p]=A[p][q];}
          else{return false;}
         }
        }
        else
        {
         if(A[q][p]!=(-1)){A[p][q]=A[q][p];}
        }
      }
     }
      /*   for(int p=1;p<=a;p++)
      {
       for(int q=1;q<=a;q++)
       {
        printf("%d ",A[p][q]);
       }
       printf("\n");
      }
      printf("------\n");
            system("pause");*/
     for(int j=1;j<=a;j++)
     {
     cnt1++;
     cnt2=0;
      for(int i=a;i>=1;i--)
      {
       cnt2++;
       B[cnt1][cnt2]=A[i][j];
      }
     }
            for(int p=1;p<=a;p++)
     {
      for(int q=1;q<=a;q++)
      {
        if(B[p][q]!=(-1))
        {
         if(B[p][q]!=B[q][p])
         {
          if(B[q][p]==(-1)){B[q][p]=B[p][q];}
          else{return false;}
         }
        }
        else
        {
         if(B[q][p]!=(-1)){B[p][q]=B[q][p];}
        }
      }
     }
         /*for(int p=1;p<=a;p++)
      {
       for(int q=1;q<=a;q++)
       {
        printf("%d ",B[p][q]);
       }
       printf("\n");
      }
      printf("end func------\n");
            system("pause");*/
     return true;
}
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {

  scanf("%d",&si);
   for(int j=1;j<=si;j++)
   {
    atx=1;
    aty=j;
    for(int k=1;k<=j;k++)
    {
     scanf("%d",&tab[aty][atx]);
     aty--;
     atx++;
    }
   }
   for(int j=si-1;j>=1;j--)
   {
    aty=si;
    atx=1+(si-j);
    for(int k=1;k<=j;k++)
    {
     scanf("%d",&tab[aty][atx]);
     aty--;
     atx++;
    }
   }
   /*printf("\n");
   for(int i=1;i<=si;i++) 
   {
    for(int j=1;j<=si;j++)
    {
     printf("%d ",tab[i][j]);
    }
    printf("\n");
   }*/
   op=0;
   for(int j=si;op==0;j++)
   {
   op=0;
  // printf("j=%d\n",j);
    for(int k=1;k<=j-si+1;k++)
    {
     for(int l=1;l<=j-si+1;l++)
     {
    //  printf("%d %d\n",k,l);
     for(int p=1;p<=j;p++)
     {
      for(int q=1;q<=j;q++)
      {
       A[p][q]=(-1);
      }
     }
      for(int p=1;p<=si;p++)
      {
       for(int q=1;q<=si;q++)
       {
        A[p+k-1][q+l-1]=tab[p][q]; 
       }
      } 
     /* for(int p=1;p<=j;p++)
      {
       for(int q=1;q<=j;q++)
       {
        printf("%d ",A[p][q]);
       }
       printf("\n");
      }
      printf("------\n");
      system("pause");*/
      if(chk(j)==true){printf("Case #%d: ",i);printf("%d\n",(j*j)-(si*si));op=1;k=9999;l=9999;}
     }
    }
   }
 }
// system("pause");
 return 0;
}
/*
4
1
0
2
 1
2 2
 1
2
 1
1 2
 1
3
  1
 6 3
9 5 5
 6 3
  1
*/
