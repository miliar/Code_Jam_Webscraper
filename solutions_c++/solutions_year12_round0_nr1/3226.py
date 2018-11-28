#include <iostream>
#include <fstream>

using namespace std;

char trans [256];

void init ()
{
    trans ['a'] = 'y';
    trans ['b'] = 'h';
    trans ['c'] = 'e';
    trans ['d'] = 's';
    trans ['e'] = 'o';
    trans ['f'] = 'c';
    trans ['g'] = 'v';
    trans ['h'] = 'x';
    trans ['i'] = 'd';
    trans ['j'] = 'u';
    trans ['k'] = 'i';
    trans ['l'] = 'g';
    trans ['m'] = 'l';
    trans ['n'] = 'b';
    trans ['o'] = 'k';
    trans ['p'] = 'r';
    trans ['q'] = 'z';
    trans ['r'] = 't';
    trans ['s'] = 'n';
    trans ['t'] = 'w';
    trans ['u'] = 'j';
    trans ['v'] = 'p';
    trans ['w'] = 'f';
    trans ['x'] = 'm';
    trans ['y'] = 'a';
    trans ['z'] = 'q';
}

int main()
{
    ifstream in ("input.txt");
    ofstream out ("code.txt");

    int T;
    string s;

    init ();

    in >> T;
    getline (in, s);
    for (int i=1; i <= T; i++) {
        out << "Case #" << i << ": ";
        getline (in, s);
        for (size_t i=0; i < s.length (); i++) {
            if (s [i] == ' ') out << " "; else out << trans [s [i]];
        }
        out << endl;
    }

    return 0;
}
