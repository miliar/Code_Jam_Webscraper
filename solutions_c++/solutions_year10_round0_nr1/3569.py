#include <iostream>
using namespace std;

int main(void){
    int n;
    cin >> n;
    for(int c=0;c<n;c++){
        cout << "Case #" << c+1 << ": ";
        int n,k;
        cin >> n >> k;
        unsigned int t = 1;
        t <<= n;
        if(k%t==t-1)
            cout << "ON" << endl;
        else
            cout << "OFF" << endl;
    }
    return 0;
}
