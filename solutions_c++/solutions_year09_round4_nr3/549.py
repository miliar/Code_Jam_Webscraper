#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int t;
int n,k,ss;
int u[100];

struct node{
       int a[25];}
       s[100];
int cmp(node a,node b)
{
    int i;
   
    return a.a[ss]>b.a[ss];
}  

int get(node a,node b)
{
    int i;
    for(i=0;i<k;i++)
    if(a.a[i]<=b.a[i])
    return 0;
    return 1;
}  
int main()
{
    int i,j,kk,Case;
    int res,res1;
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    scanf("%d",&t);
    for(Case=1;Case<=t;Case++)
    {
                        scanf("%d%d",&n,&k);
                        for(i=0;i<n;i++)
                          for(j=0;j<k;j++)
                          scanf("%d",&s[i].a[j]);
                          res=100000;
                          for(ss=0;ss<k;ss++)
                          {
                                             sort(s,s+n,cmp);
                          res1=0;
                          int sum=0;
                          int tmp;
                          memset(u,0,sizeof(u));
                          node aa;
                          while(sum<n)
                          {
                                      tmp=0;
                                      for(i=0;i<n;i++)
                                      if(u[i]==0)
                                      {
                                                 if(!tmp||get(aa,s[i]))
                                                 {
                                                                    u[i]=1;
                                                     aa=s[i];
                                                     sum++;
                                                     tmp=1;
                                                 }
                                                           
                                      }
                                      res1++;
                          }
                          if(res1<res)
                          res=res1;
                          }
                          printf("Case #%d: %d\n",Case,res);
    }
    return 0;
}
                          
                          
                        
