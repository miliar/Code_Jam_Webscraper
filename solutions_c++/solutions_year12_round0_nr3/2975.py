#include <cassert>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <map>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

const int N = 1000+10;

bool isDan(int n) {
    int k = 0;
    char s[100];
    sprintf(s, "%d", n);
    int digits[10] = {};
    for (int i = 0; s[i] != '\0'; i++) {
        if (digits[s[i]-'0']++) {
            k++;
        }

    }

    if (k == 2) {
        for (int i = 1; s[i] != '\0'; i++) {
            if (s[i-1] == s[i])
                return false;
        }
        return true;
    }
    return false;
}

int calc(int a, int b) {
    int ans = 0;
    for (int i = a; i <= b; i++) {
        char s[100];
        sprintf(s, "%d", i);

        int dan = isDan(i);
        bool found = false;
        int n = strlen(s);
        for (int j = 1; j < n; j++) { // start position

            int ndigits = 0;
            int x = 0;
            int y = 0;
            for (int k = 0; k < n; k++) {
                x = 10*x + (s[k] - '0');
                y = 10*y + (s[(k+j)%n] - '0');
            }
            if (x < y && y <= b) {
                assert(x < y);
                assert(a <= x && x <= b);

                // printf("%d %d\n", x, y);

                if (dan) {
                    found = true;
                }
                else {
                    ans++;
                }
            }
        }

        if (found && dan) ans++;

    }
    return ans;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int a, b;
        scanf("%d %d", &a, &b);

        //printf("%d %d %d\n", memo[a], memo[b], memo[b-a]);
        // printf("a:%d b:%d %d\n", a, b, calc(a, b));

        printf("Case #%d: %d\n", cc+1, calc(a, b));
    }
}

