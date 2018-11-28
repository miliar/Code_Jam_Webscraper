#include<iostream>
using namespace std;
int main()
{
    int i,j,k;
    int t,n,ans;
    long long tmp;
    int L,P,C;
    freopen("B-large.in","r",stdin);
    freopen("ou.txt","w",stdout);
    scanf("%d",&t);
    for(int ii=1;ii<=t;ii++)
    { 
      ans=0;
      scanf("%d%d%d",&L,&P,&C);
      n=0;
      tmp=L;
      while(1)
      {
         tmp*=C;
         n++;
         if(tmp>=P) break;
      }
      tmp=1;
      while(1)
      {
        if(tmp>=n) break;
        ans++;
        tmp*=2;
      }
      printf("Case #%d: %d\n",ii,ans);
    }
   // while(1);
    return 0;
}
