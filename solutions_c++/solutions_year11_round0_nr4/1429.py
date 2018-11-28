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

#define forn(i, n) for(int i=0; i < (int)(n); i++)

using namespace std;

int main() {
    int n;
    cin >> n;
    
    for(int z=1; z<=n; z++) {
        //Read inputs
        int N;
        cin >> N;
        
        double res = N;
        forn(i, N) {
            int tmp;
            cin >> tmp;
            if(tmp == i+1) {
                res--;
            }
        }
        
        //Print outputs
        printf("Case #%d: ", z);
        cout.precision(6);
        cout << fixed << res << endl;
    }
    
    return 0;
};
