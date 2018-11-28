#include <iostream>
#include <algorithm>
#include <vector>

#define all(x) (x).begin(), (x).end()

using namespace std;

int T, n;

int isok(vector<bool> &sel, vector<int> &v, int patrick)
{
    int sum = 0;
    for (int i = 0; i < n; i++)
        if (!sel[i]) sum = sum ^ v[i];

    int bit = -1;
    for (int m = 0; m < 21; m++)
        if ((patrick & (1 << m)) != (sum & (1 << m)))
        {
            bit = m;
            break;
        }

    return bit;
}

int main()
{
    cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> n;
        vector<int> bitsum(21, 0);
        vector<int> v(n);
        for (int i = 0; i < n; i++)
        {
            cin >> v[i];
            for (int m = 0; m < 21; m++)
                if ((1 << m) & v[i])
                    bitsum[m]++;
        }

        bool ok = true;
        for (int i = 0; i < 21; i++)
            if (bitsum[i] & 1)
            {
                ok = false;
                break;
            }
    
        cout << "Case #" << t << ": ";
        if (!ok)
            cout << "NO" << endl;
        else
        {
            sort(all(v));
            vector<bool> sel(n, false);
            sel[0] = true;
            int sum = 0, patrick = v[0];

            for (int i = 1; i < v.size(); i++)
            {
                int bit = isok(sel, v, patrick);
                
                int j = 0;
                while (j < n)
                {
                    if (sel[j]) j++;
                    else if (v[j] & (1 << bit))
                        break;
                    else
                        j++;
                }

                if (j == n)
                    break;
                else
                {
                    sel[j] = true;
                    patrick = patrick ^ v[j];    
                }
            }

            if (isok(sel, v, patrick) == -1)
            {
                int res = 0;
                for (int i = 0; i < n; i++)
                    if (!sel[i]) res += v[i];
                cout << res << endl;
            }
            else
                cout << "NO" << endl;
        }
    }

    return 0;
}
