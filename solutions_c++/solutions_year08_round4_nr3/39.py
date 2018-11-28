#include <iostream>
#include <iomanip>

using namespace std;

struct ship
{
    double x, y, z;
    double p;
};

int N;
ship s[2000];

void inp()
{
    cin >> N;
    for (int i=0; i < N; i++)
        cin >> s[i].x >> s[i].y >> s[i].z >> s[i].p;
}

double calc_d(int a, int b, int c, double x, double y, double z)
{
    return -a*x - b*y - c*z;
}

bool can(int A, int B, int C, double P)
{
    double dmin = -1E+100;
    double dmax = +1E+100;

    for (int i=0; i < N; i++)
    {
        double d1 = calc_d(A, B, C, s[i].x + P*s[i].p, s[i].y, s[i].z);
        double d2 = calc_d(A, B, C, s[i].x - P*s[i].p, s[i].y, s[i].z);

        if (d1 > d2)
            swap(d1, d2);

        dmin = max(dmin, d1);
        dmax = min(dmax, d2);
    }

    return dmin <= dmax;
}

bool can(double P)
{
    for (int A=-1; A <= 1; A++)
        for (int B=-1; B <= 1; B++)
            for (int C=-1; C <= 1; C++)
                if (abs(A) + abs(B) + abs(C) == 3 && !can(A, B, C, P))
                    return false;

    return true;
}

double solve()
{
    double a = 0;
    double b = 1E+10;

    while (b-a > 1E-8)
    {
        double c = (a+b)/2;
        if (can(c))
            b = c;
        else
            a = c;
    }

    return (a+b)/2;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    int T;
    cin >> T;
    for (int i=1; i <= T; i++)
    {
        inp();
        cout << "Case #" << i << ": " << setprecision(9) << solve() << endl;
    }

    return 0;
}
