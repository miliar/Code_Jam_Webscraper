#include <cstdio>
#include <iostream>
#include <queue>
#include <string>

using namespace std;

int C, D, N;

string Ci[38];
string Di[30];
string Ni;
string final;

char CC[256][256];
char DD[256][256];

void solve() {
    
    char elem[200];
    int  len = 0;
    for (int i=0; i<N; i++) {
        elem[len++] = Ni[i];
        
        if (len >= 2) {
        
            char c1 = elem[len-2];
            char c2 = elem[len-1];
            
            if (CC[c1][c2] != 0) {
                elem[len-2] = CC[c1][c2];
                len --;
            } else {
                int ll=len;
                for (int i=0; i<len-1; i++) {
                    if (DD[elem[i]][c2]) {
                        ll = i;
                        break;
                    }
                }
                if (ll != len)
                    len = 0;
            }
            
        }
    }
    putchar('[');
    for (int i=0; i<len; i++) {
        putchar(elem[i]);
        if (i != len-1) {
            putchar(',');
            putchar(' ');
        }
    }
    putchar(']');
    putchar(10);
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);
    int T = 1, cas;
    scanf("%d", &cas);
    while (cas --) {
        
        memset(CC, 0, sizeof CC);
        memset(DD, 0, sizeof DD);
        
        cin >> C;
        for (int i=0; i<C; i++) {
            cin >> Ci[i];
            CC[Ci[i][0]][Ci[i][1]] = Ci[i][2];
            CC[Ci[i][1]][Ci[i][0]] = Ci[i][2];
        }
        cin >> D;
        for (int i=0; i<D; i++) {
            cin >> Di[i];
            DD[Di[i][0]][Di[i][1]] = 1;
            DD[Di[i][1]][Di[i][0]] = 1;
        }
        cin >> N;
        cin >> Ni;
        printf("Case #%d: ", T ++);
        solve();
    }
    return 0;
}
