#include <iostream>
#include <cstdio>

using namespace std;

int power(int num)
{
    int ret = 1;
    
    for(int ix = 0; ix < num; ix++)
        ret *= 10;
        
    return ret;
}

int main()
{
    int T, A, B, digits, recycled, ans, it, history[7];

    cin >> T;
    
    for(int ix = 0; ix < T; ix++)
    {
        cin >> A;
        cin >> B;
        
        digits = 1;
        ans = 0;

        for(int iy = 10; iy <= A; iy *= 10)
            digits++;
        
        for(int iy = A; iy < B; iy++)
        {
            recycled = iy;
            for(it = 0; it < 7; it++)
                history[it] = -1;
            
            for(int iz = 0; iz < digits; iz++)
            {
                recycled = (recycled%10)*power(digits-1)+(recycled/10);
                if(recycled > iy && recycled <= B)
                {
                    for(it = 0; it < iz; it++)
                    {
                        if(history[it] == recycled)
                            break;
                    }
                    
                    if(it == iz)
                    {
                        ans++;
                        history[iz] = recycled;
                    }
                    
                    
                }
            }
        }
        
        if(ix+1 != T)
            printf("Case #%i: %i\n", ix+1, ans);
        else
            printf("Case #%i: %i", ix+1, ans);
    }
    
    return 0;
}
