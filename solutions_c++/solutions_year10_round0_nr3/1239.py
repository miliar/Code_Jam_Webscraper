#include<iostream>
using namespace std;
int main()
{
    int t,r,k,n;
    int g[20];
    int i,j;
    int ans;
    int now;
    int flag;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int head,end;
    for(i=1;i<=t;i++)
    {
      scanf("%d%d%d",&r,&k,&n);
     // cout<<r<<" "<<k<<" "<<n<<endl;
      for(j=0;j<n;j++)
          scanf("%d",&g[j]);
      head=0;
      flag=0;
      ans=0;
      for(j=1;j<=r;j++)
      {
         now=0;
         flag=head;
         while(1)
         {
            if(now+g[head]>k) break;
            else now+=g[head++];
            head%=n;
            if(flag==head) break;
         }
         ans+=now;
      } 
      printf("Case #%d: %d\n",i,ans);
    }
    //while(1);
    return 0;
}
