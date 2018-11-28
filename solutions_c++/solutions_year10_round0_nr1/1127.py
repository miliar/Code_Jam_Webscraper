#include <iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    for(int ii = 1; ii <= T; ++ii){
        int N, K;
        cin >> N >> K;
        N = 1 << N;
        if((K+1) % N == 0){
            cout << "Case #" << ii << ": ON\n";
        }
        else {
            cout << "Case #" << ii << ": OFF\n";
        }
    }
    return 0;
}
