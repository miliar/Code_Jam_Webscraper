#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;
int a[31];
int b[31];
int x[100];
int main()
{
    int t,T,n,i,j,s,p;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);   
    for(i=0;i<=30;i++)
    {
        a[i]=(i+2)/3;
        b[i]=min((i+4)/3,10);
    }
    b[0]=0;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d%d",&n,&s,&p);
        int ans=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&x[i]);
            if(a[x[i]]>=p) ans++;
            else if(s && b[x[i]]>=p) 
            {
                ans++;
                s--;
            }
        }            

        printf("Case #%d: %d\n",t,ans);
    }
//system("pause");
    return 0;
}
