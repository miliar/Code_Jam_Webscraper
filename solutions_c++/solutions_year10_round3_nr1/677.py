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
    long int T;
    long int A[1000];
    long int B[1000];
    long int N;
    long int inter;

    if (file.is_open()) {
        if (output.is_open()) {
            getline(file,line);
            T = strtol(&line[0],NULL,10);
            for (int i = 1; i < T+1; i++) {
                inter = 0;
                getline(file,line);
                N = strtol(&line[0],NULL,10);
                for (int j = 0; j < N; j++) {
                    getline(file,line);
                    A[j] = strtol(&line[0],NULL,10);
                    B[j] = strtol(&line[line.find(" ")],NULL,10);
                }
                for (int j = 0; j < N; j++) {
                    for (int k = j+1; k < N; k++) {
                        if (A[j] > A[k] && B[j] < B[k]) {
                            inter++;
                            continue;
                        }
                        if (A[j] < A[k] && B[j] > B[k]) {
                            inter++;
                            continue;
                        }
                    }
                }
                output << "Case #" << i << ": " << inter << endl;
            }
        }
    }
    return 1;
}
