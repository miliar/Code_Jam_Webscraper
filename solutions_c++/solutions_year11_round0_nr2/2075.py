#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>

using namespace std;

char r[300][300];
int inc[300][300];

int main()
{
    int t;
    cin >> t;
    for (int ca = 1; ca <= t; ++ca)
    {
        memset(r, 0, sizeof(r));
        memset(inc, 0, sizeof(inc));
        int c, d, n;
        string str;
        cin >> c;
        while ( c-- )
        {
            cin >> str;
            r[str[0]][str[1]] = str[2];
            r[str[1]][str[0]] = str[2];
        }
        cin >> d;
        while ( d-- )
        {
            cin >> str;
            inc[str[0]][str[1]] = 1;
            inc[str[1]][str[0]] = 1;
        }
        cin >> n;
        cin >> str;
        string ans = "";
        for (int i = 0; i < n; )
        {
            for (int j = 0; j < (int)ans.size(); ++j)
            {
                if ( inc[ans[j]][str[i]] == 1 )
                {
                    ans = "";
                    i++;
                    break;
                }
            }
            if ( i < n )
            {
                if ( i < n-1 && r[str[i]][str[i+1]] > 0 )
                {
                    ans += r[str[i]][str[i+1]];
                    i += 2;
                    continue;
                }
                else
                    ans += str[i];
            }
            i++;
        }
        cout << "Case #" <<  ca << ": [";
        for (int i = 0; i < (int)ans.size(); ++i)
        {
            if ( i == 0 )
                cout << ans[i];
            else
                cout << ", " << ans[i];
        }
        cout << "]\n";
    }
    return 0;
}
