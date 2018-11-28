#include <stdio.h>
#include <set>
#include <stdlib.h>
#include <string>

using namespace std;


char ar[100][100];
int val[100],n;

int eval (int p) {
    val[p] = 0;
    for (int i=n-1; i>0; i--) {
        if (ar[p][i] != '0') {
           val[p] = i;
           break;
        }
    }
}

int solve() {
    scanf("%d\n",&n);
    for (int i=0; i<n; i++) {
        scanf("%s\n", ar[i]);
        eval(i);
    }

    int res = 0;
    for (int i=0; i<n-1; i++) {
        int minj = i;
        for (int j=i; j<n; j++) {
            if (val[j] <= i) {
               minj = j;
               break;
            }
        }
        for (int k=minj; k>i; k--) {
            swap(val[k],val[k-1]);
            res++;
        }
    }
    return res;
}

int main () {
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);

    int T;
    scanf("%d\n",&T);
    for (int i=1; i<=T; i++) {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
