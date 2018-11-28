#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
using namespace std;


int main(int argc, char **argv) {

    // read input file
    ifstream ifile (argv[1]);
    ofstream ofile (argv[2]);

    if (!ifile || !ofile) { cout << "Error: files cant be opened"; exit (1); }

    int T, t = 1;
    int A, B;
    char buff[1000];

    ifile >> T;

    while (t <= T) {
        int count = 0;

        // Read A B
        ifile >> A >> B;

        // Generate numbers b/n range A B
        for (int n = A; n <= B; n++) {
            int n_copy = n;
            int digits = 1;
            int rem, m;
            int pow_10;

            while ((n_copy /= 10) > 0) digits++;

            n_copy = n;
            // Generate possible m for n where (n,m) is a recycled pair
            for (int i = 1; i < digits; i++) {
                pow_10 = pow (10, i);
                rem = n % pow_10;
                n_copy = n / pow_10;
                m = rem * pow (10, digits-i);
                m += n_copy;

                if ((A <= n) && (n < m) && (m <= B)) count++;
            }
        }

        ofile << "Case #" << t << ": " << count << endl;
        t++;
    }
}
