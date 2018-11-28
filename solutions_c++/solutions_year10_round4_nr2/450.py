#include <iostream>
#include <algorithm>
#define IMPOSSIBLE 2000000000
using namespace std;

int DP[4000][400];
int A[2000];
int P2[2000];
int P[2000];
int N;
int Q;

int dp(int n, int k)
{
    if (DP[n][k] != -1) return DP[n][k];
    
    //cout << n << " " << k << endl;
    if (n > N-1) 
    {
          //cout << n << " " << k << endl;
          if (k >= A[n - (N-1)]) return DP[n][k] = 0;
          else 
          {
               //cout << k << A[n - (N-1)] << endl;
               return DP[n][k] = IMPOSSIBLE;
          }
    }
    
    int t1 = dp(2*n, k);
    int t2 = dp(2*n, k+1);
    int t3 = dp(2*n+1, k);
    int t4 = dp(2*n+1, k+1);
    
    long long ans = min((long long)t1 + t3, (long long)t2 + t4 + P[n]);
    
    if (ans >= IMPOSSIBLE) return DP[n][k] = IMPOSSIBLE;
    else return DP[n][k] = ans;
}

void solve()
{
     memset(DP, -1, sizeof(DP));
     
     cin >> Q;
     
     //int N = 1;
     N=1;
     for (int i = 0; i < Q; i++) N*=2;
     for (int i = 1; i <= N; i++)
     {
         cin >> A[i];
         A[i] = max(Q-A[i], 0);
     }
     
     for (int i = 0; i < N-1; i++)
     {
         cin >> P2[i];
     }
     
     int sum = 0, c = 1;
     for (int i = 1; sum < N-1; i *= 2)
     {
         int start = N-1 - sum - i;
         for (int j = start; j < start + i; j++)
          P[c++] = P2[j];
         sum += i;
     }
     /*cout << "aaoao" << endl;
     for (int i = 1; i <= N; i++) 
     {
         cout << A[i] << " ";
         }
         cout << endl;
*/
     cout << dp(1, 0) << endl;
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
