#include <iostream>
#include <string>
#include <map>

using namespace std;

map<char, char> letterMap = {
    {'y', 'a'},
    {'n', 'b'},
    {'f', 'c'},
    {'i', 'd'},
    {'c', 'e'},
    {'w', 'f'},
    {'l', 'g'},
    {'b', 'h'},
    {'k', 'i'},
    {'u', 'j'},
    {'o', 'k'},
    {'m', 'l'},
    {'x', 'm'},
    {'s', 'n'},
    {'e', 'o'},
    {'v', 'p'},
    {'z', 'q'},
    {'p', 'r'},
    {'d', 's'},
    {'r', 't'},
    {'j', 'u'},
    {'g', 'v'},
    {'t', 'w'},
    {'h', 'x'},
    {'a', 'y'},
    {'q', 'z'},
    {' ', ' '},
};

int main(void) {
    int numLines = 0;
    cin >> numLines;

    for (int i = 0; i <= numLines; i++) {
        string line;
        getline(cin, line);

        if (line.empty())
            continue;

        cout << "Case #" << i << ": ";
        for (char letter : line) {
            cout << letterMap.at(letter);
        }
        cout << endl;
    }
}
