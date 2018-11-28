#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
typedef long long ll;
#define M 105
#define INF 1<<30
int t,n,s,p;
int a[M];
int c[M];
int gao(int x,int y)
{
    if(x>=p)
    return 1;
    if(y==0)
    {
        if(p==x+1 && x>0)
        return 2;
    }
    if(y==1)
    {
        if(p==x+1)
        return 1;
    }
    if(y==2)
    {
        if(p==x+1)
        return 1;
        if(p==x+2)
        return 2;
    }
    return 0;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        memset(c,0,sizeof(c));
        printf("Case #%d: ",cas);
        scanf("%d %d %d",&n,&s,&p);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            int x=a[i]/3;
            int y=a[i]%3;
            c[i]=gao(x,y);
        }
        int a1=0,a2=0;
        for(int i=0;i<n;i++)
        {
            if(c[i]==1)
            a1++;
            if(c[i]==2)
            a2++;
        }
        if(a2>=s)
        printf("%d\n",a1+s);
        else
        printf("%d\n",a1+a2);
    }
	return 0;
}
