#include <iostream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <vector>

using namespace std;

long long ev(const string& s) {
    long long res = 0;
    string buf = "";
    char sign = 0;
    for (int i=0; i<s.length(); ++i) {
        if (s[i] == '+' || s[i] == '-') {
            long long num = atoll(buf.c_str());

            switch (sign) {
            case '+':
                res += num;
                break;

            case '-':
                res -= num;
                break;

            default:
                res = num;
                break;
            }

            sign = s[i];
            buf = "";
        } else {
            buf += s[i];
        }
    }

    long long num = atoll(buf.c_str());

    switch (sign) {
    case '+':
        res += num;
        break;

    case '-':
        res -= num;
        break;

    default:
        res = num;
        break;
    }

    return res;
}

long long f(string& s, int pos) {
    if (pos >= s.length()) {
        long long num = ev(s);
        if (num < 0) {
            num = -num;
        }

        if ((num & 1) == 0 ||
            num % 3 == 0 ||
            num % 5 == 0 ||
            num % 7 == 0 ) {
            return 1;
        } else {
            return 0;
        }
    }

    s.insert(pos, 1, '+');
    int res = f(s, pos + 2);
    s[pos] = '-';
    res += f(s, pos + 2);
    s.erase(pos, 1);
    res += f(s, pos + 1);

    return res;
}

int main() {
    string s;
    getline(cin, s);
    stringstream ss(s);

    int testsNum;
    ss >> testsNum;
    for (int test=1; test <= testsNum; ++test) {
        string eq;
        getline(cin, eq);

        cout << "Case #" << test << ": " << f(eq, 1) << endl;
    }

    return 0;
}
