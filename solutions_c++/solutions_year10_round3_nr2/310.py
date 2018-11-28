#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<functional>
using namespace std;
const int INF=(1<<31)-1;
const double EPS=1e-8;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,steven=1,j,i,k;
    long long L,P,C;
    for(scanf("%d",&T);steven<=T;steven++)
    {
       cin>>L>>P>>C;
       long long t=L;
       int sum=0;
       while(t<P)
       {
          t*=C;
          sum++;        
       }
       //if(t==P)sum--;
       int ans=0;
       int xx=1;
       while(xx<sum)
       {
          xx<<=1;             
       }
       if(xx==sum)ans=-1;
       while(sum>0)
       {
         sum>>=1;
         ans++;            
       }
       printf("Case #%d: %d\n",steven,ans);

    }
    //system("pause");
    return 0;
}
