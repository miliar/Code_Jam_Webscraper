#include<iostream>
#include<string>
#include<vector>
#include<set>
using namespace std;

int cas,n,k,b,t;
int x[55],v[55],c[55];
bool f[55];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    scanf("%d",&cas);
    
    for(int cnt=1;cnt<=cas;cnt++)
    {
         scanf("%d%d%d%d",&n,&k,&b,&t);
         memset(f,0,sizeof(f));
         memset(c,0,sizeof(c));
         
         for(int i=0;i<n;i++) scanf("%d",&x[i]);
         for(int i=0;i<n;i++) scanf("%d",&v[i]);
         
         for(int i=n-1;i>=0;i--)
         {
             if((double)(b-x[i])/v[i]<=t)
             {
                 f[i]=1;
                 c[i]=c[i+1];
             }
             else
                 c[i]=c[i+1]+1;
         }
     //    for(int i=0;i<n;i++) printf("%d ",c[i]);
     //    printf("\n");
         int num=0,count=0,i; 
         for(i=n-1;i>=0;i--)
         {
             if(f[i])
             {
                 num+=c[i];
                 count++;
             }
             if(count==k) break;
         }
         printf("Case #%d: ",cnt);
         if(i<0) printf("IMPOSSIBLE\n");
         else printf("%d\n",num);
         
    }
    return 0;
} 
