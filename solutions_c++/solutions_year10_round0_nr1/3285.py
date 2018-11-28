#include <iostream>
#include <fstream>
#include <math.h>

#define INPUT_FILE "A-large.in"
#define OUTPUT_FILE "A-large.out"

using namespace std;

int main (void) {

    ifstream input;
    ofstream output;
    
    input.open (INPUT_FILE);
    output.open (OUTPUT_FILE);

    if (input.is_open ()) {
        int data;
        input >> data;
        for (int d=0; d<data; d++) {
            int N, K;
            input >> N;
            input >> K;
            cout << "values:" << N << " " << K << endl;

            int x = pow (2,N);
            cout << "power:" << x << endl;
            
            int y = (x - 1 - K) % x;
            if (y)
                output << "Case #" << d + 1 << ":" << " OFF" << endl;
            else
                output << "Case #" << d + 1 << ":" << " ON" << endl;
        }
    }
    return 0;
}
