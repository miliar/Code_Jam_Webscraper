#include <iostream>
using namespace std;

string S[101];
int query[1001];

int Sn, Qn;

int Find(string s)
{
    int st = 1, ed = Sn, md;
    while (st <= ed)
    {
        md = (st+ed) / 2;
        if (s==S[md]) return md;
        if (s < S[md]) ed = md - 1; else
        st = md + 1;
    }
    return 0;
}

int dp[1001][101];

int DP()
{
    int i, j, k;
    memset(dp, 0x30, sizeof dp);
    for (j = 1; j<=Sn; j++) 
    {
        if (query[Qn]!=j)
        {
            dp[Qn][j] = 0;
        }
    }
    
    for (i = Qn-1; i>=0; i--)
    {
        for (j = 1; j<=Sn; j++)
        {
            if (query[i]==j) continue;
            if (query[i+1]!=j)
            {
                dp[i][j] = dp[i+1][j];
            }else
            {
                for (k = 1; k<=Sn; k++)
                    if (k!=j)
                    {
                        dp[i][j] <?= dp[i+1][k] + 1;
                    }
            }
        }
    }
    
    int ret = 100000000;
    for (int j = 1; j<=Sn; j++) ret <?= dp[0][j];
    return ret;
}

int Solve()
{
    char buf[200];
    scanf("%d\n", &Sn);
    for (int i = 1; i<=Sn; i++)
    {
        gets(buf);
        S[i] = string(buf);
//        cout << S[i] << endl;
    }
    sort(S + 1, S + Sn + 1);

    scanf("%d\n", &Qn);    
    for (int i = 1; i<=Qn; i++)
    {
        gets(buf);
        query[i] = Find(string(buf));
//        cout << query[i] << endl;
    }
    
    return DP();
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    int task, cn;
    cin >> task;
    for (cn = 1; cn<=task; cn++)
    {
        cout << "Case #" << cn << ": " << Solve() << endl;
    }
}
