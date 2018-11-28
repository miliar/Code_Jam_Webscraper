#include <iostream>
#include <string>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, i, j;
    string s;
    cin >> t;
    for(i = 1; i <= t; i++)
    {
        int c = 0, m = 0;
        unsigned long long result;
        bool used[256] = {false};
        int d[256];
        for(j = 0; j < 256; j++)
            d[j] = -1;
        cin >> s;
        for(j = 0; j < s.size(); j++)
            used[s[j]] = true;
        for(j = 0; j < 256; j++)
            if(used[j])
                c++;
        if(c == 1)
            c = 2;
        d[s[0]] = 1;
        for(j = 1; j < s.size(); j++)
            if(d[s[j]] == -1)
            {
                d[s[j]] = m++;
                if(m == 1)
                    m++;
            }
        result = 0;
        for(j = 0; j < s.size(); j++)
            result = result * c + d[s[j]];
        cout << "Case #" << i << ": " << result << endl;
    }
    return 0;
}
