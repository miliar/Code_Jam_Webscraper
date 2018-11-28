#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n;
int howmany[10002];
int mqueue[1000];
int qstart, qend;

int main() {
    int T, TT;
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        int i, j;
        int c;
        for (i = 0; i <= 10001; i++)
            howmany[i] = 0;
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%d", &c);
            howmany[c]++;
        }
        qstart = 0;
        qend = 0;
        int ans = 9999999;
        for (i = 0; i <= 10001; i++) {
            if (qend - qstart > howmany[i]) {
                if (i - mqueue[qend - howmany[i]-1] < ans)
                    ans = i - mqueue[qend - howmany[i]-1];
                qstart = qend - howmany[i];
            } else {
                for (j = 0; j < howmany[i] - (qend - qstart); j++)
                    mqueue[qend+j] = i;
                qend+=j;
            }
        }
        printf("Case #%d: %d\n", T, ans == 9999999? 0: ans);
        
    }
}
