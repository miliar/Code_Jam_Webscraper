#include <stdio.h>
#include <stdlib.h>
int t,n,k;
char A[100][100];
char B[100][100];
char C[500][500];
int lastest[100];
int cntrow,cntcol;
int reds,blues;
void wins(char a)
{
 if(a=='R'){reds=1;}
 else{blues=1;}
}
void chk()
{
char pos;
 for(int i=100;i<100+n;i++)
 {
  for(int j=100;j<100+n;j++)
  {
   if(C[i][j]!='.')
   {
    pos=C[i][j];
    for(int l=1;l<k;l++)
    {
     if(C[i-l][j-l]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i-l][j]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i][j-l]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i+l][j+l]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i][j+l]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i+l][j]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i-l][j+l]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
        for(int l=1;l<k;l++)
    {
     if(C[i+l][j-l]!=pos){break;}
     else if(l==k-1){wins(pos);}
    }
   }
  }
 }
}
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d%d",&n,&k);
 // printf("%d %d\n",n,k);
  for(int j=0;j<n;j++)
  {
   scanf("%s",A[j]);
  }
 cntrow=-1;
 cntcol=-1;
  printf("Case #%d: ",i);
   /* printf("\n");
   for(int j=0;j<n;j++)
   {
    for(int l=0;l<n;l++)
    {
     printf("%c",A[j][l]);
    }
    printf("\n");
   }*/
 for(int l=0;l<=n-1;l++)
 {
  cntrow++;
  cntcol=-1;
  for(int j=n-1;j>=0;j--)
  {
   cntcol++;
   B[cntrow][cntcol]=A[j][l];
  }
 }
/* printf("\n");
   for(int j=0;j<n;j++)
   {
    for(int l=0;l<n;l++)
    {
     printf("%c",B[j][l]);
    }
    printf("\n");
   }*/
 for(int j=0;j<=n-1;j++)
 {
 lastest[j]=n-1;
 }
 for(int j=n-1;j>=0;j--)
 {
  for(int l=0;l<=n-1;l++)
  {
   if(B[j][l]!='.')
   {
    if(lastest[l]!=j)
    {
    B[lastest[l]][l]=B[j][l];
    B[j][l]='.';
    }
    lastest[l]--;
   }
  }
 }
    
  /* printf("\n");
   for(int j=0;j<n;j++)
   {
    for(int l=0;l<n;l++)
    {
     printf("%c",B[j][l]);
    }
    printf("\n");
   }*/
 for(int j=0;j<=100;j++)
 {
  for(int l=0;l<=100;l++)
  {
   C[j+100][l+100]='.';
  }
 }
 for(int j=0;j<=n-1;j++)
 {
  for(int l=0;l<=n-1;l++)
  {
   C[j+100][l+100]=B[j][l];
  }
 }
  reds=0;
  blues=0;
  chk();


  if(reds==1&&blues==1){printf("Both\n");}
  else if(reds==0&&blues==0){printf("Neither\n");}
  else if(reds==1){printf("Red\n");}
  else{printf("Blue\n");}
 }
 return 0;
}
