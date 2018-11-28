#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <iomanip>
#include <fstream>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)return a;
    return gcd(b, a % b);
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    long long n, pd, pg;
    scanf("%d", &t);
    for (int i = 0; i < t; i++) {
        cin >> n >> pd >> pg;
        printf("Case #%d: ", i + 1);
        if (pd == 0){
            if (pg == 100) printf("Broken\n");
            else printf("Possible\n");
            continue;
        }
        long long d = gcd(100, pd);
        if (n >= 100 / d) {
            if (pg == 100) {
                if (pd == 100) printf("Possible\n");
                else printf("Broken\n");
            } else if (pg == 0) {
                if (pd == 0) printf("Possible\n");
                else printf("Broken\n");
            } else printf("Possible\n");
        } else {
            printf("Broken\n");
        }
    }
    return 0;
}

