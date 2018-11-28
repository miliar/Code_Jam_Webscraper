#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <string>

#include <set>

using namespace std;

#define REP(i,N) for (int i=0; i<(int)N; i++)
#define FOREACH(v,it) for(__typeof((v).begin()) it=(v).begin();it!=(v).end();it++)



int w[600][600];
long long X[600][600], Y[600][600], W[600][600];

long long getX (int i, int j)
{
    if (i < 0 || j < 0) return 0;
    return X[i][j];
}

long long getY (int i, int j)
{
    if (i < 0 || j < 0) return 0;
    return Y[i][j];
}

long long getW (int i, int j)
{
    if (i < 0 || j < 0) return 0;
    return W[i][j];
}

int solve ()
{
    int R, C, D;
    cin >> R >> C >> D;
    REP (i, R)
    {
        string s;
        cin >> s;
        REP (j, C)
        {
            w[i][j] = s[j] - '0';
            w[i][j] += D;

            X[i][j] = w[i][j] * i;
            Y[i][j] = w[i][j] * j;
            W[i][j] = w[i][j];
            if (j > 0)
            {
                X[i][j] += X[i][j-1];
                Y[i][j] += Y[i][j-1];
                W[i][j] += W[i][j-1];
            }
            if (i > 0)
            {
                X[i][j] += X[i-1][j];
                Y[i][j] += Y[i-1][j];
                W[i][j] += W[i-1][j];
            }
            if (i*j > 0)
            {
                X[i][j] -= X[i-1][j-1];
                Y[i][j] -= Y[i-1][j-1];
                W[i][j] -= W[i-1][j-1];
            }
       //     cout << X[i][j] << " ";
        }
   //     cout << endl;
    }
    int ans = 0;
    REP (r, R) REP (c, C) REP (k, 1 + min (R-r, C-c)) if (k >= 3)
    {
        int r1 = r + k, c1 = c + k;
        long long X0 = getX(r1-1, c1-1) + getX(r-1, c-1) - getX(r1-1, c-1) - getX(r-1, c1-1)
                - w[r][c] * r - w[r][c1-1] * r - w[r1-1][c] * (r1-1) - w[r1-1][c1-1] * (r1-1);
        long long Y0 = getY(r1-1, c1-1) + getY(r-1, c-1) - getY(r1-1, c-1) - getY(r-1, c1-1)
                - w[r][c] * c - w[r][c1-1] * (c1-1) - w[r1-1][c] * c - w[r1-1][c1-1] * (c1-1);
        long long W0 = getW(r1-1, c1-1) + getW(r-1, c-1) - getW(r1-1, c-1) - getW(r-1, c1-1)
                - w[r][c] - w[r][c1-1] - w[r1-1][c] - w[r1-1][c1-1];
        if (X0 * 2 == W0 * (r + r1 - 1) && Y0 * 2 == W0 * (c + c1 - 1))
        {
            ans = max (ans, k);
        }

        if (r == 1 && c == 1 && k == 5)
        {
       //     cout << r1 << " " << c1 << " " << X0 << " " << Y0 << " " << W0 << endl;
      //      cout << getW(r1-1, c1-1) << " " << getW(r-1, c-1)  << " " << getW(r1-1, c)  << endl;
        }
    }
    return ans;
}

int main ()
{
    freopen ("B-large.in", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T;
    cin >> T;
    REP (cas, T)
    {
        int ans = solve();
        if (ans > 0)
            cout << "Case #" << cas+1 << ": " << ans << endl;
        else
            cout << "Case #" << cas+1 << ": " << "IMPOSSIBLE" << endl;
    }
    return 0;
}
