#include <iostream>

using namespace std;

char a[256][256];
char b[256][256];

int main()
{
    int t;
    cin >> t;

    for (int tt=1; tt<=t; tt++)
    {
        cout << "Case #" << tt << ": ";

        memset(a, 0, sizeof(a));
        memset(b, 0, sizeof(b));

        char s[128];
        char w[128];

        int n;
        cin >> n;

        for (int i=0; i<n; i++)
        {
            cin >> s;
            a[s[0]][s[1]] = s[2];
            a[s[1]][s[0]] = s[2];
        }

        cin >> n;

        for (int i=0; i<n; i++)
        {
            cin >> s;
            b[s[0]][s[1]] = 1;
            b[s[1]][s[0]] = 1;
        }

        cin >> n;

        if (n)
            cin >> s;

        int m = 0;

        for (int i=0; i<n; i++)
        {
            if (m && a[w[m-1]][s[i]])
                w[m-1] = a[w[m-1]][s[i]];
            else
                w[m++] = s[i];

            int j;
            for (j=0; j<m-1; j++)
                if (b[w[j]][w[m-1]])
                    break;

            if (j < m-1)
                m = 0;
        }

        cout << "[";

        if (m)
            cout << w[0];

        for (int j=1; j<m; j++)
            cout << ", " << w[j];

        cout << "]" << endl;
    }

    return 0;
}
