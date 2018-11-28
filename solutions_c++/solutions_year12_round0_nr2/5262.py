#include <cstdio>
#include <algorithm>
using namespace std;
int a[3];

int main() {
    int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++) {
        int N,S,p;
        scanf("%d %d %d", &N, &S, &p);
        for(int i = 0; i < N; i++) {
            scanf("%d", &a[i]);
        }
        int ret = 0;
        for(int m = 0; m < (1<<N); m++) {
            if(__builtin_popcount(m) == S) {
                int tmp = 0;
                for(int i = 0; i < N; i++)if(((m>>i)&1)) {
                    if(a[i]%3 == 0) {
                        if(a[i]) {
                            if(a[i]/3 + 1 >= p) {
                                tmp++;
                            }
                        }else tmp = -(0x3f3f3f3f);
                    }else if(a[i]%3 == 1) {
                        if(a[i] >= 4) {
                            tmp += (a[i]/3 + 1) >= p;
                        }else {
                            tmp = -(0x3f3f3f3f);
                        }
                    }else {
                        tmp += (a[i]/3 + 2) >= p;
                    }
                }else {
                    tmp += (a[i]/3 + (a[i]%3 > 0)) >= p;
                }
                ret = max(ret, tmp);
            }
        }
        printf("Case #%d: %d\n", t, ret);
    }
    return 0;
}
