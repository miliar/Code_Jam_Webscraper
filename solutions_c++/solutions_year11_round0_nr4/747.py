#include <iostream>
#include <cstdio>
using namespace std;

int N;
int numbers[1024];

int solve()
{
    int steps = 0; 
    for (int i = 0; i < N; i++)
    {
        if (numbers[i] == i + 1) continue;
        
        steps++;   
    }
    
    return steps;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> numbers[i];
            
        int res = solve();
        cout << "Case #" << t << ": " << res << endl;
    }
    
    return 0;
}
