#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("Dlarge.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int k=0;k<t;++k){
        int n;
        scanf("%d",&n);
        int ar[n];
        int ans=0;
        for(int i=0;i<n;++i){
            scanf("%d",&ar[i]);
            if(ar[i]!=i+1)
                ++ans;
        }
        double a=ans*1.0;
        printf("Case #%d: %.6lf\n",k+1,a);


    }
return 0;
}
