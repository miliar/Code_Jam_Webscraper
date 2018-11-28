#include<iostream>
using namespace std;

int num[10004];

int l,h;

int main()
{
    freopen("CCC22.in","r",stdin);
    freopen("CCC22.out","w",stdout);
    int t,cas=1,n,i,j;
    scanf("%d",&t);
    bool flag;
    while(t--)
    {
          printf("Case #%d: ",cas++);
          scanf("%d%d%d",&n,&l,&h);
          for(i=0;i<n;i++)
          {
               scanf("%d",&num[i]);
          }
          if(l==1)
          {
              printf("1\n");
              continue;
          }
          flag=false;
          for(i=l;i<=h&&!flag;i++)
          {
              flag=true;
              for(j=0;j<n&&flag;j++)
              if(num[j]%i!=0&&i%num[j]!=0)
              flag=false;
          }
          if(flag)
          printf("%d\n",i-1);
          else
          printf("NO\n");
    }
    return 0;
}
