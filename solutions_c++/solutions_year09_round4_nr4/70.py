#include <iostream>
#include <math.h>

using namespace std;

int x[64];
int y[64];
int r[64];

double sqr(int x)
{
    return x*x;
}

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n;
        cin >> n;
        for (int i=0; i<n; i++)
            cin >> x[i] >> y[i] >> r[i];

        double ans = 1e100;

        if (n == 1)
            ans = r[0];
        if (n == 2)
            ans = max(r[1], r[0]);

        if (n == 3)
            for (int i=0; i<3; i++)
                for (int j=0; j<i; j++)
                    for (int k=0; k<3; k++)
                        if (k != i && k != j)
                            ans = min(ans, max((double)r[k], (r[i] + r[j] + sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j]))) / 2));

        cout.setf(ios::fixed);
        cout.precision(9);                            
        cout << "Case #" << tt << ": " << ans << endl;
    }

    return 0;
}
