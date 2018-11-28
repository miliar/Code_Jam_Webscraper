#include <stdio.h>
#include <string.h>
int c[30];
int a[200], cn;
int b[30][30];
int d[30][30];
char s[200];
void add(int x){
    int i;
    if (cn && b[a[cn - 1]][x] != -1){
        c[a[cn - 1]]--;
        cn--;
        add(b[a[cn]][x]);
        return;
    }
    for (i = 0; i < 30; i++){
        if (c[i] && d[i][x]){
            cn = 0;
            memset(c, 0, sizeof(c));
            return;
        }
    }
    a[cn++] = x;
    c[x]++;
}
int main(){
    int ri = 1, n, T, i;
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--){
        memset(c, 0, sizeof(c));
        memset(b, -1, sizeof(b));
        memset(d, 0, sizeof(d));
        cn = 0;
        scanf("%d", &n);
        while (n--){
            scanf("%s", s);
            b[s[0] - 'A'][s[1] - 'A'] = s[2] - 'A';
            b[s[1] - 'A'][s[0] - 'A'] = s[2] - 'A';
        }
        scanf("%d", &n);
        while (n--){
            scanf("%s", s);
            d[s[0] - 'A'][s[1] - 'A'] = 1;
            d[s[1] - 'A'][s[0] - 'A'] = 1;
        }
        scanf("%d%s", &n, s);
        for (i = 0; i < n; i++){
            add(s[i] - 'A');
        }
        printf("Case #%d: [", ri++);
        if (cn){
            printf("%c", a[0] + 'A');
        }
        for (i = 1; i < cn; i++){
            printf(", %c", a[i] + 'A');
        }
        printf("]\n");
    }
    return 0;
}
