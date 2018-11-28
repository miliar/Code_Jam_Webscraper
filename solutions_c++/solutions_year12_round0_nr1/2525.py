#include <iostream>
#include <map>
#include <fstream>
using namespace std;

int main(int argc, char** argv) {
    if (argc < 2) { 
        cout << "Usage " << argv[0] << " <input file>" << endl;
        return 1;
    }

    int cases;
    char line[256];

    map <char,int> charMap;
    charMap['a'] = 'y';
    charMap['b'] = 'h';
    charMap['c'] = 'e';
    charMap['d'] = 's';
    charMap['e'] = 'o';
    charMap['f'] = 'c';
    charMap['g'] = 'v';
    charMap['h'] = 'x';    
    charMap['i'] = 'd';
    charMap['j'] = 'u';
    charMap['k'] = 'i';
    charMap['l'] = 'g';
    charMap['m'] = 'l';
    charMap['n'] = 'b';
    charMap['o'] = 'k';
    charMap['p'] = 'r';    
    charMap['q'] = 'z';
    charMap['r'] = 't';
    charMap['s'] = 'n';
    charMap['t'] = 'w';
    charMap['u'] = 'j';
    charMap['v'] = 'p';
    charMap['w'] = 'f';
    charMap['x'] = 'm';    
    charMap['y'] = 'a';
    charMap['z'] = 'q';
    charMap[' '] = ' ';
    charMap['\n'] = '\n';

    ifstream in(argv[1]);
    in >> cases;
    in.getline(line, 256);
    for (int c=1; c<=cases; c++) { 
        cout << "Case #" << c << ": ";
        in.getline(line, 256);
        for (int i=0; i<100; i++) {  
            line[i] = charMap[line[i]];
        }
        cout << line << endl;
    }
    return 0;
}
