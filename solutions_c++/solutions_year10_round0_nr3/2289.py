#include "util.h"
#include <iostream>

using namespace std;


int main()
{
    int T;
    
    cin >> T;
    
    for (int t = 0; t < T ; ++t)
    {
        int R, k, N;
        
        cin >> R >> k ;
        
        V<int> g;
        
        cin >> g;
        
        N = g.size();
        
        long long int s = 0;
        int i = 0;
        
        for (int r = 0; r < R; ++r)
        {
            int np = 0;
            for (int ng = 0; ng < N && np + g.at(i) <= k; i = (i + 1) % N, ++ng)
            {
                s += g.at(i);
                np += g.at(i);
            }
        }
        
        cout << "Case #" << (t + 1) << ": " << s << endl;
    }
        
}
