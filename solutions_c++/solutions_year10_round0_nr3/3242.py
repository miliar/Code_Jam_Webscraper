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
    long int K;
    long int R;
    long int G[1000];
    long int N;
    long int prev;
    long int where;
    long int money;
    long int current;
    long int start;

    if (file.is_open()) {
        if (output.is_open()) {
            getline(file,line);
            T = strtol(&line[0],NULL,10);
            for (int i = 1; i < T+1; i++) {
                getline(file,line);
                R = strtol(&line[0],NULL,10);
                K = strtol(&line[line.find(" ")],NULL,10);
                N = strtol(&line[line.rfind(" ")],NULL,10);
                getline(file,line);
                for (int j = 0; j < N; j++) {
                    if (j == 0) {
                        G[j] = strtol(&line[0],NULL,10);
                        prev = 0;
                        continue;
                    }
                    G[j] = strtol(&line[line.find(" ",prev+1)],NULL,10);
                    prev = line.find(" ",prev+1);
                }

                money = 0;
                where = 0;
                for (int r = 0; r < R; r++) {
                    current = 0;
                    start = where;
                    while((K-current) >= G[where]) {
                        money += G[where];
                        current += G[where];
                        where++;
                        if(where >= N) where = 0;
                        if(where == start) break;
                    }
                }
                output << "Case #" << i << ": " << money << endl;

            }
        }
    }
    return 1;
}
