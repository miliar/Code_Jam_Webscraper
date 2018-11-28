#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#include <set>
#ifndef __SIZE__
    #define __SIZE__ 1000
#endif

using namespace std;

typedef int int32_t;

template <typename type>
type *getNextRecycledNumber(int32_t n, int32_t *digs) {
  int32_t a = digs[n-1];
  int32_t j = 0;

    for (int32_t i = n - 2; i >= 0; i--) {
        digs[i+1] = digs[i];
    }

    digs[0] = a;
  return digs;
}

template <typename t>
t* getDigits(t * ret, t number, int32_t *n) {
  t ten = 10;
  int32_t i = 0;

    while (number != 0) {
      t rem = number % ten;
        if (ret) {
            ret[i] = rem;
        }
        i++;
        number = (number - rem)/ten;
    }
#ifdef DEBUG_DETAIL
  int32_t size = ret.size();
    for (int32_t i = 0; i < size; i++) {
        cout << ret[i] << " ";
    }
    cout << endl;
#endif
    if (n) {
        *n = i;
    }
  return ret;
}

template <typename rtype, class itype>
rtype constructNumberFromArray(itype *digits, int32_t f, int32_t t) {
  rtype ret = 0;
  rtype pow10 = 1;

    for (int32_t i = f; i < t; i++) {
        ret += digits[i] * pow10;
        pow10 *= 10;
    }

  return ret;
}

int32_t howManyRecycledPairs(int32_t a, int32_t b) {
  int32_t number_of_digits = 0;
  int32_t *digs;
  int32_t *ddigs;
  int32_t *adigs;
  int32_t *bdigs;
  int32_t ret = 0;
  int32_t upper_bound = 0;

    getDigits<int32_t>(NULL, a, &number_of_digits);
    adigs = (int32_t*)malloc(sizeof(int32_t)*number_of_digits);
    bdigs = (int32_t*)malloc(sizeof(int32_t)*number_of_digits);
    digs = (int32_t*)malloc(sizeof(int32_t)*number_of_digits);

    adigs = getDigits<int32_t>(adigs, a, NULL);
    bdigs = getDigits<int32_t>(bdigs, b, NULL);

    //upper_bound = a + (b-a)/number_of_digits;
    upper_bound = b;

    for (int32_t i = a; i < upper_bound; i++) {
        digs = getDigits<int32_t>(digs, i, NULL);

#ifdef DEBUG
        fprintf(stdout, "%d: ", i);
#endif

        ddigs = digs;

        for (int32_t j = 0; j < number_of_digits-1; j++) {
          int32_t rn = 0;
            ddigs = getNextRecycledNumber<int32_t>(number_of_digits, ddigs);

            if (!ddigs) {
              break;
            }

            rn = constructNumberFromArray<int32_t, int32_t>(ddigs, 0, number_of_digits);

#ifdef DEBUG
            fprintf(stdout, "\t - %d % ", rn);
#endif

            if (i < rn && rn <= b) {
                ret++;
#ifdef DEBUG
                fprintf(stdout, "is in interval\n");
#endif
            }
#ifdef DEBUG
            else {
                fprintf(stdout, "is not in interval\n");
            }
#endif
        }
#ifdef DEBUG
        fprintf(stdout, "\n");
#endif
    }

  return ret;
}

int main(int argc, char **argv) {
  int32_t  t = 0;
  int32_t  a = 0;
  int32_t  b = 0;

    fscanf(stdin, "%d", &t);

    for (int32_t i = 0; i < t; i++) {
        fscanf(stdin, "%d %d", &a, &b);

        fprintf(stdout, "Case #%d: %d\n", i+1, howManyRecycledPairs(a, b));
    }
  return 0;
}
