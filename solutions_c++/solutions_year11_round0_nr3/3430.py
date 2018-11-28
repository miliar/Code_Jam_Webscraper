#include <iostream>
using namespace std;
const int maxn = 1007;
int n;
int s[maxn];
int x;
int m;
int su;
int main()
{
    int T;
    cin >> T;
    for (int t=1; t<=T; t++)
    {
        x = 0;
        m = 1000009;
        su = 0;
        cin >> n;
        for (int i=0; i<n; i++)
        {
            cin >> s[i];
            x ^= s[i];
            su += s[i];
            m = m<s[i]?m:s[i];
        }
        cout << "Case #" << t << ": ";
        if (x != 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << su - m << endl;
        }
    }
    return 0;
}
