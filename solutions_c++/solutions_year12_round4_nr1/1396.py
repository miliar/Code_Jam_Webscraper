#include<stdio.h>
#include<iostream>
using namespace std;
int n,d[10000],l[10000],start[10000],mark[10000],pos,dis;

int calculate(int i,int po)
{
    int j,k,ans,val;
    
    if(i>=dis)
    return 1;
    
    for(j=po+1;j<n;j++)
    {
                      if(d[j]<=i)
                      {
                                 val=-d[po]+d[j];
                                 
                                 if(val>l[j])
                                 val=l[j];
                                     //mark[j]=1;
                                     ans=calculate(d[j]+val,j);
                                     if(ans==1)
                                     return 1;
                      }
    }
    
    return 0;
    
}
int main()
{
    int t,i,j;
    
    scanf("%d",&t);
    
    for(i=0;i<t;i++)
    {
            scanf("%d",&n);
            
            for(j=0;j<n;j++)
            {
                            scanf("%d%d",&d[j],&l[j]);
                            start[j]=d[j]-l[j];
                            if(start[j]<0)
                            start[j]=0;
                            mark[j]=0;
            }
            scanf("%d",&dis);
            pos=0;
            printf("Case #%d: ",i+1);
            if(d[0]<=l[0])
            if(calculate(2*d[0],0))
            printf("YES\n");
            else
            printf("NO\n");
            else
            printf("NO\n");
    }
    return 0;
}
