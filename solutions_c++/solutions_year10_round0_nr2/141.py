#include <iostream>
#include <cstdio>
using namespace std;

typedef long long LL;

LL nums[3], N;

LL solve()
{
    sort(nums, nums + N);
    
    LL g = 0;
    for (int i = 0; i < N - 1; i++)
        for (int j = i + 1; j < N; j++)
        {
            if (g == 0)
               g = nums[j] - nums[i];
            else
               g = __gcd(g, nums[j] - nums[i]);
        }   
    
    LL start = nums[N - 1] / g;
    for (LL i = start;;i++)
    {
        LL res = g * i;
        
        LL diff = -1; bool ok = true;
        for (int j = N - 1; j >= 0; j--)
        {
            if (res - nums[j] < 0)
            {
                ok = false;
                break;    
            }
            
            if ((nums[j] + diff) % g != 0 && diff != -1)
            {
                ok = false;
                break;    
            }
            
            if (diff == -1)
               diff = res - nums[j];
        }
            
        if (ok)
           return diff;
    }
         
    return -1;     
}

int main()
{
    int T;
    cin >> T;
    
    for (int TT = 1; TT <= T; TT++)
    {
        cin >> N;
        
        for (int i = 0; i < N; i++)
            cin >> nums[i];
            
        cout << "Case #" << TT << ": " << solve() << endl;
    }
        
    return 0;
}
