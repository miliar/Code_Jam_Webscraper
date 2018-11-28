#include <iostream>
using namespace std;

void solve()
{
     int N, ans = 0;
     cin >> N;
     for (int i = 1; i <= N; i++)
     {
         int a;
         cin >> a;
         if (a != i)
         {
            ans++;
         }
     }
     cout << ans << ".000000" << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
