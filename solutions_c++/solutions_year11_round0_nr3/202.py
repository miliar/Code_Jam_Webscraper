#include<iostream>
using namespace std;

int main() {
    int T, C=1;
    cin >> T;
    while(T--) {
        int N, x=0, min=0, sum=0;
        cin >> N;
        while(N--) {
            int c;
            cin >> c;
            if(min == 0 || c < min) {
                min = c;
            }
            
            x ^= c;
            sum += c;
        }
        
        cout << "Case #" << C++ << ": " ;
        if(x == 0) {
            cout << sum - min << endl;
        } else {
            cout << "NO" << endl;
        }
    }
}
