#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define tiao system("pause")

int main(void)
{
    int i,j,k,ci,cici,cicici;
    int t;
    int n;
    
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    
    cin >> t;
    for (cicici=1; cicici<=t; cicici++)
    {
        cin >> n >> k;
        
        bool isOK = true;
        for (i=0; i<n; i++)
            if ((k & (1 << i)) == 0)
            {
                isOK = false;
                break;
            }
            
        if (!isOK) cout << "Case #" << cicici << ": OFF\n";
        else cout << "Case #" << cicici << ": ON\n";
    }
    
//    tiao;
    return 0;
}
