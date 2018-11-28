#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int a,b,ans,p[8],ws,ss[8];
bool hash[2000001];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test,i,q,j,k;
    scanf("%d",&test);
    for(q=1;q<=test;q++)
    {
      scanf("%d%d",&a,&b);
      ans=0;
      for(i=a;i<=b;i++)
      {
        int tmp=i;
        ws=0;
        while(tmp)
        {
          p[++ws]=tmp%10;
          tmp/=10;
        }
        for(j=1;j<ws;j++)
        {
          p[0]=p[1];
          for(k=1;k<ws;k++)p[k]=p[k+1];
          p[ws]=p[0];
          tmp=0;
          for(k=ws;k>=1;k--)tmp=tmp*10+p[k];
          ss[j]=tmp;
        }
        sort(&ss[1],&ss[ws]);
        for(j=1;j<ws;j++)
          if(ss[j]<i&&ss[j]>=a&&ss[j]<=b&&(ss[j]!=ss[j-1]||j==1))ans++;
      }
      printf("Case #%d: %d\n",q,ans);
    }
    return 0;
}
