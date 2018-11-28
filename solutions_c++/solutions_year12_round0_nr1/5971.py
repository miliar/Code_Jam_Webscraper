#include <iostream>
#include <fstream>
#include <map>

using namespace std;

map<char, char> mapping;

int main() {
    char fl[] = "googlerese.in";
    char ofl[] = "googlerese.out";

    mapping['a'] = 'y';
    mapping['b'] = 'h';
    mapping['c'] = 'e';
    mapping['d'] = 's';
    mapping['e'] = 'o';
    mapping['f'] = 'c';
    mapping['g'] = 'v';
    mapping['h'] = 'x';
    mapping['i'] = 'd';
    mapping['j'] = 'u';
    mapping['k'] = 'i';
    mapping['l'] = 'g';
    mapping['m'] = 'l';
    mapping['n'] = 'b';
    mapping['o'] = 'k';
    mapping['p'] = 'r';
    mapping['q'] = 'z';
    mapping['r'] = 't';
    mapping['s'] = 'n';
    mapping['t'] = 'w';
    mapping['u'] = 'j';
    mapping['v'] = 'p';
    mapping['w'] = 'f';
    mapping['x'] = 'm';
    mapping['y'] = 'a';
    mapping['z'] = 'q';

    ifstream input(fl);
    ofstream output(ofl);
    int T;
    input>>T;
    input.ignore();
    for(int i = 0; i<T; i++) {
        char buffer[200];
        input.getline(buffer, 200);

        for(int j = 0; buffer[j]; j++) {
            if(buffer[j]!=' ')
                buffer[j] = mapping[buffer[j]];
        }
        output<<"Case #"<<(i+1)<<": "<<buffer<<"\n";
    }

    output.close();
    input.close();

    return 0;
}
