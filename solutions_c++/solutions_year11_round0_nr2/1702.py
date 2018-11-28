#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
char cc[30][30], dd[30][30];
char ans[110];
int la;
int c, d, n;
string nn;
int main() {
    int cas;
    freopen("a.in", "r", stdin);
    freopen("b.txt", "w", stdout);
    scanf("%d" ,&cas);
    for (int ccas = 1; ccas <= cas; ++ccas) {
        memset(cc, 0, sizeof(cc));
        memset(dd, 0, sizeof(dd));
        la = 0;
        string s;
        scanf("%d", &c);
        for (int j = 0; j < c; ++j) { cin >> s;  cc[s[0]-'A'+1][s[1] - 'A'+1] = s[2] - 'A'+1;  cc[s[1] - 'A'+1][s[0]-'A'+1] = s[2] - 'A'+1;  }
        scanf("%d", &d);
        for (int j = 0; j < d; ++j) { cin >> s; dd[s[0]-'A'+1][s[1] - 'A'+1] = 1;dd[s[1] - 'A'+1][s[0]-'A'+1]= 1; }
        scanf("%d", &n);
        cin >> nn;
        for (int j = 0; j < n; ++j) {
            ans[la++] = nn[j];
            if (la - 2 >= 0 && cc[ ans[la-1] - 'A' + 1][ans[la-2] - 'A' + 1] != 0) { la--; ans[la-1] = cc[ ans[la] - 'A' + 1][ans[la-1] - 'A' + 1] + 'A' - 1; } else {
                int flag  = 0;
                 for (int k = 0; k < la - 1; ++k) if (dd[ans[k] - 'A' + 1][ans[la-1] - 'A' + 1]) {
                     flag = 1;
                     break;
                 }    
                 if (flag) la = 0;
            }    
        }
   
        printf("Case #%d: [", ccas);
        if (la == 0) puts("]"); else {
            for (int j = 0; j < la-1; ++j) printf("%c, ", ans[j]);
            printf("%c]\n", ans[la-1]);
        }    

    }
    return 0;
}    
