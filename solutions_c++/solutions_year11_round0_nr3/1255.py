#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("c.in");
ofstream fout("c.out");
#define cin fin
#define cout fout
int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t )
    {
        int n, sum = 0, small = 10000000, x, ans = 0;
        cin >> n; 
        for (int i = 1; i <= n; ++i )
        {
            cin >> x;
            sum += x;
            if (small>x) small = x;
            ans ^= x;
        }
        cout << "Case #" << t <<": ";
        if (ans) cout << "NO\n";
        else cout << sum - small << endl;
    }
    system("pause");
}
