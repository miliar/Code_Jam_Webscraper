#include <iostream>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
        int n,k;
        cin >> n >> k;
        if( k + 1 & ( (1 << n) - 1) )
            cout << "Case #" << i << ": OFF" << endl;
        else
            cout << "Case #" << i << ": ON" << endl;
    }
}
