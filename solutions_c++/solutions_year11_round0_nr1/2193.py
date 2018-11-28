#include <iostream>
#include <vector>

using namespace std;

vector<int> a;
vector<int> b;

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        cout << "Case #" << tt << ": ";

        int n;
        cin >> n;

        a.clear();
        b.clear();

        for (int i=0; i<n; i++)
        {
            char c;
            int x;
            cin >> c >> x;
            if (c == 'O')
            {
                a.push_back(x);
                b.push_back(-1);
            }
            else
            {
                a.push_back(-1);
                b.push_back(x);
            }
        }

        for (int i=n-2; i>=0; i--)
        {
            if (a[i] < 0)
                a[i] = -abs(a[i+1]);
            if (b[i] < 0)
                b[i] = -abs(b[i+1]);
        }

        int x = 0, y = 0;
        int ans = 0;
        bool fa = false;
        bool fb = false;

        for (int i=0; i < n; ans++)
        {
            if (x < abs(a[i]))
                x++;
            if (x > abs(a[i]))
                x--;

            if (y < abs(b[i]))
                y++;
            if (y > abs(b[i]))
                y--;

            if (x == a[i] && fa || y == b[i] && fb)
            {
                fa = false;
                fb = false;
                i++;
            }

            if (abs(a[i]) == x)
                fa = true;

            if (abs(b[i]) == y)
                fb = true;
        }

        cout << ans-1 << endl;
    }

    return 0;
}
