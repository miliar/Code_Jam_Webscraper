#include <iostream>
#include <algorithm>
#include <math.h>
#define eps 1e-7
using namespace std;

bool eq(double a, double b)
{
    return fabs(a - b) < eps;
}

double calc(int index, int* S, int X, int N)
{
    double s[200];

    double l = 0, r = 1;
    for (int qq = 0; qq < 100; qq++)
    {
        for (int i = 0; i < N; i++) s[i] = S[i];

        double m = (l + r)/2;

        double x = X;

        x -= m*X;
        s[index] += m*X;
        double cur = s[index];
        sort(s, s + N);

        for (int j = 0; s[j] < cur - eps; j++)
        {
            double needed = cur - s[j];
            x -= needed;
        }

        //cout << x << endl;
        if (x > eps) l = m;
        else r = m;
    }
    return l*100;
}

void solve()
{
    int N;
    cin >> N;
    int S[200];

    int X = 0;
    for (int i = 0; i < N; i++)
    {
        cin >> S[i];
        X += S[i];
    }

    for (int i = 0; i < N; i++)
    {
        if (i != 0) cout << " ";
        cout << calc(i, S, X, N);
    }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}
