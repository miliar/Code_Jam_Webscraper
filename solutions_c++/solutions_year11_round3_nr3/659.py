#include <iostream>
using namespace std;

long long gcd(long long a, long long b)
{
     if (b == 0) return a;
     return gcd(b, a%b);
}

void solve()
{
     int N;
     long long L, H;
     cin >> N >> L >> H;
     
     long long R[10000];
     for (int i = 0; i < N; i++)
     {
         cin >> R[i];
     }

     long long ans = -1;
     for (long long i = L; i <= H; i++) 
     {
         bool flag = 0;
         for (int j = 0; j < N; j++)
         {
           if (R[j]%i == 0 || i % R[j] == 0)
           {
           }
           else
           {
              flag = 1;
           }
         }
         if (!flag) { ans = i; break; }
      }
     
     if (ans != -1)
     {
        cout << ans << endl;
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
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}
