#include <stdio.h>
#include <iostream>
#define INF 0x3f3f3f3f
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)

char str[1005], s[1005];
int ord[10];

int main() {
    FILE *fin = fopen("rle.in", "r"), *fout = fopen("rle.out", "w");
    int N; fscanf(fin, "%d", &N); REP(n, N) {
        int k; fscanf(fin, "%d", &k);
        fscanf(fin, "%s", str); int l = strlen(str);

        REP(i, k) ord[i] = i; 
        int best = INF;
        do {
            int x = 0; while(x < l) {
                REP(i, k) s[x+i] = str[x+ord[i]];
                x += k;
            }

            int res = 0; REP(i, l) if (s[i] != s[i+1]) res++;
            best <?= res;
        }
        while(next_permutation(ord, ord+k)) ;

        fprintf(fout, "Case #%d: %d\n", n+1, best);
    }
    return 0;
}
