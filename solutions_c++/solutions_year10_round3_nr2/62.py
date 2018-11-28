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

int na, nb, nc;
long long A, B, C, a1, a2, b1, b2;

int main() {
    int cas;
    scanf("%d", &cas);
    for (int tt = 0; tt < cas; tt++) {
        scanf("%d%d%d", &na, &nb, &nc);


        int t = nb / na;
        if (t * na < nb) t++;

        long long p = 1;
        int q = 0;
        while (p * nc < t) {
            p = p * nc;
            q++;
        }
//        p = p * c;
//        q++;

        int r = 0;

        while (q > 0) {
            int mid = (q + 1) / 2;
            q = max(mid - 1, q - mid);
            r++;
        }



        printf("Case #%d: %d\n", tt + 1, r);

    }
}
