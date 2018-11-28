#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin ("A-small-attempt0.in");
ofstream fout ("A-small-attempt0.out");

char map(char c);

int main() {
    int t, x = 0;
    string g, s;
    fin >> t;
    getline(fin, g);
    for(int i = 0; i < t; i++) {
        getline(fin, g);
        s = g;
        for(int j = 0; j < g.length(); j++) {
            s[j] = map(g[j]);
        }
        fout << "Case #" << ++x << ": " << s << endl;
    }
    return 0;
}

char map(char c) {
    switch(c) {
        case 'a':
            return 'y';
            break;
        case 'b':
            return 'h';
            break;
        case 'c':
            return 'e';
            break;
        case 'd':
            return 's';
            break;
        case 'e':
            return 'o';
            break;
        case 'f':
            return 'c';
            break;
        case 'g':
            return 'v';
            break;
        case 'h':
            return 'x';
            break;
        case 'i':
            return 'd';
            break;
        case 'j':
            return 'u';
            break;
        case 'k':
            return 'i';
            break;
        case 'l':
            return 'g';
            break;
        case 'm':
            return 'l';
            break;
        case 'n':
            return 'b';
            break;
        case 'o':
            return 'k';
            break;
        case 'p':
            return 'r';
            break;
        case 'q':
            return 'z';
            break;
        case 'r':
            return 't';
            break;
        case 's':
            return 'n';
            break;
        case 't':
            return 'w';
            break;
        case 'u':
            return 'j';
            break;
        case 'v':
            return 'p';
            break;
        case 'w':
            return 'f';
            break;
        case 'x':
            return 'm';
            break;
        case 'y':
            return 'a';
            break;
        case 'z':
            return 'q';
            break;
        default:
            return c;
            break;
    }
}
