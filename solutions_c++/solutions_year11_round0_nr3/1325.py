#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[10000];

int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cas,r=1; scanf("%d",&cas);
    while(cas--){
        int n; scanf("%d",&n);
        int s=0;
        for(int i=0; i<n; i++) {
            scanf("%d",&a[i]);
            s^=a[i];
        }
        printf("Case #%d: ",r++);
        if(s!=0) { puts("NO"); continue; }
        sort(a,a+n);
        int sum=0;
        for(int i=1; i<n; i++){
            sum+=a[i];
        }
        printf("%d\n",sum);
    }
}
