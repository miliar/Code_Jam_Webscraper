#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<functional>
#include<stdio.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(n);i++)
#define init(a,v) memset(a,v,sizeof(a))
#define gi(t) scanf("%d",&(t))
#define sz 257

int INF = 1000000000;
int d, in, m, n;
int input[105]; 
int dp[105][sz]; 


int main ()
{
    int test; gi(test);
    forn(numb,test)
    {
        forn(i,106) forn(j,sz) dp[i][j] = INF;
        gi(d); gi(in); gi(m); gi(n);
        forn(i,n) gi(input[i]); int ans; 
        if (m != 0)
        {
        dp[0][256] = 0;
        forn(i,256) dp[0][i] = in;         
        for (int i = 1; i <= n; i++)
        {
            int j = input[i-1]; 
            forn(k,256)
            {
                int diff = j-k; if (diff < 0) diff = -diff;
                if (diff) diff--; diff /= m;
                dp[i][j] = min(dp[i][j], dp[i-1][k] + diff*in); 
            }
            dp[i][j] = min(dp[i][j], dp[i-1][256]);
            for (int j = 0; j <= 256; j++)
            {
                if (j == 256) dp[i][j] = d*i;
                else if (j == input[i-1]);
                else
                {
                    int diffe = input[i-1] - j; if (diffe < 0) diffe = 0-diffe;
                    dp[i][j] = min(diffe + (i-1)*d, in + i*d);
                    forn(k,256)
                    {
                        if (j != k)
                        {
                            int diff = j-k; if (diff < 0) diff = -diff;
                            diff--; diff /= m; diff++;
                            dp[i][j] = min(dp[i][j], dp[i-1][k] + diff*in + d);
                        }
                        else dp[i][j] = min(dp[i][j], dp[i-1][k] + d);
                    }
                    forn(k,256)
                    {
                        int diff = j-k; if (diff < 0) diff = -diff;
                        if (diff) diff--; diff /= m;
                        int more = input[i-1]-j; if (more < 0) more = -more; 
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + diff*in + more);
                    }
                }
            }
        }
        ans = INF;
        forn(i,257) ans = min(ans, dp[n][i]);
//        forn(i,n+1) { forn(j,10)  cout << dp[i][j] << ' '; cout << endl;   }
//        printf("Case #%d: ", numb+1);
        }
        else
        {
            ans = d*n;
            forn(j,256)
            {
                int current = 0;
                forn(i,n)
                {
                    int diff = j - input[i]; if (diff < 0) diff = 0-diff; 
                    current += min(diff, d); 
                }
                forn(j,256) ans = min(ans, current);
            }
        }
//        cout << d << ' ' << in << ' ' << m << ' ' << n << endl;
  //      forn(i,n) cout << input[i] << ' '; cout << endl; 
        cout << "Case #" << numb+1 << ": " << ans << endl;
    }
    return 0;
}