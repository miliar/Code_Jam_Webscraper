#include <stdio.h>
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    long i,n;
    long test,order,mn,end1,end2;
    long a[1005];
    scanf("%ld",&test);
    for(order=1;order<=test;order++){
        printf("Case #%ld: ",order);
        scanf("%ld",&n);
        end1=end2=0;
        mn=0x3f3f3f3f;
        for(i=0;i<n;i++){
            scanf("%ld",&a[i]);
            if(mn>a[i])
                mn=a[i];
            end1+=a[i];
            end2^=a[i];
        }
        if(end2!=0)
            printf("NO\n");
        else
            printf("%ld\n",end1-mn);
    }
    return 0;
}
