#include <stdio.h>
#include <iostream>
#define fo(i,n) for(i=0;i<n;i++)
using namespace std;

int k, t, i, n;

int main(void){
    freopen("A-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    cin >> t;
    fo(i,t){
            cin >> n >> k;
            int z = (1 << n) - 1;
            cout << "Case #" << i+1 << ": ";
            if (z <= k && (k - z) % (z+1) == 0) cout << "ON"; else cout << "OFF";
            cout << endl;
            }
    
    
}
