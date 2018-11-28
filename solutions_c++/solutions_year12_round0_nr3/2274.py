#include <fstream>
#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <iterator>
#include <algorithm>
#include <cstring>
#include <cmath>

#include <cstdio>
#include <cstdlib>

using namespace std;

volatile int digits = -1;

void convert(int x, char *strx) {
    int k = 0;
    while (x) {
        strx[k++] = x % 10 + '0';
        x /= 10;
    }
    if (digits == -1) digits = k;
}

void debug(char *str) {
    for (int j = 0; j < digits; j++) {
        printf("%c", str[digits - j - 1]);
    }
    printf("\n");
}

int convert(char *str) {
    int x = 0;
    for (int j = 0; j < digits; j++) {
        x = x * 10 + str[digits - j - 1] - '0';
    }
    return x;
}

int get_recycle_pairs(int x, char *smax) {
    int counter = 0;
    static char strx[16];
    vector<int> generated_numbers;
    convert(x, strx);

    static char str[32];
    str[0] = 0;
    strncpy(str, strx, digits);
    strncpy(str + digits, strx, digits);

    for (int i = 0; i < digits; i++) {
        // Ignore numbers starting with 0
        if (str[i + digits - 1] == '0') continue;

        // Current number has to be less or equal than max
        // and greater than x
        int ok = 1;
        for (int j = 0; j < digits; j++) {
            char c1 = smax[digits - j - 1];
            char c2 = str[digits - j - 1 + i];
            if (c1 < c2) {
                ok = 0;
                break;
            }
            else if (c1 == c2) {
                continue;
            }
            else {
                ok = 1;
                break;
            }
        }

        if (ok) {
            ok = 0;
            for (int j = 0; j < digits; j++) {
                char c1 = strx[digits -j - 1];
                char c2 = str[digits - j - 1 + i];
                if (c1 > c2) {
                    ok = 0;
                    break;
                }
                else if (c1 == c2) {
                    continue;
                }
                else {
                    ok = 1;
                    break;
                }
            }
        }

        if (ok && (find(generated_numbers.begin(), generated_numbers.end(), convert(str + i)) == generated_numbers.end())) {
            generated_numbers.push_back(convert(str + i));
            //printf("%d %d\n", convert(strx), convert(str + i));
            counter++;
        }
    }

    return counter;
}

int recycle(int min, int max) {
    int result = 0;
    static char smax[16];
    convert(max, smax);
    for (int i = min; i < max; i++) {
        result += get_recycle_pairs(i, smax);
    }
    return result;
}

int check_recycle_pair(int x, int y) {
    int counter = 0;
    static char strx[16];
    convert(x, strx);

    static char str[32];
    str[0] = 0;
    strncpy(str, strx, digits);
    strncpy(str + digits, strx, digits);

    static char stry[16];
    convert(y, stry);

    return strstr(str, stry) != NULL;
}

int recycle_serial(int min, int max) {
    int result = 0;    
    for (int i = min; i < max; i++) {
        for (int j = i + 1; j <= max; j++) {
            int tmp = check_recycle_pair(i, j);
            if (tmp) {
                printf("%d %d\n", i, j);
            }
            result += tmp;
        }
    }
    return result; 
}

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 0; i < T; i++) {
        int min, max;
        scanf("%d %d", &min, &max);
        digits = -1;
        printf("Case #%d: %d\n", i + 1, recycle(min, max));
        //printf("Case #%d: %d\n", i + 1, recycle_serial(min, max));
    }
    return 0;
}

