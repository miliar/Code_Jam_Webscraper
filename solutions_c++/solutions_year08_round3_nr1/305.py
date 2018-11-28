/*
 * File:   template.c
 * Author: rsalmeidafl
 *
 * Created on 26 de Julho de 2008, 23:32
 */

#include <stdio.h>
#include <stdlib.h>
#include <list>

using namespace std;

/*
 *
 */
int main(int argc, char** argv) {

    int number_of_test_cases;
    int current_test_case = 1;

    scanf("%d", &number_of_test_cases);

    while (current_test_case <= number_of_test_cases) {
        /* Input */
        int P, K, L;
        list<int> frequencies;

        scanf("%d %d %d", &P, &K, &L);

        for (int i = 0; i < L; ++i) {
            int f;
            scanf("%d", &f);
            frequencies.push_back(f);
        }

        /* Computations */
        frequencies.sort();

        long long keypresses = 0;
        list<int>::const_reverse_iterator pFreq = frequencies.rbegin(),
                                          pFreqEnd = frequencies.rend();

        int counter = 0;
        long long multiplier = 1;
        while (pFreq != pFreqEnd) {
            if (counter == K) {
                counter = 0;
                multiplier += 1;
            }
            long long llf = *pFreq;
            keypresses += llf*multiplier;
            ++counter;
            ++pFreq;
        }

        /* Output */
        printf("Case #%d: ", current_test_case);

        list<int> digits;
        while (keypresses > 0) {
            digits.push_back(keypresses % 10);
            keypresses /= 10;
        }
        while (!digits.empty()) {
            printf("%d", digits.back());
            digits.pop_back();
        }
        printf("\n");


        /* Loop */
        ++current_test_case;
    }


    return (EXIT_SUCCESS);
}


