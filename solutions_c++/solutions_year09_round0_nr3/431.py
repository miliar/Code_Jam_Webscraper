#include <iostream>
using namespace std;

char s[1000];
char a[30] = "welcome to code jam";

int f[1000][30];

int T;

int main() {
    scanf("%d\n", &T);
    for (int ca = 0; ca < T; ++ca) {
        printf("Case #%d: ", ca + 1);
        gets(s);
        
        int ns = strlen(s);
        int na = strlen(a);
        memset(f, 0, sizeof(f));
        for (int i = 0; i < ns; ++i) {
            if (s[i] == a[0]) {
                f[i][0] = 1;
            }
            for (int j = 1; j < na; ++j) {
                if (s[i] == a[j]) {
                    for (int k = 0; k < i; ++k) {
                        f[i][j] = (f[i][j] + f[k][j - 1]) % 10000;
                    }
                }
            }
        }
        
        int ans = 0;
        for (int i = 0; i < ns; ++i) {
            ans = (ans + f[i][na - 1]) % 10000;
        }
        
        printf("%04d\n", ans);
    }
    return 0;
}
