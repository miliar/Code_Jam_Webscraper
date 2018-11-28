#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

bool is_ugly(long long a) {
    return (a % 2 == 0) ||
           (a % 3 == 0) ||
           (a % 5 == 0) ||
           (a % 7 == 0);
}

long long result = 0;

long long evaluate(string& a) {
    long long value = 0L;
    long long tmp = 0;
    char op = '+';
    for (int i = 0; a[i]; ++i) {
        char c = a[i];
        if (c == '+' || c == '-') {
            if (op == '+')
                value += tmp;
            else
                value -= tmp;
            op = c;
            tmp = 0;
        }
        else {
            tmp *= 10;
            tmp += c - '0';
        }
    }
    if (op == '+')
        value += tmp;
    else
        value -= tmp;
    return value;
}


void test(string& a, string& b) {
    if (b.size() == 0) {
        long long value = evaluate(a);
        if (is_ugly(value)) {
            result += 1;
        }
    }
    else {
        string x = a+b[0];
        string y = b.substr(1);
        test(x, y);

        x = a + '+' + b[0];
        y = b.substr(1);
        test(x, y);

        x = a + '-' + b[0];
        y = b.substr(1);
        test(x, y);
    }
}

int main() {
    int t;
    scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        string n;
        cin >> n;
        result = 0;
        string x = n.substr(0, 1);
        string y = n.substr(1);
        test(x, y);
        printf("Case #%d: %lld\n", i + 1, result);
    }
}
