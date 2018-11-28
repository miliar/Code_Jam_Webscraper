#define maxn 40
#define maxl 107
#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;
int a, b, n;
char s[maxn][maxl], f[maxn][maxl], str[maxl];
char lst[maxl * maxn];

void solve(){
    int tail = 0;
    for (int i=0; i<n; i++){
        lst[tail++] = str[i];
//        lst[tail]=0; printf("fir i:%d tail:%d - %s\n", i, tail, lst);
        for (int j=0; j<a; j++) if (tail>1 && (lst[tail-1]==s[j][0]&&lst[tail-2]==s[j][1] || lst[tail-1]==s[j][1]&&lst[tail-2]==s[j][0])){
            lst[tail-2] = s[j][2];
            tail--;
            break;
        }
        for (int k=0; k<tail-1; k++) for (int j=0; j<b; j++){
            if (lst[k]==f[j][0] && lst[tail-1]==f[j][1] || lst[k]==f[j][1] && lst[tail-1]==f[j][0]) {
                tail = 0;
                break;
            }
        }
//        lst[tail]=0; printf("i:%d tail:%d - %s\n", i, tail, lst);
    }
    for (int i=0; i<tail; i++) if (i!=tail-1) printf("%c, ", lst[i]);
    else printf("%c]\n", lst[i]);
    if (tail==0) puts("]");
}

int main(){
    int test; scanf("%d", &test);
    for (int cas=1; cas<=test; cas++){
        scanf("%d", &a);
        for (int i=0; i<a; i++) scanf("%s", s[i]);
        scanf("%d", &b);
        for (int i=0; i<b; i++) scanf("%s", f[i]);
        scanf("%d%s", &n, str);
        printf("Case #%d: [", cas);
        solve();
    }
}
