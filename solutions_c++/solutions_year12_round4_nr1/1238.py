#include <iostream>
using namespace std;

int DP[10003][10003];
int D[10003];
int L[10003];
int S, N;
int I[10003][10003];

int f(int k1, int k2)
{
    k2++;
    int res = 0;
    while (k2 > 0)
    {
        res += I[k1][k2];
        k2 -= k2&(-k2);
    }
    return res;
}

void add(int k1, int k2)
{
    //cout << "added " << k1 << " " << k2 << endl;
    k2++;
    while (k2 <= N + 1)
    {
        I[k1][k2]++;
        k2 += k2&(-k2);
    }
    //cout << I[1][4] << endl;
}

bool dp(int k1, int k2)
{
    int len = min(D[k2] - D[k1], L[k2]);
    if (D[k2] + len >= S) return 1;

    int& res = DP[k1][k2];
    if (res != -1) return res;

    res = 0;
    int l = k1, r = N + 1;
    while (l + 1 != r)
    {
        int m = (l + r)/2;
        if (D[k2] + len >= D[m]) l = m;
        else r = m;
    }

    for (int i = l; i > k2; i--)
    {
        res |= dp(k2, i);
    }
    return res;
}

bool solve()
{
    memset(DP, -1, sizeof(DP));
    memset(I, 0, sizeof(I));
    cin >> N;
    D[0] = 0;
    for (int i = 1; i <= N; i++) cin >> D[i] >> L[i];
    cin >> S;

    for (int k1 = N; k1 >= 0; k1--)
     for (int k2 = N; k2 > k1; k2--)
     {
          DP[k1][k2] = 0;

          int len = min(D[k2] - D[k1], L[k2]);
          if (D[k2] + len >= S) DP[k1][k2] = 1, add(k1, k2);
          else
          {
               int l = k2, r = N + 1;
               while (l + 1 != r)
               {
                   int m = (l + r)/2;
                   if (D[k2] + len >= D[m]) l = m;
                   else r = m;
               }
               //if (k1 == 0 && k2 == 1) cout << k2 << " " << l << " " << f(k2, l) << endl;
               DP[k1][k2] = (f(k2, l) - f(k2, k2) > 0) ? 1 : 0;
               if (DP[k1][k2]) add(k1, k2);
          }
     }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        solve();
        for (int i1 = 0; i1 <= N; i1++)
        {

            for (int j = 0; j <= N; j++)
             {
           //      cout << DP[i1][j];
             }
           //  cout << endl;
        }
        cout << "Case #" << i + 1 << ": " << (DP[0][1]?"YES":"NO") << endl;
    }
}
