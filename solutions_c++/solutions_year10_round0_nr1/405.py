#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int powers[32];

string solve(int N, int K)
{
   if (K % powers[N] == powers[N] - 1)    
      return "ON";
   else
      return "OFF";
}

int main()
{
    powers[0] = 1;
    for (int i = 1; i <= 30; i++)
        powers[i] = powers[i - 1] * 2;
    
    int T;
    scanf("%d", &T);
    for (int TT = 1; TT <= T; TT++)
    {
        int N, K;
        scanf("%d%d", &N, &K);
        
        printf("Case #%d: %s\n", TT, solve(N, K).c_str());
    }
           
    return 0;
}
