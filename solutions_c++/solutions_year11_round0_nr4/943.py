#include <iostream>
#include <vector>

using namespace std;

long double fact(int x)
{
    long double res = 1.0;

    for (int i = 2; i <= x; i++)
        res *= i;

    return res;
}

int main()
{
    int t, tn = 1;

    cout.setf(ios::fixed);
    cin >> t;

    while (tn <= t)
    {
        int n;
        vector<int> inp;
        vector<bool> u;
        long double ans = 0.0;
        int t = 0, curr;

        cin >> n;
        inp.resize(n);
        u.assign(n, false);

        for (int i = 0; i < n; i++)
        {
            cin >> inp[i];
            inp[i]--;
        }

        for (int i = 0; i < n; i++)
        {
            if (u[i])
                continue;

            t = 1;
            u[i] = true;
            curr = inp[i];
            while (curr != i)
            {
                u[curr] = true;
                curr = inp[curr];
                t++;
            }
            ans += (t == 1 ? 0 : t);
        }

        cout << "Case #" << tn << ": " << ans << endl;
        tn++;
    }

    return 0;
}
