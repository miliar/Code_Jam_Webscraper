#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int cases, cas;
    cin >> cases;
    for(cas = 1; cas <= cases; cas++)
    {
        long long n, k;
        cin >> n >> k;
        bool on = true;
        for(int i = 1; i <= n; i++)        
        {
                if(k%2 != 1)        
                { on = false; break;}
                k /= 2;
        }
        if(on)
              cout << "Case #" << cas << ": ON" << endl;
        else
              cout << "Case #" << cas << ": OFF" << endl;
    }
    return 0;    
}
