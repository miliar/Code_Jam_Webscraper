#include <assert.h>

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


#if 1

int main(int argc, char** argv) {
    int T = 0;
    freopen ("A-large-attempt1.in", "r", stdin);
    freopen ("A-large-attempt1.out", "w", stdout);
    fscanf(stdin, "%d", &T);

    for (int ncase=0; ncase<T; ncase++) {
        int N = 0, K = 0;
        fscanf(stdin, "%d %d", &N, &K);
        unsigned result = K % (1<<N);
        bool on = (K != 0) && ((result+1) == (1<<N));
        printf("Case #%d: %s\n", ncase+1, on ? "ON" : "OFF");

    }
}
#endif
