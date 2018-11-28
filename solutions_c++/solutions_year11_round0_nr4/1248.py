#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("d.in");
ofstream fout("d.out");
#define cin fin
#define cout fout

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t )
    {
        int n, ans = 0;
        cin >> n;
        for (int i = 1; i <= n; ++i )
        {
            int x;
            cin >> x;
            ans += (x!=i);
        }
        cout << "Case #" << t << ": " << ans << endl;
    }
    system("pause");
}
