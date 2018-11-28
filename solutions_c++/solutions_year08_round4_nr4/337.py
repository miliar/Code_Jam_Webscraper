#include <iostream>
#include <algorithm>
using namespace std;

void solve()
{
     int k;
     cin >> k;
     string S;
     cin >> S;
     
     int m[5];
     for (int i = 0; i < k; i++)
      m[i] = i;
     
     
     int ans = 10000000;
     do
     {
           string S1 = S;
           
           for (int i = 0; i < S1.size(); i++)
            S1[i] = S[i-(i%k) + m[i%k]];
           
           int curans = 0;
           char prev = '.';
           for (int i = 0; i < S1.size(); i++)
           {
               if (S1[i] != prev) curans++;
               prev = S1[i];
           }
           ans = min(ans, curans);
     }
     while (next_permutation(m, m + k));
     cout << ans << endl;
}
int main()
{
    int q; cin >> q;
    for (int i = 0; i < q; i++)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
