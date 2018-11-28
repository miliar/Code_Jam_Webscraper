#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <iomanip>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <bitset>
#include <fstream>

#define SZ(n) (int)n.size()
#define PB(n) push_back(n)

using namespace std;

int main ()
{
    ifstream input("A-small-attempt0.in.txt");
    ofstream output("out");
    
    string line;
    
    map<char, char> tr;
    
    tr['a'] = 'y';
    tr['b'] = 'h';
    tr['c'] = 'e';
    tr['d'] = 's';
    tr['e'] = 'o';
    tr['f'] = 'c';
    tr['g'] = 'v';
    tr['h'] = 'x';
    tr['i'] = 'd';
    tr['j'] = 'u';
    tr['k'] = 'i';
    tr['l'] = 'g';
    tr['m'] = 'l';
    tr['n'] = 'b';
    tr['o'] = 'k';
    tr['p'] = 'r';
    tr['q'] = 'z';
    tr['r'] = 't';
    tr['s'] = 'n';
    tr['t'] = 'w';
    tr['u'] = 'j';
    tr['v'] = 'p';
    tr['w'] = 'f';
    tr['x'] = 'm';
    tr['y'] = 'a';
    tr['z'] = 'q';
    tr[' '] = ' ';
    
    
    int t; input >> t;
    getline(input, line); // \n
    
    for (int cs = 1; cs <= t; cs++) {
        getline(input, line);
        output << "Case #" << cs << ": ";
        for (int i = 0; i < line.length(); i++) {
            output << tr[line[i]];
        }
        output << endl;
    }
    
    output.close();
    input.close();
    
    return 0;
}

