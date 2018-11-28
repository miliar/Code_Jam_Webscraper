#include <iostream>
using namespace std;

int X[50], V[50], N, K, B, T;

void solve()
{
     cin >> N >> K >> B >> T; 
     for (int i = 0; i < N; i++) cin >> X[i];
     for (int i = 0; i < N; i++) cin >> V[i];
     
     int bavnipileta = 0;
     
     int ans = 0;
     for (int i = N-1; i >= 0; i--)
     {
         if (K == 0) break;
         if (B - X[i] > T*V[i]) bavnipileta++;
         else ans += bavnipileta, K--;
     }
     
     if (K) cout << "IMPOSSIBLE" << endl;
     else cout << ans << endl;     
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
    return 0;
}
