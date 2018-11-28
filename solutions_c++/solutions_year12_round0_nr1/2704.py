//Christopher Mueller
//Made for Google Code Jam 2012

#include <map>
#include <fstream>
#include <cstring>

using namespace std;

int main()
{
    map <char, char> m;
    m['a'] = 'y';
    m['b'] = 'h';
    m['c'] = 'e';
    m['d'] = 's';
    m['e'] = 'o';
    m['f'] = 'c';
    m['g'] = 'v';
    m['h'] = 'x';
    m['i'] = 'd';
    m['j'] = 'u';
    m['k'] = 'i';
    m['l'] = 'g';
    m['m'] = 'l';
    m['n'] = 'b';
    m['o'] = 'k';
    m['p'] = 'r';
    m['q'] = 'z';
    m['r'] = 't';
    m['s'] = 'n';
    m['t'] = 'w';
    m['u'] = 'j';
    m['v'] = 'p';
    m['w'] = 'f';
    m['x'] = 'm';
    m['y'] = 'a';
    m['z'] = 'q';
    m[' '] = ' ';

    char buf[1000];

    ifstream infile("A-small-attempt0.in");
    int T;
    infile >> T;
    infile.getline(buf, 1000); //remove the newline after T

    ofstream outfile("output.txt");
    for(int i = 0; i < T; ++i)
    {
        outfile << "Case #" << i + 1 << ": ";
        infile.getline(buf, 1000);

        unsigned size = strlen(buf);
        for(unsigned i = 0; i < size; ++i)
            buf[i] = m[buf[i]];

        outfile << buf << endl;
    }

    return 0;
}
