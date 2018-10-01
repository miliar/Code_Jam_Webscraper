#include <cstdio>
#include <cstring>
#include <cstdlib>

bool is_palindrome(long long x) {
    char s[25];
    sprintf(s, "%lld", x);
    int len = strlen(s);
    for (int i = 0; i < len; ++i) {
        if (s[i] != s[len - i - 1]) {
            return false;
        }
    }
    return true;
}

int main() {
    for (long long n = 1; n <= 10010000; ++n) {
        long long nn = n * n;
        if (is_palindrome(n) && is_palindrome(nn)) {
            printf("%lld\n", nn);
        }
    }
    return 0;
}
