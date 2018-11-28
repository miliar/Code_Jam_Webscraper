#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>

using namespace std;

int mat[10000];
int main()
{
    freopen("/home/renxl/下载/in","r",stdin);
    freopen("out","w",stdout);
    int i,j,n,m=1,t,ans,Min,p,temp,z,num;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++)
        {
            scanf("%d",&mat[i]);
        }
        ans=0;
        for(i=1;i<=n;i++)
        {
            if(mat[i]==0)continue;
            temp=mat[i];
            mat[i]=0;
            num=1;
            while(mat[temp]!=0)
            {
                num++;
                z=temp;
                temp=mat[temp];
                mat[z]=0;
            }
            if(num!=1)ans+=num;
        }
        printf("Case #%d: %d.000000\n",m++,ans);
    }
}
