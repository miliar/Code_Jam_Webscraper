#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <utility>
#include <cstring>
using namespace std;

#define forn(i, n)      for(int i=0; i < (int)(n); i++)
#define pb              push_back

typedef vector<int> VI;

int main() {
    int n;
    cin >> n;
    
    for(int z=1; z<=n; z++) {
        //Read inputs
        int T;
        cin >> T;
        VI candies(T);
        forn(i, T) {
            cin >> candies[i];
        }
        
        int res = -1;
        forn(i, (1 << T)-1) {
            int sumA = 0;
            int sumB = 0;
            int xorA = 0;
            int xorB = 0;
            
            forn(j, T) {
                if((i & (1<<j)) == (1<<j)) {
                    sumA += candies[j];
                    xorA ^= candies[j];
                } else {
                    sumB += candies[j];
                    xorB ^= candies[j];
                }
            }
            
            if(xorA == xorB && sumA > res) {
                res = sumA;
            }
            
        }
        
        //Print outputs
        printf("Case #%d: ", z);
        if(res == -1) {
            cout << "NO" << endl;
        } else {
            cout << res << endl;
        }
    }
    
    return 0;
};
