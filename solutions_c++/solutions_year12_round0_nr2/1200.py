#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 128;
const int INF = 1000000;

int N, S, P;

int points[MAXN];
int DP[MAXN][MAXN];
bool have[MAXN][MAXN];

bool canWithP(int totSum)
{
    for (int a = 0; a <= 10; a++)   
        for (int b = a; b <= 10; b++)
            for (int c = b; c <= 10; c++)
            {
                if (a + b + c != totSum) continue;
                if (c - a <= 1 && c >= P) return true;
            }
            
    return false;
}

bool canSurpriseWithP(int totSum)
{
    for (int a = 0; a <= 10; a++)   
        for (int b = a; b <= 10; b++)
            for (int c = b; c <= 10; c++)
            {
                if (a + b + c != totSum) continue; 
                
                if (c - a == 2 && c >= P) return true;
            }
            
    return false;
}

int rec(int pos, int rem)
{
    if (pos == N) { if (rem == 0) return 0; else return -INF; }
    if (have[pos][rem]) return DP[pos][rem];
    
    int result = -INF;
    
    //Be a not suprising
    result = max(result, rec(pos + 1, rem) + canWithP(points[pos]));
    
    //Be a suprising
    if (rem > 0) result = max(result, rec(pos + 1, rem - 1) + canSurpriseWithP(points[pos]));
    
    have[pos][rem] = true;    
    return DP[pos][rem] = result;
}

int solve()
{
    memset(DP, -1, sizeof(DP));
    memset(have, 0, sizeof(have));
    
    return rec(0, S);
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> S >> P;
        
        for (int i = 0; i < N; i++)
            cin >> points[i];
        
        int result = solve();
        printf("Case #%d: %d\n", t, result);
    }    
    
    return 0;
}
