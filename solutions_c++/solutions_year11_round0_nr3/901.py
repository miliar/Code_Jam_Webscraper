#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("CLARGE.txt","w",stdout);
    int t;
    scanf("%d",&t);

    for(int k=0;k<t;++k){
        int n;
        scanf("%d",&n);
        int ar[n];
        int ans=10000000,sum=0;
        for(int i=0;i<n;++i){scanf("%d",&ar[i]);ans=min(ar[i],ans);sum+=ar[i];}
        int bit=1;
        bool poss=true;
        for(int i=0;i<20;++i){
            int ons=0;
            for(int j=0;j<n;++j)
                if(ar[j]&bit)
                    ++ons;
            if(ons%2){poss=false;break;}
            bit<<=1;
        }
        printf("Case #%d: ",k+1);
        if(poss)
            printf("%d\n",sum-ans);
        else
            printf("NO\n");

    }
return 0;
}
