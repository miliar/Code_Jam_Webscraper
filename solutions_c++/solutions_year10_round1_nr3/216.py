#include<iostream>
#include<algorithm>
using namespace std;
int start[1000010],end[1000010];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    
    int t,a1,a2,b1,b2;
    int x,i,j;
    start[1]=1;
    end[1]=1;
    start[2]=2;
    end[2]=3;
    for(i=3;i<=1000000;i++)
    {
                           int *p;
                           p=lower_bound(&end[1],&end[i-1],i);
                           start[i]=p-end;
                           end[i]=start[i]+i-1;
                           }
    
    /*for(i=1;i<=100;i++)
    printf("%d: %d %d\n",i,start[i],end[i]);*/
    
    scanf("%d",&t);
    for(x=0;x<t;x++)
    {
                    scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
                    long long ans=0;
                    for(i=a1;i<=a2;i++)
                    {
                                       int temp=max(0,min(end[i],b2)-max(start[i],b1)+1);
                                       ans+=(long long)(b2-b1+1-temp);
                                       }
                    printf("Case #%d: %lld\n",x+1,ans);
                    }
    //scanf(" ");
    return 0;
    }
