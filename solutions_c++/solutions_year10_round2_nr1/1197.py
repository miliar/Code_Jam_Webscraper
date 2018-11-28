#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

int t,n,m,ans;
char ch[110];
string a[105],b[105];

int bin_search(int k)
{
    if(n==0)return 0;
    int tmp=-1,ret=0,i;
    int l=0,r=n-1,mid;
    while(l<=r)
    {
        mid=(l+r)/2;
        if(a[mid]>b[k])r=mid-1;
        else
        {
            tmp=mid;
            l=mid+1;
        }
    }
    if(tmp==-1)return 0;
    for(i=0;i<a[tmp].size()&&i<b[k].size();i++)
    {
        if(a[tmp][i]==b[k][i])
        {
            if(b[k][i]=='/')ret++;
        }
        else break;
    }
    if(!(i==a[tmp].size()&&(i==b[k].size()||b[k][i]=='/')))ret--;
    return ret;
}

int main()
{
    int i,j,k1,k2,tmp,bla;
    scanf("%d",&t);
    getchar();
    bla=0;
    for(;t;t--)
    {
        bla++;
        ans=0;
        scanf("%d%d",&n,&m);
        getchar();
        for(i=0;i<n;i++)
        {
            scanf("%s",ch);
            a[i]=ch;
        }
        for(i=0;i<m;i++)
        {
            scanf("%s",ch);
            b[i]=ch;
        }
        sort(a,a+n);
        sort(b,b+m);
        for(j=0;j<m;j++)
        {
            tmp=0;
            for(i=0;i<b[j].size();i++)
             tmp+=(b[j][i]=='/');
            k1=k2=0;
            if(j)
            {
                for(i=0;i<b[j].size()&&i<b[j-1].size();i++)
                {
                    if(b[j][i]==b[j-1][i])
                    {
                        if(b[j][i]=='/')k2++;
                    }
                    else break;
                }
                if(!(i==b[j-1].size()&&(i==b[j].size()||b[j][i]=='/')))k2--;
            }
            k1=bin_search(j);
            ans+=tmp-max(k1,k2);
        }
        printf("Case #%d: %d\n",bla,ans);
    }
}
