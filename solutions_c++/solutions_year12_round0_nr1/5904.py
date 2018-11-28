#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<char,char> Conv;
    Conv['y'] = 'a';
    Conv['n'] = 'b';
    Conv['f'] = 'c';
    Conv['i'] = 'd';
    Conv['c'] = 'e';
    Conv['w'] = 'f';
    Conv['l'] = 'g';
    Conv['b'] = 'h';
    Conv['k'] = 'i';
    Conv['u'] = 'j';
    Conv['o'] = 'k';
    Conv['m'] = 'l';
    Conv['x'] = 'm';
    Conv['s'] = 'n';
    Conv['e'] = 'o';
    Conv['v'] = 'p';
    Conv['z'] = 'q';
    Conv['p'] = 'r';
    Conv['d'] = 's';
    Conv['r'] = 't';
    Conv['j'] = 'u';
    Conv['g'] = 'v';
    Conv['t'] = 'w';
    Conv['h'] = 'x';
    Conv['a'] = 'y';
    Conv['q'] = 'z';
    Conv[' '] = ' ';
    
    string input, output;
    char c;
    int n,i,j,panjang;
    scanf("%d\n",&n);
    for (j=1;j<=n;j++) {
        getline(cin,input);
        panjang = input.length();
        cout << "Case #" << j << ": ";
        for (i=0; i<panjang; i++) {
            c = input[i];
            cout << Conv[c];
        }
        cout << endl;
    }
}
