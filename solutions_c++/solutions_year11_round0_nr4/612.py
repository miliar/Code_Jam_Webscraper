#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#define MAXN 1000

using namespace std;

int T,N;
int a[MAXN+10];
int k;
bool temp[MAXN+10];

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    double ans;
    for(int t=1;t<=T;t++)
    {
        memset(temp,0,sizeof(temp));
        ans=0;
       scanf("%d",&N);
       for(int i=1;i<=N;i++) scanf("%d",&a[i]);
       for(int i=1;i<=N;i++)
       {
           k=0;
           if(temp[i]) continue;
           int p=a[i];
           while(p!=i)
           {
               temp[p]=1;
               p=a[p];
               k++;
           }
           if(k) ans+=k+1;
       }
       printf("Case #%d: %.6lf\n",t,ans);
    }
    return 0;
}
