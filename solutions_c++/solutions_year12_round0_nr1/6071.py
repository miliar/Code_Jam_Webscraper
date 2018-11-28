#include <iostream>
#include <string>
using namespace std;

char toAlpha[27] = {
    'y', 'h', 'e', 's', 'o',
    'c', 'v', 'x', 'd', 'u',
    'i', 'g', 'l', 'b', 'k',
    'r', 'z', 't', 'n', 'w',
    'j', 'p', 'f', 'm', 'a',
    'q',
};

int main() {
    int T;
    cin >> T;
    cin.ignore();
    for (int c = 0; c < T; c++) {
        string line;
        getline(cin, line);
        for (string::iterator it = line.begin(); it != line.end(); it++) {
            if (isalpha(*it)) {
                *it = toAlpha[*it - 'a'];
            }
        }
        cout << "Case #" << c + 1 << ": " << line << endl;
    }
}