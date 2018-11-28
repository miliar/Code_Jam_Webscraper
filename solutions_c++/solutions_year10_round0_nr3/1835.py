#include <stdio.h>
#include <memory.h>
#include <iostream>

using namespace std;

int n, R, k;
int g[1000];
long long res;

int sj, cnt;
long long amt;
int q[1001], s[1000];
long long c[1001];


void input() {
    scanf("%d%d%d", &R, &k, &n);
    for (int i=0; i<n; i++) scanf("%d", &g[i]);
}

void find_cycle() {
    int i, j, acc;
    int u;


    //
    memset(s, -1, sizeof(s));
    i = 0; q[0] = 0; c[0] = 0; s[0] = 0;   

    //
    j = 0;
    while (true) {
        //
        i++;
        
        // 
        acc = 0; u = 0;
        while (true) {
            if (u==n || acc+g[j]>k) break;
            u++;
            acc += g[j];
            j = (j+1) % n;
        }

        //
        //printf("i=%d  j=%d  s[j]=%d\n", i, j, s[j]);
        q[i] = j; c[i] = c[i-1]+acc;
        if (s[j] != -1) break;
        s[j] = i;
    }

    //
    cnt = i - s[j];
    amt = c[i] - c[s[j]];
    sj  = s[j];
    //printf("sj=%d    cnt=%d    amt=%lld\n", sj, cnt, amt);
}

void process() {
    //
    find_cycle();

    //
    if (R <= sj) {
        res = c[R];
    } else {
        res = amt*((R-sj)/cnt) + c[sj+(R-sj)%cnt];
    }
}



int main() {
    int numtest;

    scanf("%d", &numtest);
    for (int i=1; i<=numtest; i++) {
        input();
        process();
        printf("Case #%d: %lld\n", i, res);
    }

    return 0;
}
