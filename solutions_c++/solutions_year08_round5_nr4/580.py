#include <iostream>
#define MOD 10007
using namespace std;

int DP[200][200];
int A[200][200];
int movei[6] = {2, 1};
int movej[6] = { 1, 2 };
int main()
{
    int q; cin >> q;
    for (int qq = 0; qq < q; qq++)
    {
        
        
    memset(DP, 0, sizeof(DP));
    memset(A, 0, sizeof(A));
        
    int N, M, R;
    cin >> N >> M >> R;
    for (int i = 0; i < R; i++)
    {
        int a, b;
        cin >> a >> b;
        A[a-1][b-1] = 1;
    }
    
    DP[0][0] = 1;
    for (int i = 0; i < N; i++)
     for (int j = 0; j < M; j++) if (DP[i][j])
     {
         for (int m = 0; m < 2; m++)
         {
             int newi = i + movei[m];
             int newj = j + movej[m];
             
             if (newi < 0 || newi == N || newj < 0 || newj == M || A[newi][newj]) continue;
             
             DP[newi][newj] += DP[i][j];
             DP[newi][newj] %= MOD;
         }
     }
     cout << "Case #" << qq+1 << ": " << DP[N-1][M-1] << endl;
   }
}
