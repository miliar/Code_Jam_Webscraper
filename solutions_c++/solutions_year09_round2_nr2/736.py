#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>

using namespace std;

int i,j,k,a[30],t,n,p,Q;
char c;
bool done;

main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d%c",&t,&c);
    for(Q=1;Q<=t;Q++)
    {
        done=false;
        scanf("%c",&c); n=0;
        while(c!='\n')
        {
            a[n]=c-'0';
            n++;
            scanf("%c",&c);
        }
        for(i=n-2;i>=0;i--)
        {
            k=i; p=10;
            for(j=i+1;j<n;j++)
                if(a[j]>a[i] && a[j]<p) { p=a[j]; k=j; }
            if(k!=i)
            {
                swap(a[i],a[k]);
                sort(a+i+1,a+n);
                done=true;
                break;
            }
        }
        printf("Case #%d: ",Q);
        if(!done)
        {
            k=0;
            for(i=0;i<n;i++)
                if(a[i]==0)k++;
            sort(a,a+n);
            printf("%d",a[k]);
            for(i=0;i<=k;i++) printf("0");
            for(i=k+1;i<n;i++) printf("%d",a[i]);
            printf("\n");
        } else
        {
            for(i=0;i<n;i++) printf("%d",a[i]);
            printf("\n");
        }
    }
}
