#include <iostream>
#include <string>
using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int N;
    char in[510];
    sscanf(gets(in), "%d", &N);
    for(int t=1; t<=N; t++)
    {
        cout << "Case #" << t << ": ";
        gets(in);
        string s = in;
        
        //welcome to code jam
        //1234567890123456789
        int dp[19][500];
        memset(dp, 0, sizeof(dp));
        string w = "welcome to code jam";
        
        for(int i=18; i>=0; i--) for(int j=s.length()-1; j>=0; j--)
        {
            if(i == 18)
            {
                if(w[i] == s[j])
                {
                    if(j == s.length()-1) dp[i][j] = 1;
                    else dp[i][j] = dp[i][j+1] + 1;
                }
                else
                {
                    if(j == s.length()-1) dp[i][j] = 0;
                    else dp[i][j] = dp[i][j+1];
                }
            }
            else
            {
                if(j == s.length()-1) dp[i][j] = 0;
                else
                {
                    if(w[i] == s[j]) dp[i][j] = dp[i][j+1] + dp[i+1][j+1];
                    else dp[i][j] = dp[i][j+1];
                }
            }
        }
        
        //for(int i=18; i>=0; i--, puts("")) for(int j=0; j<s.length(); j++) cout << dp[i][j];
        printf("%04d\n", dp[0][0]);
    }
}
