#include <iostream>
using namespace std;

void solve()
{
     int N, C[1000];
     cin >> N;
     int sum = 0, xorr = 0, minn = 1000006;
     for (int i = 0; i < N; i++)
     {
         cin >> C[i];
         sum += C[i];
         xorr ^= C[i];
         minn = (C[i] > minn) ? minn : C[i];
     }
     
     if (xorr == 0)
     {
         cout << sum - minn << endl;
     }
     else
     {
         cout << "NO" << endl;
     }
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
}
