#include <iostream>
using namespace std;

void solve()
{
     int N, K;
     cin >> N >> K;
     int needed = (1<<N)-1;
     if ((needed&K) != needed) cout << "OFF" << endl;
     else cout << "ON" << endl;
}

int main()
{
    int q;
    cin >> q;
    for (int i = 1; i <= q; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }
}
