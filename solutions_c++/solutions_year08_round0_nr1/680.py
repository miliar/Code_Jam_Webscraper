#include <iostream>
#include <string>
#include <map>
using namespace std;

int main()
{
    int t, cnt = 0;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int n;
        cin >> n;
        string s;
        getline(cin, s);
        map <string, int> mp;
        for (int i=0;i<n;i++)
        {
            getline(cin, s);
            mp[s] = 0;
        }
        int k, m = n;
        cin >> k;
        int ans = 0;
        getline(cin, s);
        for (int i=0;i<k;i++)
        {
            getline(cin, s);
            if (mp[s]++ == 0) m--;
            if (m == 0)
            {
                ans++;
                for (map <string, int>::iterator iter = mp.begin();
                     iter != mp.end(); iter++)
                    iter->second = 0;
                mp[s]++; m = n - 1;
            }
        }
        cout << "Case #" << ++cnt << ": " << ans << endl;
    }
    return 0;
}
