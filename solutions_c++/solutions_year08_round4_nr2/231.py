#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    for (int cas = 1; cas <= n; cas++) {
        int N, M, A;
        scanf("%d %d %d", &N, &M, &A);
        for (int i1 = 0; i1 <= N; i1++) {
            for (int j1 = 0; j1 <= M; j1++) {
                for (int i2 = 0; i2 <= N; i2++) {
                    for (int j2 = 0; j2 <= M; j2++) {
                        long long int ar = (long long)(i1 * j2) - (long long)(i2 * j1);
                        ar = abs(ar);
                        if (ar == A) {
                            printf("Case #%d: %d %d %d %d %d %d\n", cas, 0, 0, i1, j1, i2, j2);
                            goto done;
                        }
                    }
                }
            }
        }
        printf("Case #%d: IMPOSSIBLE\n", cas);
done:
        N = N;
    }
}
