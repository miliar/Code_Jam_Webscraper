
#include <iostream>
#include <cstdlib>
#include <list>

using namespace std;

const unsigned int offset = 65;

bool opposed[26][26];
char combinations[26][26];
list<char> invoked;

void init() {
    for (unsigned int i = 0; i < 26; ++i) {
        for (unsigned int j = 0; j < 26; ++j) {
            opposed[i][j] = false;
            combinations[i][j] = '#';
        }
    }

    invoked.clear();
}

void readCombinations() {
    unsigned int c;
    cin >> c;

    for (unsigned int i = 0; i < c; ++i) {
        char elements[3];
        cin >> elements;
        combinations[elements[0] - offset][elements[1] - offset] = elements[2];
        combinations[elements[1] - offset][elements[0] - offset] = elements[2];
    }
}
void readOpposingElements() {
    unsigned int d;
    cin >> d;

    for (unsigned int i = 0; i < d; ++i) {
        char elements[2];
        cin >> elements;
        opposed[elements[0] - offset][elements[1] - offset] = true;
        opposed[elements[1] - offset][elements[0] - offset] = true;
    }
}

void readElements() {
    unsigned int n;
    cin >> n;

    for (unsigned int i = 0; i < n; ++i) {
        char element;
        cin >> element;

        if (invoked.size() > 0) {
            char comb = combinations[element - offset][invoked.back() - offset];
            if (comb != '#') {
                invoked.pop_back();
                invoked.push_back(comb);
                continue;
            } else {
                bool cont = false;
                for (list<char>::iterator it = invoked.begin(); it != invoked.end(); ++it) {
                    if (opposed[element - offset][*it - offset]) {
                        invoked.clear();
                        cont = true;
                        break;
                    }
                }
                if (cont) {
                    continue;
                }
            }
        }

        invoked.push_back(element);
    }
}

void writeElements() {
    cout << '[';
    bool firstElement = true;
    for (list<char>::iterator it = invoked.begin(); it != invoked.end(); ++it) {
        if (!firstElement) {
            cout << ", ";
        }
        cout << *it;
        firstElement = false;
    }
    cout << ']';
}

void doTestcase() {
    init();
    readCombinations();
    readOpposingElements();
    readElements();
    writeElements();
}

int main(int argc, char *argv[]) {
    unsigned int t;
    cin >> t;
    for (unsigned int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        doTestcase();
        cout << endl;
    }
}

