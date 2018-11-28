#include <cstdio>
#include <cmath>
#include <cstring>
using namespace std;
#define abs(a) ((a)>=0?(a):-(a))
#define max(a,b) (a>b?a:b)

int main(){
    int debug = 1;
    if( debug ){
        freopen("C-large.in","r",stdin);
        freopen("C-large.out","w",stdout);
    }
    int Cas, n;
    scanf("%d",&Cas);
    for(int cas=1; cas<=Cas; ++cas){
        scanf("%d",&n);
        int sum = 0, res = -1, flag = 0;
        for(int i=1; i<=n; ++i){
            int a;
            scanf("%d",&a);
            flag = flag ^ a;
            sum += a;
            if( res == -1 || a < res ) res = a;
        }
        printf("Case #%d: ",cas);
        if( flag ) printf("NO\n"); else printf("%d\n",sum-res);
    }
    if( debug ){
        fclose(stdin);
        fclose(stdout);
    }
    return 0;
}
