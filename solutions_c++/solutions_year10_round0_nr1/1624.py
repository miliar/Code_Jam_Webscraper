#include<sstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i=0;i<(n);i++)
#define foru(i,a,b) for (int i=(a);i<=(b);i++)
#define ford(i,a,b) for (int i=(a);i>=(b);i--)

int n, K;

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d%d", &n, &K);
        //n = 30;
        K++;
        int P = (1 << n) - 1;
        //printf("%d\n", P);
        printf("Case #%d: %s\n", tt + 1, (P & K) ? "OFF" : "ON");
    }
}

