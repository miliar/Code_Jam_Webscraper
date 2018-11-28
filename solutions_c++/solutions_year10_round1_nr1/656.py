#include <iostream>
char b[1000][1000],a[1000][1000];
int g[8]={0,0,1,1,1,-1,-1,-1};
int h[8]={-1,1,-1,0,1,-1,0,1};
int n,m,x,y;
void down()
{
     int i,k,j;
     char ch;
     for (i=0;i<n;i++)
     {
         k=n-1;
         for (j=n-1;j>=0;j--)
         if (a[j][i]!='.')
         {
            ch=a[j][i];a[j][i]='.';
            a[k][i]=ch;
            k--;
         }                    
     }                      
}
void rotat(int x,int y)
{
     b[y][n-1-x]=a[x][y];               
}
int check(int x,int y,int z,char ch,int p)
{
     if (p==0)return 1;
     if (x>=n||y>=n||y<0||x<0)return 0;
     if (a[x][y]!=ch)return 0;
     return check(x+g[z],y+h[z],z,ch,p-1);
}
void prt()
{
     int i,j;
     for (i=0;i<n;i++)
     {
     for (j=0;j<n;j++)
     {
         printf("%c",a[i][j]);
     }
     puts("");
     }
     puts("");
 }
void init()
{
     
     char st[10];
     int i,k,j;
     scanf("%d%d",&n,&m);
     gets(st);
     for (i=0;i<n;i++)
     gets(a[i]);     
     

     
     
     down();     
     for (i=0;i<n;i++)
     for (j=0;j<n;j++)
     rotat(i,j);
     for (i=0;i<n;i++)
     for (j=0;j<n;j++)
     a[i][j]=b[i][j];
     
  
     
     down();
     x=y=0;
     for (i=0;i<n;i++)
     for (j=0;j<n;j++)
     {
         for (k=0;k<8;k++)
         {
         if (check(i,j,k,'R',m))x=1;
         if (check(i,j,k,'B',m))y=1;}
     }
     
   
}
int main()
{
  //  freopen("i.txt","r",stdin);
  //  freopen("o.txt","w",stdout);
    int i,k,j,cas;
    scanf("%d",&cas);
    for (i=1;i<=cas;i++)
    {
        init();
        printf("Case #%d: ",i);
        if (x!=0&&y!=0)puts("Both");
        if (x!=0&&y==0)puts("Red");
        if (x==0&&y!=0)puts("Blue");
        if (x==0&&y==0)puts("Neither");
    }

}
