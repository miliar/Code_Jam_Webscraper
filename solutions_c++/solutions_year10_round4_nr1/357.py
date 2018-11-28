#include<iostream>
using namespace std;
int n,Ans;
int num[110][110];
int FIRST[110];
int cnt=0;
int ABS(int x)
{
    if (x<0) return -x; else return x;
}    
bool Check(int x,int y,int dx,int dy,int number,int kind)
{
     if (kind==0) x=-x; else y=-y;
     x-=dx;
     y-=dy;
     int row=n-1-y;
     int col=(x-FIRST[row])/2;
     if (row>=0 && row<=2*n-2)
     {
         if (col<0) return true;
        if (row<n && col>row) return true;
        if (row>=n && col>=n-1-(row-n)) return true;
        if (num[row][col]!=number) return false;
     }
     return true;     
}
void Solve()
{
     scanf("%d",&n);
     for (int i=0;i<n;++i)
     {
         for (int j=0;j<=i;++j)
         scanf("%d",&num[i][j]);
         FIRST[i]=-i;
     }
     for (int i=0;i<n-1;++i)
     {
         for (int j=0;j<n-i-1;++j)
         scanf("%d",&num[i+n][j]);     
         FIRST[i+n]=-(n-1)+i+1;
     }
     
     Ans=1000000000;
     for (int dx=-n;dx<=n;++dx)
     for (int dy=-n;dy<=n;++dy)
     {
         bool OK=true;
         int Length=0;
         for (int i=0;i<n;++i)
             for (int j=0;j<=i;++j)
             {
                 int x=FIRST[i]+j*2;
                 int y=n-1-i;
                 Length=max(Length,ABS(x+dx)+ABS(y+dy)+1);
                 if (!Check(x+dx,y+dy,dx,dy,num[i][j],0)) OK=false;
                 if (!Check(x+dx,y+dy,dx,dy,num[i][j],1)) OK=false;
            }
         for (int i=0;i<n-1;++i)
             for (int j=0;j<n-i-1;++j)
             {
                 int x=FIRST[i+n]+j*2;
                 int y=-i-1;
                 Length=max(Length,ABS(x+dx)+ABS(y+dy)+1);
                 if (!Check(x+dx,y+dy,dx,dy,num[i+n][j],0)) OK=false;
                 if (!Check(x+dx,y+dy,dx,dy,num[i+n][j],1)) OK=false;
             }
         if (OK)
         {
         Ans=min(Ans,Length*Length-n*n);
         }
     }
     
     printf("Case #%d: %d\n",++cnt,Ans);
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("Answer_A_Large.txt","w",stdout);
    int Tcase;
    scanf("%d",&Tcase);
    while (Tcase--)   Solve();
    return 0;
}
