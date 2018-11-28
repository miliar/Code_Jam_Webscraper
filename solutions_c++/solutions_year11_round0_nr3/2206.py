#include <cstdio>
#include <algorithm>

using namespace std;

int main(){
    int ncas;
    scanf("%d",&ncas);
    for(int m=1;m<=ncas;m++){
        int n;
        int a[10000];
        int xorsum = 0;
        int sum = 0;
        int mini = 999999;
        scanf("%d",&n);
        for(int i=0;i<n;i++) scanf("%d",&a[i]);
        for(int i=0;i<n;i++){
            xorsum ^= a[i];
            sum += a[i];
            mini = min(a[i],mini);
        }
        
        printf("Case #%d: ",m);
        if(xorsum == 0) printf("%d\n",sum-mini);
        else printf("NO\n");
    }
    return 0;
}
