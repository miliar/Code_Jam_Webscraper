#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t, pd, pg;
    long long int n;
    int temp = 100;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        cin >> n >> pd >> pg;

        if ((pg == 100 && pd != 100) || (pg == 0 && pd != 0) || (pd == 0 && pg == 100))
        {
            cout << "Case #" << i + 1 << ": Broken" << endl;
            continue;
        }

        if (pd == 0)
        {
            cout << "Case #" << i + 1 << ": Possible" << endl;
            continue;
        }

        temp = 100;
        while (pd % 2 == 0 && temp % 2 == 0)
        {
            temp /= 2;
            pd /= 2;
        }
        while (pd % 5 == 0 && temp % 5 == 0)
        {
            temp /= 5;
            pd /= 5;
        }

        if (temp <= n)
            cout << "Case #" << i + 1 << ": Possible" << endl;
        else
            cout << "Case #" << i + 1 << ": Broken" << endl;
    }

    return 0;
}
