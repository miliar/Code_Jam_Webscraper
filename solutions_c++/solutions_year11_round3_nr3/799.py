#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

typedef pair<int, int> PI;
typedef long long LL;

int N, L, H;

LL notes[16000];

void solve()
{
    for (LL test = L; test <= H; test++)
    {
        bool can = true;
        for (int i = 0; i < N; i++)
        {
            if (notes[i] % test == 0) continue;
            if (test % notes[i] == 0) continue;
               
            can = false;
            break;
        }
            
        if (can) { cout << test << endl; return; }
    }
            
    cout << "NO" << endl;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> L >> H;
        for (int i = 0; i < N; i++)
            cin >> notes[i];    
        
        cout << "Case #" << t << ": ";
        solve();
    }
    
    return 0;
}
