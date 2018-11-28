#include <iostream>
#include <string>
#include <map>

using namespace std;

int a[1024];
map <string, int> m;

int main()
{
    int t;
    cin >> t;
    for (int tt=1; tt<=t; tt++)
    {
        int n, k, i, j, u;
        cin >> n;
        m.clear();
        char s[128];
        cin.getline(s, 128);
        for (i=0; i<n; i++)
        {
            cin.getline(s, 128);
            m[s] = i+1;
        }
        cin >> k;
        cin.getline(s, 128);
        for (i=0; i<k; i++)
        {
            cin.getline(s, 128);
            a[i] = m[s];
        }
        int ans = -1;
        for (j=0; j<k; ans++)
        {
            int b = 0;
            for (i=1; i<=n; i++)
            {
                for (u=j; u<k; u++)
                    if (a[u] == i)
                        break;
                if (u > b)
                    b = u;
            }
            j = b;
        }
        cout << "Case #" << tt << ": " << (ans>0?ans:0) << endl;
    }
}
