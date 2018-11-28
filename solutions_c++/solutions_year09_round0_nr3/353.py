#include <cstdio>
#include <cstring>

using namespace std;

const char c[] = "welcome to code jam";
const int mod = 10000;

int main()
{
    int t, dp[20], Case = 1;
    char s[520];
    
    //freopen ("F:\C-large.in", "r", stdin);
    //freopen ("C-large.out", "w", stdout);
    scanf ("%d", &t);
    gets(s);
    
    while (t--) {
        gets(s);
        //printf ("--%s\n", s);
        memset (dp, 0, sizeof(dp));
        for (int i = 0; s[i]; ++i) {
            if (s[i] == ' ') {
                dp[7] = (dp[7] + dp[6]) % mod;
                dp[10] = (dp[10] + dp[9]) % mod;
                dp[15] = (dp[15] + dp[14]) % mod;
            }
            else if (s[i] == 'w')
                dp[0] = (dp[0] + 1) % mod;
            else if (s[i] == 'e') {
                dp[1] = (dp[1] + dp[0]) % mod;
                dp[6] = (dp[6] + dp[5]) % mod;
                dp[14] = (dp[14] + dp[13]) % mod;
            }
            else if (s[i] == 'l')
                dp[2] = (dp[2]+ dp[1]) % mod;
            else if (s[i] == 'c') {
                dp[3] = (dp[3] + dp[2]) % mod;
                dp[11] = (dp[11] + dp[10]) % mod;
            }
            else if (s[i] == 'o') {
                dp[4] = (dp[4] + dp[3]) % mod;
                dp[9] = (dp[9] + dp[8]) % mod;
                dp[12] = (dp[12] + dp[11]) % mod;
            }
            else if (s[i] == 'm') {
                dp[5] = (dp[5] + dp[4]) % mod;
                dp[18] = (dp[18] + dp[17]) % mod;
            }
            else if (s[i] == 't')
                dp[8] = (dp[8] + dp[7]) % mod;
            else if (s[i] == 'd')
                dp[13] = (dp[13] + dp[12]) % mod;
            else if (s[i] == 'j')
                dp[16] = (dp[16] + dp[15]) % mod;
            else if (s[i] == 'a')
                dp[17] = (dp[17] + dp[16]) % mod;
            /* for (int j = 0; j < 19; ++j)
                printf ("%d ", dp[j]);
            printf ("%c\n", s[i]); */
        }
        printf ("Case #%d: %04d\n", Case++, dp[18] % mod);    
    }
    
    //while (1);
    
    return 0;
}
