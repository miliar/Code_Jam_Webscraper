#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;

int a[512][512];
int s[512] = {0};
int c[512][512];

int C(int n, int m)
{
    if (c[n][m] != -1)
        return c[n][m];
    else if (n < m)
        return c[n][m] = 0;
    else if (m == 0 || n == m)
        return c[n][m] = 1;
    else
    {
        int s = 1;
        for (int i = 1; i <= m; ++i)
        {
            s *= (n - i + 1);
            s /= i;
            s %= 100003;
        }
        return c[n][m] = s;
    }
}

void main()
{
    ifstream fin("C-small.in");
    ofstream fout("A.out");
    int T;
    fin >> T;
    memset(a, 0, sizeof(a));
    memset(s, 0, sizeof(s));
    memset(c, 0xFF, sizeof(c));
    a[2][1] = 1;
    a[3][1] = 1;
    a[3][2] = 1;
    s[2] = 1;
    s[3] = 2;
    for (int i = 4; i <= 500; ++i)
    {
        a[i][1] = 1;
        a[i][2] = 1;
        for (int j = 3; j < i; ++j)
        {
            a[i][j] = 0;
            for (int k = 1; k < j; ++k)
            {
                a[i][j] += ((long long)a[j][k]) * C(i - j - 1, j - k - 1) % 100003;
                a[i][j] %= 100003;
            }
        }
        s[i] = 0;
        for (int j = 1; j < i; ++j)
        {
            s[i] += a[i][j];
            s[i] %= 100003;
        }
    }
    for (int tt = 1; tt <= T; ++tt)
    {
        fin >> n;
        fout << "Case #" << tt << ": " << s[n] << endl;
    }
    fout.close();
    fin.close();
}
