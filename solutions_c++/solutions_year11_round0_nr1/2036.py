#include<iostream>
#include<cmath>
using namespace std;
int ans;
int T;
int Solve()
{
     int n,x=1,y=1,Lx=0,Ly=0;
     cin>>n;
     char c;
     int p,t=0;
     for (int i=0;i<n;++i) 
     {
         cin>>c>>p;
         if (c=='O')
         {
               Lx+=abs(p-x)+1;
               Lx=max(Lx,Ly+1);
            x=p;
         } else
         {
                Ly+=abs(p-y)+1; 
                Ly=max(Ly,Lx+1);
             y=p;
         }
         t=max(Lx,Ly);
     }
     return t;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    cin>>T;
    for (int i=0;i<T;++i) 
    printf("Case #%d: %d\n",i+1,Solve());
    return 0;
}
