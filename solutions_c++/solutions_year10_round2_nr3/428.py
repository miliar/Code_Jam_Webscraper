#include <iostream>
#include <cstdio>  
using namespace std;

const int MOD = 100003;

int ans[501];
int DP[501][501];

void precompute()
{
    for (int i = 0; i <= 500; i++)
        DP[1][i] = 1; 
     
    for (int i = 2; i <= 500; i++)
        for (int j = 1; j <= 500; j++)
            for (int k = 0; k <= i && k <= j; k++)
            {
                DP[i][j] += DP[i - k][j]; 
                DP[i][j] %= MOD;
            }
        
    for (int i = 0; i <= 500; i++)
    {
        int a = 0, b = i;
        while (b >= 0)
        {
            ans[i] += DP[a][b];  
            ans[i] %= MOD;
            
            a++;
            b--;
        }
    }
}

int main()
{
    precompute();
    
    int T;
    cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        int N;
        cin >> N;
        
        cout << "Case #" << t << ": " << ans[N] << endl;
    }
    
    return 0;
}
