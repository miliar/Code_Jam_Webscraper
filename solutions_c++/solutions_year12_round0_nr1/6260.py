#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>

using namespace std;

int main() {
    int T,tc;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cin >> T;

    scanf("%*c");
    map <char, char> m;
    m[' '] = ' ';
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
    for(int tc = 1 ; tc <= T ; tc++) {
        char ch;
        cout << "Case #" << tc << ": ";
        scanf("%c",&ch);
        while(ch != '\n') {
            cout << m[ch];
            scanf("%c",&ch);
        }
        cout << endl;
    }
    return (0);
}
