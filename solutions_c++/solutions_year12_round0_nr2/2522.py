#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int T, N, S, p, t, result, point, left, xp;
    
    cin >> T;
    
    for(int ix = 0; ix < T; ix++)
    {
        result = 0;
        cin >> N;
        cin >> S;
        cin >> p;
        xp = S;
        
        for(int iy = 0; iy < N; iy++)
        {  
            cin >> t;
            
            point = t/3;
            left = t-(point*3);
            
            if(point >= p)
                result++;
            else if(left > 0)
            {
                if(point+1 >= p)
                    result++;
                else if(left == 2 && point+2 >= p && xp > 0)
                {
                    result++;
                    xp--;
                }
            }
            else if(t%3 == 0 && xp && point != 0)
            {
                if(point+1 >= p)
                {
                    result++;
                    xp--;
                }
            }
            
            /*if(point+left >= p)
                result++;*/
        }
        
        printf("Case #%i: %i\n", ix+1, result);
    }

    return 0;
}
