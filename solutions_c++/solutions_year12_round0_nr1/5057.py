#include <string>
#include <iostream>

using std::string;

const char *googlerese = "ynficwlbkuomxsevzpdrjgthaq";

int main() {
    char *english = new char [26];
    for (int i = 0; i < 26; i++) english[googlerese[i]-'a'] = i+'a';

    int tests;
    std::cin >> tests;
    string line;
    std::getline(std::cin, line);
    for (int i = 1; i <= tests; i++) {
        std::getline(std::cin, line);

        string nu = line;
        for (int j = 0; j < (int)line.size(); j++)
            if (nu[j] != ' ')
                nu[j] = english[line[j]-'a'];

        std::cout << "Case #" << i << ": " << nu << '\n';
    }

    return 0;
}

