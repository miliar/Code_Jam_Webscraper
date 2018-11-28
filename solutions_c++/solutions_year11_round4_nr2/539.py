#include <iostream>
#include <string>
#include <vector>

using namespace std;

const long double EPS = 1e-12;

struct go
{
    long double x, y;
    go()
    {
        x = y = 0.0;
    }
    go(const long double &a, const long double &b)
    {
        x = a;
        y = b;
    }

    go operator +(const go &b) const
    {
        return go(x + b.x, y + b.y);
    }
    go operator -(const go &b) const
    {
        return go(x - b.x, y - b.y);
    }
    go operator *(const long double k) const
    {
        return go(x * k, y * k);
    }
};

int main()
{
    int t, tn = 1;

    cin >> t;

    while (tn <= t)
    {
        int r, c, d;
        bool nf = true;
        vector<string> inp;
        vector<vector<pair<go, long long> > > dp;

        cin >> r >> c >> d;

        inp.resize(r);
        dp.assign(r, vector<pair<go, long long> >(c));
        for (int i = 0; i < r; i++)
            cin >> inp[i];

        for (int k = min(r, c); nf && k >= 3; k--)
            for (int i = 0; nf && i < r - k + 1; i++)
                for (int j = 0; nf && j < c - k + 1; j++)
                {
                    go c = go();
                    double m = (k - 1) / 2.0;
                    long long tw = 0;
                    if (i == 0 && j == 0)
                    {
                        for (int a = 0; a < k; a++)
                            for (int b = 0; b < k; b++)
                            {
                                if (a == 0 && b == 0)
                                    continue;
                                if (a == 0 && b == k - 1)
                                    continue;
                                if (a == k - 1 && b == 0)
                                    continue;
                                if (a == k - 1 && b == k - 1)
                                    continue;

                                tw += inp[i + a][j + b] - '0' + d;
                                c = c + (go(a - m, b - m) * (inp[i + a][j + b] - '0' + d));
                            }
                    }
                    else
                        if (i == 0)
                        {
                            c = dp[i][j - 1].first;
                            tw = dp[i][j - 1].second;

                            for (int a = 1; a < k - 1; a++)
                            {
                                c = c - (go(a - m, -m) * (inp[i + a][j - 1] - '0' + d));
                                tw -= inp[i + a][j - 1] - '0' + d;
                            }

                            c = c + (go(-m, m) * (inp[i][j + k - 2] - '0' + d));
                            tw += inp[i][j + k - 2] - '0' + d;
                            c = c + (go(m, m) * (inp[i + k - 1][j + k - 2] - '0' + d));
                            tw += inp[i + k - 1][j + k - 2] - '0' + d;

                            c = c + (go(0, -1) * tw);

                            c = c - (go(-m, -m) * (inp[i][j] - '0' + d));
                            tw -= inp[i][j] - '0' + d;
                            c = c - (go(m, -m) * (inp[i + k - 1][j] - '0' + d));
                            tw -= inp[i + k - 1][j] - '0' + d;

                            for (int a = 1; a < k - 1; a++)
                            {
                                c = c + (go(a - m, m) * (inp[i + a][j + k - 1] - '0' + d));
                                tw += inp[i + a][j + k - 1] - '0' + d;
                            }
                        }
                        else
                        {
                            c = dp[i - 1][j].first;
                            tw = dp[i - 1][j].second;

                            for (int b = 1; b < k - 1; b++)
                            {
                                c = c - (go(-m, b - m) * (inp[i - 1][j + b] - '0' + d));
                                tw -= inp[i - 1][j + b] - '0' + d;
                            }

                            c = c + (go(m, -m) * (inp[i + k - 2][j] - '0' + d));
                            tw += inp[i + k - 2][j] - '0' + d;
                            c = c + (go(m, m) * (inp[i + k - 2][j + k - 1] - '0' + d));
                            tw += inp[i + k - 2][j + k - 1] - '0' + d;

                            c = c + (go(-1, 0) * tw);

                            c = c - (go(-m, -m) * (inp[i][j] - '0' + d));
                            tw -= inp[i][j] - '0' + d;
                            c = c - (go(-m, m) * (inp[i][j + k - 1] - '0' + d));
                            tw -= inp[i][j + k - 1] - '0' + d;

                            for (int b = 1; b < k - 1; b++)
                            {
                                c = c + (go(m, b - m) * (inp[i + k - 1][j + b] - '0' + d));
                                tw += inp[i + k - 1][j + b] - '0' + d;
                            }
                        }


                    dp[i][j].first = c;
                    dp[i][j].second = tw;

                    if (fabs(c.x) < EPS && fabs(c.y) < EPS)
                    {
                        cout << "Case #" << tn << ": " << k << endl;
                        nf = false;
                    }
                }
        if (nf)
            cout << "Case #" << tn << ": IMPOSSIBLE\n";

        tn++;
    }

    return 0;
}
