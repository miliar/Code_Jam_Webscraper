#include <cstdio>
#include <algorithm>
using namespace std;
int a[1005];
int T,N;
int main(){
    int ans,check;
    scanf("%d",&T);
    for (int i=0;i<T;++i){
        scanf("%d",&N);
        ans = check = 0;
        for (int j=0;j<N;++j){
            scanf("%d",&a[j]);
            ans += a[j];
            check ^= a[j];
        }    
        printf("Case #%d: ",i+1);
        if (check)
            printf("NO\n");
        else {
            sort(a,a+N);
            printf("%d\n",ans - a[0]);
        }
    }
}
