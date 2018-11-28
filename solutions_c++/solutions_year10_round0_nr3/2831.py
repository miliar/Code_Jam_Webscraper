#include <iostream>
using namespace std;
int a[1010];
int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C.out","w",stdout);
    int T,n,r,k;
    scanf("%d",&T);
    for(int I = 1;I <= T;++I){
        int ans(0),tmp,j;
        scanf("%d%d%d",&r,&k,&n);
        int cir(0),cir1,ans1(0);
        for(int i = 0;i < n;++i) scanf("%d",&a[i]);
        j = 0;
        for(int i = 0;i < r;++i){
            cir1 = tmp = 0;
            while(cir1 < n && tmp + a[j] <= k){
                tmp += a[j];
                ans += a[j];
                j = (j+1) % n;
                ++cir1;
            }
        }
/*      if(cir1 > 0 && cir < r)
        for(int i = 0;i < r % cir1;++i){
            tmp = 0;
            while(tmp + a[j] <= k){
                ans += a[j];
                tmp += a[j];
                j = (j+1) % n;
            }
        }*/
        printf("Case #%d: %d\n",I,ans);
    }
}
