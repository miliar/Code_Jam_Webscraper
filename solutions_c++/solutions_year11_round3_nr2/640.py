#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<math.h>
using namespace std;

int T;
int l,t,n,c;
int a[1005];
int p[1005];

void sol1()
{
    int i,j;
    int ans=2*p[n];
    int tmp;
    for(i=0;i<n;i++)
    {
        if(t<=2*p[i+1])
        {
            if(t<=2*p[i])
                tmp=2*p[n]+p[i]-p[i-1];
            else
                tmp=2*p[n]+p[i]-p[i+1]+(t-2*p[i])/2;
        }
        if(tmp<ans)
            ans=tmp;
    }
    printf("%d\n",ans);
    return;
}

void sol2()
{
    int i,j;
    int ans=2*p[n];
    int tmp1,tmp2;
    for(i=0;i<n;i++)
    {
        if(t<=2*p[i+1])
        {
            if(t<=2*p[i])
                tmp1=p[i]+p[i+1];
            else
                tmp1=p[i+1]+p[i]+(t-2*p[i])/2;
            for(j=i+1;j<n;j++)
            {
                if(t<=2*(p[j+1]-p[i+1])+tmp1)
                {
                    if(t<=2*(p[j]-p[i+1])+tmp1)
                        tmp2=p[j+1]-p[j];
                    else
                    {
                        tmp2=p[j+1]-p[j];
                        tmp2=tmp2-(t+2*p[i+1]-2*p[j]-tmp1)/2;
                    }
                }
                if(tmp1-tmp2+2*p[n]-2*p[i+1]<ans)
                    ans=tmp1-tmp2+2*p[n]-2*p[i+1];
            }
        }
    }
    printf("%d\n",ans);
    return;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("bs1.txt","w",stdout);
    int i,j;
    scanf("%d",&T);
    int cnt=1;
    while(T--)
    {
        printf("Case #%d: ",cnt++);
        scanf("%d %d %d %d",&l,&t,&n,&c);
        for(i=0;i<c;i++)
            scanf("%d",&a[i]);
        int x=0;
        p[0]=0;
        for(i=1;i<=n;i++)
        {
            p[i]=p[i-1]+a[x];
            x++;
            x%=c;
        }
        if(l==0)
        {
            printf("%d\n",2*p[n]);
            continue;
        }
        if(l==1)
        {
            sol1();
            continue;
        }
        if(l==2)
        {
            sol2();
            continue;
        }
    }
    //system("pause");
    return 0;
}
