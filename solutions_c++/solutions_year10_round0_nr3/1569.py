#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
using namespace std;

struct Split {
    int front;
    int n;
    int next;
};

int main() {
    int T;
    int R,K,N;
    int g[1002];
    Split s[1002];

    cin >> T;
    for(int C=1;C<=T;C++) {
        scanf("%d %d %d", &R, &K, &N);

        for(int i=0;i<N;i++) {
            scanf("%d", g+i);
        }

        for(int i=0;i<N;i++) {
            s[i].front = i;
            s[i].n = g[i];
            s[i].next = i;

            int j=(i+1)%N;
            while(j!=i) {
                if(s[i].n + g[j] <= K) {
                    s[i].n += g[j];
                } else {
                    s[i].next = j;
                    break;
                }

                j = (j+1)%N;
            }
        }

        long long euro = 0;
        int pos = 0;
        while(R--) {
            euro += s[pos].n;
            pos = s[pos].next;
        }

        printf("Case #%d: %lld\n", C, euro);
    }

    return 0;
}
