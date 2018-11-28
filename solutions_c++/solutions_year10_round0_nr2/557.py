#include <iostream>

#include <gmp.h>
#include <gmpxx.h>

#include <string>
#include <algorithm>

int main ( ) {

    int number_of_cases, N;
    std::string input_string;
    std::cin >> number_of_cases;

    mpz_class input_list[1000]; //Max number of input numbers
    mpz_class current_diff, current_gcd, temp, final;

    for ( int cse = 1; cse <= number_of_cases; cse++ ) {

        std::cin >> N;

        for ( int i = 0; i < N; i++ )
            std::cin >> input_list[i];
        
        std::sort ( input_list, input_list + N );

        current_gcd = 0;
        for ( int i = 1; i < N; i++ ) {
            current_diff = input_list[i] - input_list[i-1];
            mpz_gcd ( temp.get_mpz_t(), current_gcd.get_mpz_t(), current_diff.get_mpz_t() );
            current_gcd = temp;
        }

        temp = input_list[0] % current_gcd;

        if ( temp == 0 )
            std::cout << "Case #" << cse << ": " << 0 << std::endl;
        else {
            final = current_gcd - temp;
            std::cout << "Case #" << cse << ": " << final << std::endl;
        }
    }

    return 0;
}
