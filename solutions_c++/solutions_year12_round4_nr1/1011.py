#include <iostream>
#include <cstdio>

using namespace std;

int d[10000], l[10000], b[10000];
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++)
    {
        int N, D;
        cin >> N;
        for (int i = 0; i < N; ++i)
        {
            cin >> d[i] >> l[i];
            b[i] = -1;
        }
        cin >> D;

        b[0] = d[0];
        for (int i = 0; i < N; i++)
        {
            for (int j = i+1; j < N; j++)
            {
                if (d[j] <= d[i] + b[i])
                {
                    int tmp = min(l[j], d[j] - d[i]);
                    if (b[j] < tmp)
                        b[j] = tmp;
                }
                else
                    break;
            }
        }

        cout << "Case #" << test << ": ";
        int ok=0;
        for (int i=0; i < N; i++)
            if ((b[i] != -1) && (D <= d[i] + b[i]))
            {
                ok = 1;
                break;
            }
        if (ok)
            cout << "YES";
        else
           cout << "NO";
        cout << "\n";
    }
    cout << flush;
    return 0;
}
