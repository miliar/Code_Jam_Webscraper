#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(int argc, char** argv) {
    map<char,char> translator;
    translator['a'] = 'y';
    translator['b'] = 'h';
    translator['c'] = 'e';
    translator['d'] = 's';
    translator['e'] = 'o';
    translator['f'] = 'c';
    translator['g'] = 'v';
    translator['h'] = 'x';
    translator['i'] = 'd';
    translator['j'] = 'u';
    translator['k'] = 'i';
    translator['l'] = 'g';
    translator['m'] = 'l';
    translator['n'] = 'b';
    translator['o'] = 'k';
    translator['p'] = 'r';
    translator['q'] = 'z';
    translator['r'] = 't';
    translator['s'] = 'n';
    translator['t'] = 'w';
    translator['u'] = 'j';
    translator['v'] = 'p';
    translator['w'] = 'f';
    translator['x'] = 'm';
    translator['y'] = 'a';
    translator['z'] = 'q';
    translator[' '] = ' ';
    int num_lines;
    char input_line[300];
    cin >> num_lines;
    cin.getline(input_line,300);
    for(int i = 1; i <=num_lines; ++i) {
        cout << "Case #" << i << ": ";
        cin.getline(input_line, 300);
        string temp_line = input_line;
        string::iterator it;
        for(it = temp_line.begin(); it < temp_line.end(); ++it) {
            cout << translator[(*it)];
        }
        //loop the character array
        cout << endl;
    }
    return 0;
}
