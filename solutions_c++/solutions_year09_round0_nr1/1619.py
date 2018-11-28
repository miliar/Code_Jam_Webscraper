#include <cstdio>
#include <string>

using namespace std;

int L, D, N;
int d[5000][20];
int mask[20];
char s[102400];

int main()
{
    scanf("%d %d %d", &L, &D, &N);
    for (int i = 0; i < D; ++i) {
        scanf("%s", s);
        for (int j = 0; j < L; ++j)
            d[i][j] = 1 << (s[j] - 'a');    
    }
    for (int cas = 1; cas <= N; ++cas) {
        scanf("%s", s);
        int len = strlen(s);
        for (int i = 0, ind = 0; i < len; ++i, ++ind) {
            mask[ind] = 0;
            if (s[i] == '(') {
                while (s[++i] != ')') {
                    mask[ind] |= 1 << (s[i] - 'a');        
                }
            }
            else {
                mask[ind] = 1 << (s[i] - 'a');
            }
        }
        int ans = 0;
        for (int i = 0; i < D; ++i) {
            bool ok = true;
            for (int j = 0; j < L; ++j) {
                if ((d[i][j] & mask[j]) == 0) {
                    ok = false;
                    break;
                }
            }
            if (ok)
                ans++;
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}


