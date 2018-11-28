
/*
 * File:   template.c
 * Author: rsalmeidafl
 *
 * Created on 26 de Julho de 2008, 23:32
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <list>
#include <string>
#include <iostream>

using namespace std;

typedef struct {
    int m2;
    int m3;
    int m5;
    int m7;
} ugly_remainders;

list<string> debugstack;
int          debugcount;

void debugprint(int print = 0) {
/*    if (!print) return;
    list<string>::iterator i = debugstack.begin(), iEnd = debugstack.end();
    while (i != iEnd) {
        cout << *i << ' ';
        ++i;
    }
    cout << '\n';*/
}

ugly_remainders compute_remainders(char *string) {
    const char *pStart = string + strlen(string);
    const char *pEnd = string;
    --pStart; --pEnd;

    ugly_remainders retval = {0};
    retval.m2 = (*pStart - '0') % 2;
    retval.m5 = (*pStart - '0') % 5;

    int m7 = 1;
    while (pStart != pEnd) {
        retval.m3 += (*pStart - '0') % 3;
        retval.m7 += m7*(*pStart - '0') % 7;
        m7 *= 10;
        m7 = m7 % 7;
        --pStart;
    }

    retval.m3 = retval.m3 % 3;
    retval.m7 = retval.m7 % 7;

    return retval;
}

ugly_remainders add(ugly_remainders onleft, ugly_remainders onright) {
    ugly_remainders addition;
    addition.m2 = (onleft.m2 + onright.m2) % 2;
    addition.m7 = (onleft.m7 + onright.m7) % 7;
    addition.m3 = (onleft.m3 + onright.m3) % 3;
    addition.m5 = (onleft.m5 + onright.m5) % 5;

    return addition;
}

ugly_remainders subtract(ugly_remainders onleft, ugly_remainders onright) {
    ugly_remainders addition;
    addition.m2 = (onleft.m2 - onright.m2) % 2;
    addition.m7 = (onleft.m7 - onright.m7) % 7;
    addition.m3 = (onleft.m3 - onright.m3) % 3;
    addition.m5 = (onleft.m5 - onright.m5) % 5;

    return addition;
}


long long ugly(ugly_remainders addition) {
    if (!addition.m2 || !addition.m3 || !addition.m5 || !addition.m7) {
        debugprint(1);
        return 1;
    }
    else
        return 0;
}


long long compute_number_of_ugly_numbers(ugly_remainders onleft, char *string, int first_pass = 0) {
    char leftpart[41];
    leftpart[0] = string[0];
    leftpart[1] = '\0';
    char *rightpart = string + 1;
    int i = 1;

    /* The whole number */
    debugstack.push_back(string);
    debugcount += 2;
    ugly_remainders whole_number = compute_remainders(string);
    long long number_of_ugly_numbers = ugly(add(onleft,whole_number)) +
                                       ugly(subtract(onleft,whole_number));
    debugprint();
    debugstack.pop_back();


    if (first_pass) {
        number_of_ugly_numbers /= 2;
        debugcount -= 1;
    }

    while (strlen(rightpart) > 0) {

        debugstack.push_back(std::string(leftpart));

        ugly_remainders onright = compute_remainders(leftpart);
        /*if (strlen(rightpart) > 1) {*/
            if (first_pass)
                number_of_ugly_numbers += compute_number_of_ugly_numbers(onright, rightpart);
            else {
                number_of_ugly_numbers += compute_number_of_ugly_numbers(add(onleft, onright), rightpart);
                number_of_ugly_numbers += compute_number_of_ugly_numbers(subtract(onleft, onright), rightpart);
            }
        /*}
        else {
            debugstack.push_back(std::string(rightpart));
            ugly_remainders final = compute_remainders(rightpart);
            ugly_remainders addcase = add(onleft, onright);
            ugly_remainders subcase = subtract(onleft, onright);

            number_of_ugly_numbers += ugly(add(addcase, final)) + ugly(add(subcase, final)) +
                    ugly(subtract(addcase, final)) + ugly(subtract(subcase, final));

            debugcount += 4;

            debugprint();
            debugstack.pop_back();
        }*/

        debugstack.pop_back();

        leftpart[i] = *rightpart;
        leftpart[i + 1] = '\0';
        ++rightpart;
        ++i;
    }

    return number_of_ugly_numbers;
}

/*
 *
 */
int main(int argc, char** argv) {

    int number_of_test_cases;
    int current_test_case = 1;

    scanf("%d", &number_of_test_cases);

    while (current_test_case <= number_of_test_cases) {
        /* Input */
        char string[41];
        scanf("%s", string);
        debugstack.clear();
        debugcount = 0;

         /* Computations */
        ugly_remainders zero = {0};
        long long keypresses = compute_number_of_ugly_numbers(zero, string, 1);

        /* Output */
        printf("Case #%d: ", current_test_case);

        list<int> digits;
        while (keypresses > 0) {
            digits.push_back(keypresses % 10);
            keypresses /= 10;
        }
        if (digits.empty())
            printf("0");
        while (!digits.empty()) {
            printf("%d", digits.back());
            digits.pop_back();
        }
        printf("\n", debugcount);


        /* Loop */
        ++current_test_case;
    }


    return (EXIT_SUCCESS);
}

