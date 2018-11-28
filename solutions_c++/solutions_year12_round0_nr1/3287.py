#include <iostream>
#include <map>
using namespace std;

int main()
{
    size_t tests;
    cin >> tests;
    map<char, char> trans;
        trans['y']='a';
        trans['n']='b';
        trans['f']='c';
        trans['i']='d';
        trans['c']='e';
        trans['w']='f';
        trans['l']='g';
        trans['b']='h';
        trans['k']='i';
        trans['u']='j';
        trans['o']='k';
        trans['m']='l';
        trans['x']='m';
        trans['s']='n';
        trans['e']='o';
        trans['v']='p';
        trans['z']='q';
        trans['p']='r';
        trans['d']='s';
        trans['r']='t';
        trans['j']='u';
        trans['g']='v';
        trans['t']='w';
        trans['h']='x';
        trans['a']='y';
        trans['q']='z';
        char x[10];
    cin.getline(x, 10);
    for(size_t i = 1;i<=tests; ++i){
        char BUFF[111];
        cin.getline(BUFF,110);
        cout << "Case #" << i << ": ";
        for (int i=0; i<cin.gcount(); ++i){
            if (BUFF[i]==' ') cout << ' ';
            else cout << trans[BUFF[i]];
        }
        cout << endl;

    }
    return 0;
}
