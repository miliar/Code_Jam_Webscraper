#include <iostream>
#include <string.h>
using namespace std;
#define N 35

bool State[N];
bool Pow[N];

int main()
{
    freopen("in.in", "r", stdin);
 	freopen("in1.out", "w", stdout);
    int t, n, k;
    cin >> t;
    int i = 0;
    while(t--)
    {
        cin >> n >> k;
        i ++;
        memset(State, 0, sizeof(State));
        memset(Pow, 0, sizeof(Pow));
        
        State[0] = true;
        Pow[0] = true;
        Pow[1] = true;
            
        for(int j = 1; j <= k; j ++)
        {
             for(int m = 1; m <= n; m ++)
             if(Pow[m]) State[m] = !State[m];
             else break;
             
             for(int m = 2; m <= n; m ++)
             if(State[m - 1] && Pow[m - 1]) Pow[m] = true;
             else 
             {
                  memset(Pow + m, 0, (N - m) * sizeof(bool));
                  break;
             }     
        }
        
        bool tag;
        if(Pow[n] && State[n]) tag = true;
        else tag = false;
      
        cout << "Case #" << i << ": ";  
        if(tag) cout << "ON " << endl;
        else cout << "OFF " << endl;
    }
    
    return 0;
}
