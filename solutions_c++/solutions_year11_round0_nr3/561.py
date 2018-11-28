#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
using namespace std;

int arr[1005], n;

int main() {
    //freopen("D:\\C-small-attempt0.in","r",stdin);
    //freopen("D:\\C-small-attempt0.out","w",stdout);
    int t,c,i,tot,sum;
    scanf("%d",&t);
    for (c=1;c<=t;c++) {
        scanf("%d",&n);
        for (sum=tot=i=0;i<n;i++) {
            scanf("%d",arr+i);
            tot^=arr[i];
            sum+=arr[i];
        }
        printf("Case #%d: ",c);
        if (tot) {
            puts("NO");
        } else {
            sort(arr,arr+n);
            printf("%d\n",sum-*arr);
        }
    }
    return 0;
}
