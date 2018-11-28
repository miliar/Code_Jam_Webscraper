#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <map>
#include <set>

using namespace std;
typedef unsigned long long ull;

bool fun(int n, int m)
{
    int _n = n, r, digits = 0, mul = 1;
    
    while(_n > 0)
    {
        digits++;
        _n /= 10;
        mul *= 10;
    }
    mul /= 10;
    for(int i = 0; i < digits; i++)
    {
        r = n%10;
        n /= 10;
        n += r*mul;
        if(n == m)
            return 1;
    }
    
    return 0;
}

int main()
{
    
    int cases, a, b, n, m, idx = 1, cnt;
    cin >> cases;
    
    while(cases--)
    {
        cnt = 0;
        cin >> a >> b;
        
        for(n = a; n <= b; n++)
        {
            for(m = n + 1 ; m <= b; m++)
            {
                if(fun(n, m))
                    cnt++;
            }
        }
        
        cout << "Case #" << idx++ << ": " << cnt << endl;
    }
    
    return 0;
}
