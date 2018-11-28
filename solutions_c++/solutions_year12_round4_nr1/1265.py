#include<iostream>
#include<algorithm>
#include<string.h>
#include<math.h>
#include<stdio.h>
#define N 1000010
#define lp(i,n) for(i=0;i<n;i++)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
using namespace std;

long long n,i,j,k,ans,m,d,tt,time;
long long a[N];
char s[N];
bool flag,f[N];
long long sum=0,tmp,dis[N];

struct vine
{
    double l;
    double d;
}v[N];

FILE *in,*out;

int main()
{
    in=freopen("A-large.in","r",stdin);
    out=freopen("A-large.out","w",stdout);
    cin>>tt;
    for (time=1;time<=tt;time++)
    {
        cin>>n;
        lp(i,n)
            cin>>v[i].d>>v[i].l;
        cin>>d;
        memset(dis,0,sizeof(dis));
        dis[0]=v[0].d;
        for (i=1;i<n;i++)
        {
            sum=0;
            for (j=0;j<i;j++)
            {
                if (v[j].d+dis[j]>=v[i].d)
                    if (min(v[i].d-v[j].d,v[i].l)>sum)//change the saver
                        sum=min(v[i].d-v[j].d,v[i].l);
            }
            dis[i]=sum;
        }
        flag=false;
        i=0;
        while (i<n && !flag)
        {
            if (dis[i]+v[i].d>=d)
                flag=true;
            i++;
        }
        if (flag)
            cout<<"Case #"<<time<<": "<<"YES"<<endl;
        else
            cout<<"Case #"<<time<<": "<<"NO"<<endl;
    }
    return 0;
}
