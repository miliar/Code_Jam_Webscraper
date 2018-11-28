#include <iostream>
#include <cstdio>
using namespace std;

int N;
int candies[1024];

int solve()
{
    int allXor = 0, allSum = 0, minCandy = 1000000000;
    for (int i = 0; i < N; i++)
    {
        allXor ^= candies[i];
        allSum += candies[i];
        
        if (candies[i] < minCandy)
           minCandy = candies[i];
    }
        
    if (allXor != 0) return -1;       
        
    return allSum - minCandy;    
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
       cin >> N;
       for (int i = 0; i < N; i++) cin >> candies[i];
       
       cout << "Case #" << t << ": ";
       int res = solve(); 
       
       if (res == -1)
          cout << "NO" << endl;
       else
          cout << res << endl;
    }
    
    return 0;
}
