#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
#include <sstream>
#include <cstdlib>
#include <gmp.h>
#include <gmpxx.h>


using namespace std;


int main() {
    ifstream inFile("B_small.in");
    ofstream outFile("results.txt");

    unsigned int C;
    inFile >> C;

    for (int s = 1; s <= C; s++) {
            unsigned int N; inFile >> N;
            mpz_class* numbers = new mpz_class[N];

            for (int j = 0; j < N; j++) {
                string str;
                inFile >> str;
                numbers[j] = str;
            }

            mpz_class min = numbers[0];
            mpz_class ggt = abs(numbers[1] - numbers[0]);
            for (int i = 0; i < N; i++)
                for (int j = i+1; j < N; j++) {
                    mpz_class diff = abs(numbers[i] - numbers[j]);
                    mpz_gcd(ggt.get_mpz_t(),ggt.get_mpz_t(),diff.get_mpz_t());
                }
            mpz_class T = ggt;

            // min is  = min_{i,j} |t_i - t_j|
            mpz_class y = T - (numbers[0] % T);
            if (T == 1) y = 0;
            if (T == y) y = 0;
            cout << y.get_str() << "= y, T = " << T.get_str() << endl;
            outFile << "Case #" << s << ": " << y.get_str() << endl;
    }


    inFile.close();
    outFile.close();

}

/*
void generatePrimes(vector<long long>& primes) {
    primes.push_back(2); // Seeds the first primes
    primes.push_back(3);
    long long number = 5; // Next integer to be tested
    long long max_number = pow(10,25);
    for (; *(primes.end()-1) < max_number; number += 2) {
        // The maximum divisor we need to try is the sqrt of number
        long long const limit((long long)sqrt((double)number));

        // Divide by all primes we have up to limit
        for (vector<long long>::iterator count(primes.begin()+1);
        *count < max_number && *count <= limit; ++count)
        if (number%*count == 0) // Is it an exact divisor
        goto outer; // Yes, try the next one

        primes.push_back(number); // We got one!
    outer:;
    }
    cout << "the number of primes less than or equal to "
    << max_number + 1
    << " is " << primes.size() << "." << endl << endl;
}
*/
