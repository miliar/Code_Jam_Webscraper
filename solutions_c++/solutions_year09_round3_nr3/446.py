/* 
 * File:   main.cpp
 * Author: kiril
 *
 * Created on September 13, 2009, 12:53 PM
 */

#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int prison[1000];
int released[10];
int p, q;

void input() {
    memset(prison, 0, sizeof(prison));
    scanf("%d %d", &p, &q);
    for(int i = 0; i < q; i++) {
        scanf("%d", &released[i]);
    }
}

long calcBridge() {
    long ans = 0;
    for(int i = 0; i < q; i++) {
        prison[released[i]] = 1;
        for(int j = released[i]+1; j <= p; j++) {
            if (prison[j] == 1) {
                break;
            }
            ans++;
        }
        for(int j = released[i]-1; j > 0; j--) {
            if (prison[j] == 1) {
                break;
            }
            ans++;
        }
    }
    for(int i = 0; i < q; i++) {
        prison[released[i]] = 0;
    }
    return ans;
}
long solve() {
    long ans = calcBridge();
    long tmp;
    while(next_permutation(released, released + q)) {
        tmp = calcBridge();
        if (ans > tmp) {
            ans = tmp;
        }
    }
    return ans;
}
int main(int argc, char** argv) {

    int tests;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &tests);
    for(int i = 1; i <= tests; i++) {
        input();
        printf("Case #%d: %d\n", i, solve());
    }
    return (EXIT_SUCCESS);
}

