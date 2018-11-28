#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<set>
#include<cmath>
#include<map>
#include<string>
#include<sstream>
#include<queue>

using namespace std;

int main() {

    //freopen("A-small.in", "r", stdin);
    //  freopen("A-small.out", "w", stdout);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int nth = 1; nth <= cas; nth++) {
        int N, K;
        scanf("%d%d", &N, &K);
        int P = 1;
        for (int i = 1; i <= N; i++) P *= 2;
        if ((K + 1) % P == 0) printf("Case #%d: ON\n", nth);
        else printf("Case #%d: OFF\n", nth);

    }


    return 0;
}
