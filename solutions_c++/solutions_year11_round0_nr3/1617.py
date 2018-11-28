#include <iostream>
using namespace std;

int T, N, C;
int val[1010];
int ft, total;


void init() {
    cin >> N;
    C = 10000000;
    ft = 0;
    total = 0;
    for( int i = 0; i < N; i++ ) {
        cin >> val[i];
        C = min(C, val[i]);
        ft = ft^val[i];
        total += val[i];
    }
}

void solve(int tc) {
    if( ft != 0 ) {
        printf("Case #%d: NO\n", tc);
        return;
    }
    int ret = total - C;
    printf("Case #%d: %d\n", tc, ret);
}

int main() {
    cin >> T;
    for( int k = 1; k <= T; k++ ) {
        init();
        solve(k);
    }
    //system("pause");
    return 0;
}
