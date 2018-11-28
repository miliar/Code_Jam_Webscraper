#include<iostream>
#include<sstream>
using namespace std;
int t,n;
char tmp[100000];
int X[10100];
struct ttt
{
       int a,b;
} rank[10100];
int Solve()
{
     int rn=0;
     for (int i=0;i<10100;++i)
     if (X[i]>0)
     {
                rank[rn].a=i;
                rank[rn].b=X[i];
                rn++;
     }
     int ans=100000;
     while (true)    
     {
         int l=0,r;
         while (rank[l].b==0 && l<rn) ++l;
         r=l;
         if (l==rn) break;
         while (r<rn-1 && rank[r].a+1==rank[r+1].a && rank[r].b<=rank[r+1].b) ++r;
         ans=min(r-l+1,ans);
         for (int i=l;i<=r;++i) rank[i].b--;
     }
     return ans;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);
    scanf("%d\n",&t);
    for (int i=1;i<=t;++i)
    {
        int n;
        scanf("%d",&n);
        memset(X,0,sizeof(X));
        for (int j=0;j<n;++j) 
        {
            int x;
            scanf("%d",&x);
            X[x]++;
        }
        if ( n==0 )   printf("Case #%d: 0\n",i); else
        printf("Case #%d: %d\n",i,Solve());
    }
    return 0;
}
