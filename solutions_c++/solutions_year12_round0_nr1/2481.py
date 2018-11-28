#include <iostream>
#include <cstdio>
#include <map>
using namespace std;
#define ELMATI
map<char, char> dicc;

int main(){
dicc['a']= 'y';
dicc['b']= 'h';
dicc['c']= 'e';
dicc['d']= 's';
dicc['e']= 'o';
dicc['f']= 'c';
dicc['g']= 'v';
dicc['h']= 'x';
dicc['i']= 'd';
dicc['j']= 'u';
dicc['k']= 'i';
dicc['l']= 'g';
dicc['m']= 'l';
dicc['n']= 'b';
dicc['o']= 'k';
dicc['p']= 'r';
dicc['q']= 'z';
dicc['r']= 't';
dicc['s']= 'n';
dicc['t']= 'w';
dicc['u']= 'j';
dicc['v']= 'p';
dicc['w']= 'f';
dicc['x']= 'm';
dicc['y']= 'a';
dicc['z']= 'q';
dicc[' ']= ' ';
#ifdef ELMATI
    freopen("A-small-attempt0.out","w",stdout);
    freopen("A-small-attempt0.in","r",stdin);
#endif
    string p;
   int tot;
    cin >> tot;
    int w = 1;
    getline(cin,p);
    while (tot > 0) {
        getline(cin,p);
        cout << "Case #" << w << ": ";
        for (unsigned int i=0; i<p.length(); i++) {
            cout << dicc[p[i]];
        }
        cout << "\n";
        tot--;
        w++;
    }
    return 0;
}
