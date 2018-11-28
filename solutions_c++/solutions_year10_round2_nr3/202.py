#include <iostream>
#define MOD 100003
using namespace std;


int DP[505][505][505];

int dp(int n, int k, int l)
{
    if (k < 0) return 0;
    if (n == 1)
    {
          if (l == 1 && k == 0) return 1;
          else return 0;
    }
    
    int &ret = DP[n][k][l];
    if (ret != -1) return ret;
    
    ret = 0;
    
    //put a bit here
    if (n == l) ret = (ret + dp(n-1, k-1, k))%MOD;
    else ret = (ret + dp(n-1, k-1, l))%MOD;
    //put a zero
    ret = (ret + dp(n-1, k, l))%MOD;
    
    return ret;
}

void solve()
{
     int N;
     cin >> N;
     
     int ans = 0;
    
     for (int i = 1; i <= N-1; i++)
      ans = (ans + dp(N-1, i-1, i))%MOD;
     
     cout << ans << endl;
}

int main()
{
    memset(DP, -1, sizeof(DP));
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
