#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int N, L, H;
int freq[105];

bool poss(int f) {
    bool p = true;
    for (int i = 0 ; p && i < N ; i++) {
        if(freq[i] > f) {
            if ( freq[i] % f != 0) p = false;
        }
        else {
            if ( f % freq[i] != 0) p = false;
        }
    }
    return p;
}

void work() {
    
    scanf("%d %d %d\n", &N, &L, &H);
    for (int i = 0; i < N ; i++) {
        scanf("%d", &freq[i]);
    }

    for (int f = L ; f <= H ; f++) {
        if (poss(f)) {
            printf("%d\n", f);
            return;
        }
    }
    
    printf("NO\n");
}

/////////////////////////////////////////////////////////////

int main() {
    int T;
    scanf("%d\n", &T);
    for (int tt = 1 ; tt <= T ; tt++) {
        printf("Case #%d: ", tt);
        work();
    }
}
