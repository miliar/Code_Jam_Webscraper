#include <iostream>
using namespace std;
int n, l, h;
int f[1000];

bool divide(int m, int n) {
    if(m % n == 0 || n % m == 0) {
        return true;
    }
    
    return false;
}


int main() {
    int test;
    cin >> test;
    
    for(int task = 1; task <= test; ++task) {
        cin >> n >> l >> h;
        
        for(int i = 0; i < n; ++i) {
            cin >> f[i];
        }
        
        bool possible = true;
        int fre = 0;
        for(int j = l; j <= h; ++j) {
            possible = true;
            for(int k = 0; k < n; ++k) {
                if(!divide(j, f[k])) {
                    possible = false;
                    break;
                }
            }
            
            if(possible) {
                fre = j;
                break;
            }
        }
        
        if(possible) {
            cout << "Case #" << task << ": " << fre << endl;
        }
        else {
            cout << "Case #" << task << ": NO" << endl;
        }
    }
}
