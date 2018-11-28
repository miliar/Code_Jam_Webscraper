#include<iostream>
#include<cmath>
using namespace std;
void solve(int id)
{
     int n,sum=0;
     cin>>n;
     int Min=1000000000,Ans=0,x;
     for (int i=0;i<n;++i)
     {
      cin>>x;
      Ans=Ans ^ x;
      Min=min(Min,x);
      sum+=x;
     }
     if (Ans==0)
     {
        printf("Case #%d: %d\n",id,sum-Min);   
     } else
     {
       printf("Case #%d: NO\n",id);
     }
     
}

int main()
{
    freopen("C-large.in","r",stdin);
        freopen("C-large.txt","w",stdout);
    int T;
    cin>>T;
    for (int i=0;i<T;++i)
    solve(i+1);
    return 0;
}
