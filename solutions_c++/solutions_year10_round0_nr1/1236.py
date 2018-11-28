#include <iostream>


int main ( ) {
    
    int num_cases, N, K;

    std::cin >> num_cases;

    int masks[33] = { };

    for ( int i = 1; i < 33; i++ ) {
        int mask = 1 << (i-1);
        for ( int j = i; j < 33; j++) {
            masks[j] |= mask; 
        }
    }//Inefficient... could be done with a single loop

    for ( int i = 1; i <= num_cases; i++ ) {
        std::cin >> N >> K;
        //std::cout << "N=" << N << ", K=" << K << "  ";
        std::cout << "Case #" << i << ": ";
        //if ( K & (1 << (N-1)) ) {
        if ( (masks[N] & K) == masks[N] ) { 
            std::cout << "ON";
        } else {
            std::cout << "OFF";
        }
        std::cout << std::endl;
    }

    return 0;
}
