#include <cstdio>
#include <iostream>
using namespace std;

int t,n,k,w;

int main(){
    cin >> t;
    for (int i = 0; i < t; i++){
        cin >> n >> k;
        k+=1;
        n = 1 << n;
        if (k % n == 0) cout << "Case #" << (i+1) << ": " << "ON" << endl;
        else cout << "Case #" << (i+1) << ": " << "OFF" << endl;
    }
    return 0;
}
