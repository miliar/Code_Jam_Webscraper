#include<iostream>
#include<stdio.h>
#include<map>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<string>
#include<math.h>
using namespace std;

int main()
{
    //freopen("C-large.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int i,n,t,k,ans,min,sum,a;
    scanf("%d",&t);
    for(k=1;k<=t;k++) {
        printf("Case #%d: ",k);
        scanf("%d",&n);
        ans=sum=0; min=10000000;
        for(i=0;i<n;i++) {
            scanf("%d",&a);
            if(a<min) min=a;
            sum+=a;
            ans^=a;
        }
        if(ans!=0) printf("NO\n");
        else printf("%d\n",sum-min);
    }
    return 0;
}
