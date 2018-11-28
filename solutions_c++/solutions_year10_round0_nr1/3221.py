#include <iostream>

using namespace std;

int main(){
    long long T;
    cin >> T;
    int pow2[40];
    pow2[0] = 1;
    for(int i=1;i<40;i++) pow2[i] = pow2[i-1]*2;
    
    for(int t=1;t<=T;t++){
            long long N,K;
            cin >> N >> K;
            cout << "Case #" << t << ": " << ( ( (K % pow2[N]) == pow2[N]-1) ? "ON" : "OFF" ) << endl;
    }
}
