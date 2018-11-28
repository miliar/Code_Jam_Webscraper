#include <iostream>

int main() {
    const int MIN_TT=1, MAX_TT=10000;
    const int MIN_NN=1, MAX_NN=30;
    const int MIN_KK=0, MAX_KK=100000000;
    int TT, NN, KK;
    int POWERS_OF_TWO_LESS_ONE[MAX_NN+1];
    bool b;

    int v=1;
    for (int i=0; i<=MAX_NN; i++) {
        POWERS_OF_TWO_LESS_ONE[i]=v-1;
        v*=2; }

    std::cin >> TT;
    for (int z=1; z<=TT; z++) {
        std::cin >> NN >> KK;
        b =  (KK==0)  ? false
          : /*KK!=0*/   (((KK+1) & POWERS_OF_TWO_LESS_ONE[NN]) == 0); 
        std::cout << "Case #" << z << ": " << (b ? "ON" : "OFF") << '\n';
    }
}