#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[1005];
int main(){
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cas,r=1; 
    scanf("%d",&cas);
    while(cas--){
        int n,y=0,sum=0;; 
        scanf("%d",&n);
        for(int i=0; i<n; i++) {
            scanf("%d",&a[i]);
            y^=a[i];
        }
        sort(a,a+n);
        printf("Case #%d: ",r++);
        if(y!=0) puts("NO");
        else{
            for(int i=1; i<n; i++){
                sum+=a[i];
            }
            printf("%d\n",sum);
        }
    }
}
