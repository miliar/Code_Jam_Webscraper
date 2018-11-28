#include<cstdio>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    int T;
    scanf("%d",&T);
    for(int t = 0 ;  t < T ; t++) {
        int N,K;
        scanf("%d%d",&N,&K);
        bool Sign = true;
        for(int i = 0 ; i < N ; i++) {
            if (((1 << i) & K) == 0) {
                Sign = false;
                break;
            }
        }
        printf("Case #%d: ",t + 1);
        if (Sign) printf("ON\n");
        else printf("OFF\n");
    }
    
    return 0;
}
