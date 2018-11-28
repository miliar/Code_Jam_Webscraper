#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main() {
    ifstream file("input.txt");
    ofstream output("output.txt");
    string line;
    long int L;
    long int P;
    long int C;
    long int T;
    long int pow;
    long int Lorig;
    long int findpow(long int L, long int P, long int C);

    if (file.is_open()) {
        if (output.is_open()) {
            getline(file,line);
            T = strtol(&line[0],NULL,10);
            for (int i = 1; i < T+1; i++) {
                getline(file,line);
                L = strtol(&line[0],NULL,10);
                P = strtol(&line[line.find(" ")],NULL,10);
                C = strtol(&line[line.rfind(" ")],NULL,10);
                Lorig = L;
                if (L*C >= P) {
                    output << "Case #" << i << ": 0\n";
                    continue;
                }
                pow = findpow(L,P,C);
                output << "Case #" << i << ": " << pow << endl;
            }
        }
    }
    return 1;
}

long int findpow(long int L, long int P, long int C) {
    long int p = 0;
    long int Lorig;
    if (L*C >= P) {
        return 0;
    }
    if (L*C*C >= P) {
        return 1;
    }
    if (L*C*C*C*C >= P) {
        return 2;
    }
    Lorig = L;
    while(L*C<P) {
        p++;
        L*=C;
    }
    if (p%2 == 1) return 1+findpow(Lorig,Lorig*(long int)pow((double)C,(double)(p/2 + 1)),C);
    if (p%2 == 0) return 1+findpow(Lorig,Lorig*(long int)pow((double)C,(double)(p/2 + 1)),C);
}
