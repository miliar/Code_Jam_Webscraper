#include <iostream>
#include <cmath>
using namespace std;

#define mset(a,x) memset(a,x,sizeof(a))
typedef long long i64;
const int INF=INT_MAX/2;

int a[1005];
int b[1005];

int main()
{
    int T,n,kcase(0);
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
        }
        sort(a,a+n);
        for(int i=0;i<n;i++){
            scanf("%d",&b[i]);
        }
        sort(b,b+n);
        int res=0;
        for(int i=0;i<n;i++){
            res+=a[i]*b[n-1-i];
        }
        printf("Case #%d: %d\n",++kcase,res);
    }
}
