#include <stdlib.h>
#include <iostream>
#include <math.h>

using namespace std;

long long int T, L, P, C;
int *results;

int main(int argc, char** argv) {
    cin >> T;
    results = new int[T];


    for (int i = 0; i < T; i++) {
        cin >> L >> P >> C;

        int counter = 0;
        long long int temp = L;
        for (temp *= C; temp < P; temp *= C) {
            counter++;
        }

        results[i] = ceil(log(counter+1) / log(2));
        counter = 0;
        temp = 0;
    }
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ": " << results[i] << endl;
    }
    return 0;
}

