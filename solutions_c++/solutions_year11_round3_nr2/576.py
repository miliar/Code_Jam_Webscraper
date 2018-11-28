#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <map>
using namespace std;
int ss[1200];
int w[1200];

int main()
{
    int t,cas,L,T,N,C,ai;
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    cas=0;
    while(t--)
    {
       scanf("%d%d%d%d",&L,&T,&N,&C);
       for(int i=0;i<C;i++)
       {
           scanf("%d",&ai);
           int k=0;
           while(k*C+i+1<=N)
           {
               w[k*C+i+1]=ai*2;
               k++;
           }
       }
       int sum=0;
       for(int i=1;i<=N;i++)
       {
           sum+=w[i];
           //cout<<w[i]<<endl;
       }
       ss[1]=w[1];
       for(int i=2;i<=N;i++)
       {
           ss[i]=ss[i-1]+w[i];
       }
       //for(int i=1;i<=N;i++)
         //cout<<ss[i]<<endl;
        //cout<<sum<<endl;
       printf("Case #%d: ",++cas);
       if(L==0)
         {
             printf("%d\n",sum);
             continue;
         }
       if(L==1)
       {
           bool flag=false;
           int mx=sum;
           int start;
           for(start=1;start<=N;start++)
             {
                 if(T<ss[start])
                   break;
             }
             for(int i=start;i<=N;i++)
             {
                 if(i==start)
                    {
                        mx=min(mx,sum-(ss[i]-T)/2);
                       //cout<<ss[i]<<" "<<t<<endl;
                    }
                 else
                    mx=min(mx,sum-w[i]/2);
                //cout<<mx<<" "<<sum<<endl;
             }
             printf("%d\n",mx);

       }
       else if(L==2)
       {
           int start;
           int mx=sum;
           for(start=1;start<=N;start++)
           {
               if(T<ss[start])
                 break;
           }
           for(int i=start;i<=N;i++)
             for(int j=i+1;j<=N;j++)
             {
                 int tmp;
                 tmp=sum;
                 if(i==start)
                    {
                        tmp=(ss[i]-T)/2;
                    }
                 else
                      tmp=w[i]/2;
                 tmp+=w[j]/2;
                 mx=min(mx,sum-tmp);


             }
             printf("%d\n",mx);
         }

    }
    return 0;

}
