#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<iostream>
using namespace std;
int T,i,j,k,n,l,h,flag;
int f[10000];
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w+",stdout);
    scanf("%d",&T);
    for(k=1;k<=T;k++) {
        scanf("%d%d%d",&n,&l,&h);
        for(i=0;i<n;i++) {
            scanf("%d",&f[i]);
        }
        flag=1;
        for(i=l;i<=h;i++) {
            for(j=0;j<n;j++) {
                if ( ( (i % f[j])==0) || ((f[j] % i)==0) ) {
                    continue;
                }
                else {
                    flag=-1;
                    break;
                }
            }
            if (j==n) {
                flag=1;break;
            }
        }
        if (flag==1) printf("Case #%d: %d\n",k,i);
        else printf("Case #%d: NO\n",k);
    }
    return 0;
}
