#include <cstdio>
#include <iostream>
using namespace std;

const int MAX_N = 200;

int n, T;
char d[] = "yhesocvxduiglbkrztnwjpfmaq";
char b[MAX_N];

void solve() {
//    scanf("%s", &b);
    gets(b);
    for (int i = 0; b[i]; ++i)
        if (b[i] != ' ')
            b[i] = d[b[i] - 'a'];
    printf("%s\n", b);
    
    
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    scanf("%d\n", &T);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}
