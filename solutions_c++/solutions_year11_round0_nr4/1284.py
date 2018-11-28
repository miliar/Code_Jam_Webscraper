#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    int C,n,a[1000],b[1000],Case=1;
    double ans;
    scanf("%d",&C);
    while(C--){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            b[i]=a[i];
        }
        sort(b,b+n);
        ans=0.0;
        for(int i=0;i<n;i++)
            if(a[i]!=b[i])
                ans+=1.0;
        printf("Case #%d: %.6lf\n",Case++,ans);
    }
}
