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
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,steven=1,i,j,k,N;
    int a[1010],b[1010];
    for(scanf("%d",&T);steven<=T;steven++)
    {
       cin>>N;
       for(i=0;i<N;i++)scanf("%d %d",a+i,b+i);
       int sum=0;
       for(i=0;i<N;i++)
       {
          for(j=i+1;j<N;j++)
          {
             if(a[i]>a[j]&&b[i]<b[j])sum++;
             else if(a[i]<a[j]&&b[i]>b[j])sum++;               
          }                
       }
       printf("Case #%d: %d\n",steven,sum);

    }
    //system("pause");
    return 0;
}
