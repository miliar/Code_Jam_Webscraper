#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream inFile("A_small.in");
    ofstream outFile("results.txt");

    int T;
    inFile >> T;
    long int N,K;
    for (int i = 1; i <= T; i++) {
        inFile >> N;
        inFile >> K; // Case #1: OFF
        int light = ((K+1) % (2 << (N-1)));
        outFile << "Case #" << i << ": " << ((light == 0) ? "ON" : "OFF") << endl;
    }

    inFile.close();
    outFile.close();

}
