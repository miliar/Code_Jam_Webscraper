#include <iostream>
#include <vector>
#include <cstdio>
using namespace std;

int main()
{
    int t, T;
    int A, B;
    vector<double> p;
    int i;
    double best;
    double current;

    cin >> T;
    for (t = 1; t <= T; t++)
    {
        cin >> A >> B;
        p.resize(A+1);
        best = 1000000000;
        p[0] = 1.0;
        for (i = 1; i <= A; i++)
        {
            cin >> p[i];
        }
        for (i = 1; i <= A; i++)
        {
            p[i] = p[i] * p[i-1];
        }

        for (i = 0; i <= A; i++)
        {
            current = p[A-i]*(2*i+B-A+1) + (1-p[A-i])*(2*i+2*B-A+2);
            if (current < best)
            {
                best = current;
            }
        }
        if (2 + B < best)
        {
            best = 2 + B;
        }
        printf("Case #%d: %.6lf\n", t, best);
    }

    return 0;
}

