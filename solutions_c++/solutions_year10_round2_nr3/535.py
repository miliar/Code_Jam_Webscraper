#include<iostream>
#include<vector>
using namespace std;

vector<int> a;
int t,n,res;
int rcd[30];

bool v[26];
void dfs(int x)
{
     if(x==n+1) 
     {
      //   for(int i=1;i<=n;i++) printf("%d ",v[i]); printf("\n");
         if(!v[n]) return;
         a.clear();
         for(int i=2;i<=n;i++)
             if(v[i]) a.push_back(i);
    //     /*
         
         int b=n;
      //   printf("b=%d\n",b);
         while(1)
         {
              int i;
              for(i=0;i<a.size();i++) 
                  if(a[i]==b) break;
              if(i==a.size()) return;
              b=i+1;
           //   printf("b=%d\n",b);
              if(b==1) break;
         }
         res=(res+1)%100003; 
     //    for(int i=0;i<a.size();i++) printf("%d ",a[i]); printf("\n");
   //      */
         return;
     } 
     v[x]=1;
     dfs(x+1);
     v[x]=0;
     dfs(x+1);
}

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    
    for(int i=2;i<=25;i++) 
    {
        n=i;
        memset(v,0,sizeof(v));
        res=0;
        dfs(2);
        rcd[i]=res;
    }
    
  //  for(int i=2;i<=25;i++) printf("%d ",rcd[i]);
    
    scanf("%d",&t);
    for(int cnt=1;cnt<=t;cnt++)
    {
        scanf("%d",&n);
     //   memset(v,0,sizeof(v));
     //   res=0;
     //   dfs(2);
        printf("Case #%d: %d\n",cnt,rcd[n]);
    }
    
    return 0;
}
