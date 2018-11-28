#include <iostream>
#include <stdio.h>
#include <memory.h>
using namespace std;

int a[20000],b[20000],c[20000];

int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int ca=0,tem,t,i,last1,last2,now1,now2,k1,k2,x,k,op,l1,l2,ans;
    char cc;
    scanf("%d",&t);
    while(t--)
    {
        ++ca;
        scanf("%d",&op);
        k1=0; k2=0; k=0;
        for(i=1;i<=op;i++)
        {
            scanf(" %c %d",&cc,&x);
            if(cc=='O')
            {
                a[++k1]=x;
                c[++k]=1;
            }
            else
            {
                b[++k2]=x;
                c[++k]=2;
            }
        }
        ans=0; now1=0; now2=0; last1=0; last2=0; l1=1; l2=1;
        for(i=1;i<=k;i++)
        {
            if(c[i]==1)      // 1
            {
                ++now1;
                tem=a[now1]-l1;
                if(tem<0) tem=-tem;
                ans=last1+tem>ans?last1+tem:ans; ans++;
                last1=ans; l1=a[now1];
            }
            else
            {
                ++now2;
                tem=b[now2]-l2;
                if(tem<0) tem=-tem;
                ans=last2+tem>ans?last2+tem:ans; ans++;
                last2=ans; l2=b[now2];
            }
        }
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}