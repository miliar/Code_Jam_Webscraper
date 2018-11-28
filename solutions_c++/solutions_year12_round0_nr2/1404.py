#include <iostream>
#include <vector>
using namespace std;

void solve()
{
     int N, S, p;
     cin >> N >> S >> p;
     
     vector<int> v;
     int ans = 0;
     for (int i = 0; i < N; i++)
     {
         int a;
         cin >> a;
         if (a/3 >= p - 2)
         {
            if (a/3 >= p) ans++;
            else if (a/3 == p-1)
            {
               if (a%3 > 0) ans++;
               else if (S > 0 && a/3 > 0) ans++, S--;
            }
            else if (a/3 == p-2)
            {
               if (a%3 == 2 && S > 0) ans++, S--;
            }
         }
     }
     cout << ans << endl;
}

int main()
{
    int n;
    cin >> n;
    for (int q = 0; q < n; q++)
    {
        cout << "Case #" << q+1 << ": ";
        solve();
    }
}
