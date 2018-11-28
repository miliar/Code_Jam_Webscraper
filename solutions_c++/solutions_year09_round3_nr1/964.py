#include <iostream>
#include <string>
#include <cstring>
#include <cctype>

using namespace std;

int digit[1000];

int main() {
    int C, base;
    cin >> C;

    string in;
    for (int i = 0; i < C; ++i) {

        cin >> in;

        memset(digit, -1, sizeof(digit));

        digit[in.at(0) - '0'] = 1;

        int p;
        for (p = 1; p < in.length(); ++p) {
            if (digit[in.at(p) - '0'] == -1) {
                digit[in.at(p) - '0'] = 0;
                break;
            }
        }

        base = 2;
        for (int j = p-1; j < in.length(); ++j) {
            if (digit[in.at(j) - '0'] == -1) {
                digit[in.at(j) - '0'] = base;
                ++base;
            }
        }
        int sum = 0, b = 1;
        for (int j = in.length(); j > 0; --j) {
            sum += b * digit[in.at(j-1) - '0'];
            b *= base;
        }

        cout << "Case #" << i + 1 << ": " << sum << endl;
    }
}
