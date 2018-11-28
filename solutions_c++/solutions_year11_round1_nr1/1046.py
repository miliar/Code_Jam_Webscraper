#include <iostream>

using namespace std;

int main ()
{
    freopen("aa.in", "r", stdin);
    freopen("aa.out", "w", stdout);
    
    int t;
    cin >> t;
    
    for(int i = 0; i < t; ++i)
    {
        long n;
        int pd, pg;
        cin >> n >> pd >> pg;
        
        bool found = false;
        for(long j = n; j > 0; --j)
        {
            if((j*pd) % 100 == 0)
            {
                found = true;
                break;
            }
        }
        
        if(found)
        {
            if ((pg == 100 && pd != 100) || (pg == 0) && pd !=0)
                found = false;
        }
        
        printf("Case #%d: ", i+1);
        if (found)
            printf("%s\n", "Possible");
        else
            printf("%s\n", "Broken");
    }
    return 0;
}