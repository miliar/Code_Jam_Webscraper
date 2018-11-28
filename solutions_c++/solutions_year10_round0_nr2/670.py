#include <iostream>
#include <algorithm>
using namespace std;

long long gcd(long long a, long long b)
{
     if (b == 0) return a;
     return gcd(b, a%b);
}

void solve()
{
     long long a[3];
     long long N;
     cin >> N;
     for (int i = 0; i < N; i++) cin >> a[i];
     sort(a, a + N);
     
     long long T = a[1]-a[0];
     //cout << T << endl;
     for (int i = 2; i < N; i++) T = gcd(T, a[i] - a[i-1]);
     cout << (T-(a[0]%T))%T << endl;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
    }    
    return 0;
}
