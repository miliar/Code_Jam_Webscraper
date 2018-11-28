#include <iostream>

using namespace std;

int nc;

int main(){
    cin >> nc;
    for (int q = 1; q<= nc; q++){
        cout << "Case #" << q << ": ";
        int a,b;
        cin >> a >> b; b++;
        int div = 1 << a;
        if (b % div == 0) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
    
    return 0;
}
