#include <iostream>
#include <math.h>

using namespace std;

int main(){
    int t,n,k,checker;
    cin >> t ;
    for (int i=0 ; i!= t; i++){
        cin >> n >> k;
        checker = pow(2,n);
        k = k%checker+1;
        cout << "Case #" << i+1 << ": ";
        if (checker&k) cout << "ON"<<endl;
        else cout << "OFF" <<endl;
        }
    
    return 0;
}
