#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

int T, N, K;

int main() {
    ifstream entrada("A-large.in");
    ofstream salida("A-large.out");
    
    entrada >> T;
    for(int i = 1; i <= T; i++) {
        entrada >> N >> K;
        int mask = (int)pow(2.0f,(float)N) - 1;
        if((K & mask) == mask) {
            salida << "Case #" << i << ": ON" << endl;
        } else {
            salida << "Case #" << i << ": OFF" << endl;
            //cout << i << ": " << N << " " << K << " " << (K & mask) << " " << mask << endl;;
        }   
    }
    
//    cin.get();
    salida.close();
    return 0;
}
