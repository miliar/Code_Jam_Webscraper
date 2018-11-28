#include <fstream>
#include <iostream>
#include <map>

using namespace std;

int main() {

    map<char, char> to;
    to['a'] = 'y';
    to['b'] = 'h';
    to['c'] = 'e';
    to['d'] = 's';
    to['e'] = 'o';
    to['f'] = 'c';
    to['g'] = 'v';
    to['h'] = 'x';
    to['i'] = 'd';
    to['j'] = 'u';
    to['k'] = 'i';
    to['l'] = 'g';
    to['m'] = 'l';
    to['n'] = 'b';
    to['o'] = 'k';
    to['p'] = 'r';
    to['q'] = 'z';
    to['r'] = 't';
    to['s'] = 'n';
    to['t'] = 'w';
    to['u'] = 'j';
    to['v'] = 'p';
    to['w'] = 'f';
    to['y'] = 'a';
    to['x'] = 'm';
    to['z'] = 'q';



    ifstream in("/home/am/Downloads/A-small-attempt1.in", ifstream::in);
    ofstream out("/home/am/Downloads/A-small-attempt1.out", ofstream::out);

    int n = 0, _count = 0; in >> n;
    string temp;
    in.ignore();
    while(getline(in, temp) && _count < n){
        out << "Case #" << (_count + 1) << ": ";
        for(string::iterator i = temp.begin(); i < temp.end(); ++i){
            if(*i != ' ') out << to[*i];
            else out << *i;
        }
        ++_count;
        out << endl;
    }


    return 0;
}

