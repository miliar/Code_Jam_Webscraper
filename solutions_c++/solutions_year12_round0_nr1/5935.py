#include "util.h"

int main()
{
    char m[256];
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

    ifstream in("in");

    int n;
    in >> n;
    in.get();

    for(int c=1;c<=n;++c) {
        char line[128];
        in.getline(line, 128);
        int len = strlen(line);

        dump << "Case #" << c << ": ";
        for(int j=0;j<len;++j) {
            if(line[j] == ' ')
                dump << ' ';
            else
                dump << m[line[j]];
        }
        dump << endl;
    }
    return 0;
}
