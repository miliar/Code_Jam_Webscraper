#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    ifstream in("lights.in");
    ofstream out("lights.txt");
    int t;
    in >> t;
    for (int z=1; z<=t; z++) {
        long long N, K, M, A;
        in >> N >> K;
        A = 1 << N;
        M = K % A;
        //out << "N: " << N << " K: " << K << " M: " << M << endl;
        out << "Case #" << z << ": " << (M == (A - 1) ? "ON" : "OFF" ) << endl;        
    }
}
