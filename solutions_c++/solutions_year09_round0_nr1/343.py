#include <cstdio>
#include <cstring>

using namespace std;

char s[5010][20];
bool f[20][26];
int l, d, n;

void init()
{
    for (int i = 0; i < d; ++i)
        scanf ("%s", s[i]);
}

void solve()
{
    char now[1000];
    
    for (int Case = 1; Case <= n; ++Case) {
        scanf ("%s", now);
        int pos = 0;
        memset (f, 0, sizeof(f));
        
        for (int k = 0; k < l; ++k) {
            if (now[pos] == '(') {
                for (++pos; now[pos] != ')'; ++pos) {
                    //printf ("%d %c\n", k, now[pos]);
                    f[k][now[pos] - 'a'] = 1;
                }
                ++pos;
            }
            else {
                //printf ("%d %c\n", k, now[pos]);
                f[k][now[pos++] - 'a'] = 1;
            }
            if (now[pos] == '\0')
                break;
        }      
            
        int ans = 0;
        for (int j = 0; j < d; ++j) {
            int flag = 1;
            for (int k = 0; k < l; ++k) {
                //printf ("Check: %d %c\n", k, s[j][k]);
                if (!f[k][s[j][k] - 'a']) {
                    flag = 0;
                    break;
                }
            }
            ans += flag;
        }
        printf ("Case #%d: %d\n", Case, ans);
    }
}

int main()
{
    //freopen ("F:/A-large.in", "r", stdin);
    //freopen ("A-large.out", "w", stdout);
    
    while (scanf ("%d%d%d", &l, &d, &n) != EOF) {
        init();
        solve();
    }
    
    //while (1);
    
    return 0;
}
