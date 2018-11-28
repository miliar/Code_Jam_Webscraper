#include <iostream.h>

int main() {
    
    unsigned int T;
    unsigned int N;
    unsigned long int K;
    
    cin >> T;
    
    unsigned int i;
    for (i = 0; i < T; i++) {
        cin >> N;
        cin >> K;
        
        unsigned int mask_for_N = ~(-1 << N);
        unsigned long int one_more_than_K = K + 1;

        if (one_more_than_K & mask_for_N) {
           cout << "Case #" << i+1 << ": OFF" << endl;
        } else {
           cout << "Case #" << i+1 << ": ON" << endl;
        }                
    }    
}
