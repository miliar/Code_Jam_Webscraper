#include <stdio.h>
const int ia[4]={-1,0,0,1};
const int ja[4]={0,-1,1,0};
int ii,t,n,i,j,m;
int a[200][200];
char mas[200][200];
char aso,k;
char chayola(int i,int j)
{
int mni,ik,i1,k;
if(mas[i][j])
   return mas[i][j];
mni=a[i-1][j];ik=0;
for(i1=1;i1<4;i1++)
   if(a[i+ia[i1]][j+ja[i1]]<mni)
      {
      mni=a[i+ia[i1]][j+ja[i1]];
      ik=i1;
      }
if(mni>=a[i][j]){mas[i][j]=aso;return 0;}
k=chayola(i+ia[ik],j+ja[ik]);
if(k) mas[i][j]=k;
else mas[i][j]=aso;
return k;
}
int main()
{
freopen("B-large.in","r",stdin);
freopen("B-large.out","w",stdout);
scanf("%d",&t);
for(ii=1;ii<=t;ii++)
   {
   printf("Case #%d:\n",ii);
   scanf("%d %d",&n,&m);
   for(i=0;i<=n+1;i++)
      for(j=0;j<=m+1;j++)
         a[i][j]=1000000000,
         mas[i][j]=0;
   for(i=1;i<=n;i++)
      for(j=1;j<=m;j++)
         scanf("%d",&a[i][j]);
   aso='a';
   for(i=1;i<=n;i++)
      for(j=1;j<=m;j++)
         if(!mas[i][j])
            {
            if(k=chayola(i,j))
               mas[i][j]=k;
            else
               mas[i][j]=aso++;
            }
   for(i=1;i<=n;i++)
      {
      printf("%c",mas[i][1]);
      for(j=2;j<=m;j++)
         printf(" %c",mas[i][j]);
      printf("\n");
      }
   }
return 0;
}
