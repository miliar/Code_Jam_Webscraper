#include <fstream>
#include <string>
#include <iostream>

using namespace std;

char sredi(char c) {
    switch (c) {
        case 'y':
            return 'a';
            break;
        case 'n':
            return 'b';
            break;
        case 'f':
            return 'c';
            break;
        case 'i':
            return 'd';
            break;
        case 'c':
            return 'e';
            break;
        case 'w':
            return 'f';
            break;
        case 'l':
            return 'g';
            break;
        case 'b':
            return 'h';
            break;
        case 'k':
            return 'i';
            break;
        case 'u':
            return 'j';
            break;
        case 'o':
            return 'k';
            break;
        case 'm':
            return 'l';
            break;
        case 'x':
            return 'm';
            break;
        case 's':
            return 'n';
            break;
        case 'e':
            return 'o';
            break;
        case 'v':
            return 'p';
            break;
        case 'z':
            return 'q';
            break;
        case 'p':
            return 'r';
            break;
        case 'd':
            return 's';
            break;
        case 'r':
            return 't';
            break;
        case 'j':
            return 'u';
            break;
        case 't':
            return 'w';
            break;
        case 'h':
            return 'x';
            break;
        case 'a':
            return 'y';
            break;
        case 'q':
            return 'z';
            break;
        case 'g':
            return 'v';
            break;
    }
}

int main() {
    ofstream fout ("googlish.out");
    ifstream fin ("googlish.in");
    int brtest;
    string tekst;

    fin >> brtest;

    cout << brtest;

    getline(fin, tekst);

    for (int i=0; i<brtest; ++i) {
        getline(fin, tekst);
        for (int j=0; j<tekst.size(); ++j) {
            if (tekst[j] != ' ')
                tekst[j] = sredi(tekst[j]);
        }
        fout << "Case #" << i+1 << ": " << tekst << endl;

    }

    return 0;
}
