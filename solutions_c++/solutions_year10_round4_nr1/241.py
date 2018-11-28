#include <iostream>
using namespace std;
const int maxn=200;
int t,cc,f[maxn][maxn],a[maxn][maxn],ans,n,i,j,k;
int px[maxn*maxn],py[maxn*maxn],l,r;
int max(int i,int j)
{
    if (i<j) return j;
        else return i;
}
void add(int i,int j,int k)
{
     r++;
     px[r]=i;
     py[r]=j;
     f[i][j]=k;
}
int check(int x,int y)
{
     int dx,dy,i,j,k;
     for (i=0;i<maxn;i++)
            memset(f[i],0,sizeof(f[i]));
     dx=2*n-x;
     dy=2*n-y;
     x+=dx;
     y+=dy;
     l=0;r=0;
     for (i=1;i<n*2;i++)
         for (j=1;j<n*2;j++)
             if (a[i][j]) add(i+dx,j+dy,a[i][j]);
     while (l<r)
     {
           l++;
           dx=px[l];
           dy=py[l];
           i=x+x-dx;
           j=dy;
           if (!f[i][j]) add(i,j,f[dx][dy]);
                    else if (f[i][j]!=f[dx][dy]) return 0;
           i=dx;
           j=y+y-dy;
           if (!f[i][j]) add(i,j,f[dx][dy]);
                    else if (f[i][j]!=f[dx][dy]) return 0;
           i=x+x-dx;
           j=y+y-dy;
           if (!f[i][j]) add(i,j,f[dx][dy]);
                    else if (f[i][j]!=f[dx][dy]) return 0;
     }
     return 1;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for (cc=1;cc<=t;cc++)
    {
        for (i=0;i<maxn;i++)
            for (j=0;j<maxn;j++)
                a[i][j]=0;
        cin>>n;
        for (i=1;i<=n;i++)
        for (j=1;j<=i;j++)
        {
            
           cin>>a[i][n-i+2*j-1];
           a[i][n-i+2*j-1]++;
        }
        for (i=n+1;i<2*n;i++)
        for (j=1;j<=2*n-i;j++)
        {
            cin>>a[i][i-n+2*j-1];
            a[i][i-n+2*j-1]++;
        }
        ans=maxn*maxn;
        for (i=1;i<2*n;i++)
            for (j=1;j<2*n;j++)
                if (check(i,j))
                {
                               k=abs(n-i)+abs(n-j)+n;
                               if (k*k<ans) ans=k*k;
                }
        printf("Case #%d: %d\n",cc,ans-n*n);
    }
}
