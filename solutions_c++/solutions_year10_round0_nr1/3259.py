#include <iostream>

using namespace std;

bool solve(unsigned N, unsigned long K){
    ++K;
    for (unsigned i = 0; i < N; ++i){
        if ((K >> i) & 1){
            return false;
        }
    }

    return true;
}

int main(){
    
    unsigned tc_count = 0;
    cin >> tc_count;
    for (unsigned tc = 1; tc <= tc_count ; ++tc){
        unsigned N = 0;
        unsigned long K = 0;
        cin >> N; cin >> K;
        cout << "Case #" << tc << ": " << (solve(N, K)?"ON":"OFF") << endl;
    }

    return 0;
}
