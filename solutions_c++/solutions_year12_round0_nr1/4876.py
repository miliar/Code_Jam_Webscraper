#include <iostream>
#include <string>
#include <cmath>

using namespace std;

char from[26] = {
    'y',
    'h',
    'e',
    's',
    'o',
    'c',
    'v',
    'x',
    'd',
    'u',
    'i',
    'g',
    'l',
    'b',
    'k',
    'r',
    'z',
    't',
    'n',
    'w',
    'j',
    'p',
    'f',
    'm',
    'a',
    'q'
};

int main(int argc, char** argv)
{
    size_t n;
    string s;
    cin >> n;
    getline(cin, s);
    for (size_t i = 0; i < n; ++i) {
        string str;
        getline(cin, str);
        for (size_t j = 0; j < str.size(); ++j) {
            if (str[j] >= 'a' && str[j] <= 'z') str[j] = from[str[j]-'a'];
        }
        cout << "Case #" << (i+1) << ": " << str << endl;
    }
}

