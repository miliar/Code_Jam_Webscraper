#include <cstdio>
using namespace std;
int main(){
    freopen("al.in","r",stdin);
    freopen("al2.out","w",stdout);
    int T;
    scanf("%d", &T);
    int n;
    long long k;
    for (int i = 1; i <= T; ++i) {
        scanf("%d%I64d", &n, &k);
        long long x = (1 << n) ;
        bool flag = false;
        if ((k >= (x -1))  && ((k+1) % x == 0)) {
            flag = true;
        }
        printf("Case #%d: %s\n", i, flag?"ON":"OFF");
    }
    return 0;
}
