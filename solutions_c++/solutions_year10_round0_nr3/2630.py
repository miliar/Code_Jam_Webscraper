#include <iostream>

int main() {
    const unsigned long int MIN_TT=1, MAX_TT=50;
    const unsigned long int MIN_RR=1, MAX_RR=100000000;
    const unsigned long int MIN_KK=1, MAX_KK=1000000000;
    const unsigned long int MIN_NN=1, MAX_NN=1000;
    const unsigned long int MIN_GG=1, MAX_GG=10000000;
    unsigned long int TT, RR, KK, NN;
    unsigned long int GG[MAX_NN];
    unsigned long int seatsremaining;
    unsigned long int index;
    unsigned long int profit_part_a;
    unsigned long int profit_part_b;
    unsigned long int first_index_this_ride;
    unsigned long int z;
    unsigned long int i;    

    const unsigned long int max_long_int = 2147483647;
    const unsigned long int multiplier[10] = { 8, 4, 6, 3, 8, 4, 7, 4, 1, 2 }; 

    int answer_digits[19];
    int new_digits[19];
    int answer_digit_count;
    bool leading_zeros=true;
    unsigned long int remainder;

    std::cin >> TT;
    for (z=1; z<=TT; z++) {
        std::cin >> RR >> KK >> NN;
        for (i=0; i<NN; i++) {
            std::cin >> GG[i];
        }

        seatsremaining=KK;
        index = 0;
        profit_part_a = 0;
        profit_part_b = 0;
        first_index_this_ride = 0;
        for (i=0; i<RR; i++) {
            while (seatsremaining>=GG[index]) {
                seatsremaining-=GG[index]; 
                if (max_long_int - profit_part_a >= GG[index]) {
                    profit_part_a += GG[index];
                } else {
                    profit_part_b += 1;
                    profit_part_a = GG[index] - 1 - (max_long_int - profit_part_a);
                }
                index++;
                if (index==NN) { index=0; };
                if (index==first_index_this_ride) { break; };
            }
            first_index_this_ride = index;
            seatsremaining=KK;
        }
        
        std::cout << "Case #" << z << ": ";
        if (profit_part_b == 0) {
            std::cout << profit_part_a << '\n';
        } else {
            answer_digit_count = 0;
            for (int i=0; i<19; i++) {
                answer_digits[i] = 0;
            }
            for (int i=0; i<19; i++) {
                if (profit_part_b > 10) {
                    answer_digits[i] = profit_part_b % 10;
                    profit_part_b /= 10;
                } else {   
                    answer_digits[i] = profit_part_b;
                    profit_part_b = 0;
                }
            }

            /* multiply part_b by 2147483648 */
            remainder = 0;
            for (int i = 0; i < 19; i++) {
                for (int j = 0; (j <= i and j < 10); j++) {
                    remainder += (answer_digits[i-j] * multiplier[j]);
                }
                new_digits[i] = remainder % 10;
                remainder /= 10;
            }
            for (int i = 0 ; i < 19; i++) {
                answer_digits[i] = new_digits[i];
            }
            
            /* add part_a */
            remainder = 0;
            for (int i = 0; i < 19; i++) {
                if (profit_part_a > 10) {
                    remainder += answer_digits[i] + (profit_part_a % 10);
                    profit_part_a /= 10;
                } else {   
                    remainder += answer_digits[i] + profit_part_a;
                    profit_part_a = 0;
                }
                new_digits[i] = remainder % 10;
                remainder /= 10;
            }
            for (int i = 0 ; i < 19; i++) {
                answer_digits[i] = new_digits[i];
            }
            
            leading_zeros=true;
            for (int i=18; i>=0; i--) {
                if (answer_digits[i] == 0 and leading_zeros) {
                    /* do not output leading zeros */
                } else {
                    leading_zeros = false;
                    std::cout << answer_digits[i];
                }
            }
            std::cout << '\n';
        }
    }
}