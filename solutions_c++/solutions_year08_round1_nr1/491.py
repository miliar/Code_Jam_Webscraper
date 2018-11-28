#include <stdio.h>
#include <functional>
#include <algorithm>
#define MAX 810

using namespace std;
int main(){
    int t_case,t,n,i;
    int a[MAX],b[MAX],res;
    scanf("%d",&t_case);
    for (t = 1;t <= t_case;t++){
        scanf("%d",&n);
        for (i = 0;i < n;i++) scanf("%d",&a[i]);
        for (i = 0;i < n;i++) scanf("%d",&b[i]);
        sort(a,a+n);
        sort(b,b+n,greater<int>());
        res = 0;
        for (i = 0;i < n;i++)
            res += a[i]*b[i];
        printf("Case #%d: %d\n",t,res);
    }
}
