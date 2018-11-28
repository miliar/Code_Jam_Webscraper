
#include <iostream>
#include <fstream>
#include <math.h>
#include<vector>
#include<map>
#include<list>
// #include <conio.h>

using namespace std;

const int MAX  = 5001;

struct interval 
{
       interval(int b, int e, int ev):
                    begin(b),
                    end(e),
                    even(ev){}
       int begin;
       int end;
       int even;
};

int main()
{
    ifstream cin("in.in");
    ofstream cout("out.out");
    
    map<char, char> m;
    m[' ']=' ';
    m['a']='y';
    m['b']='h';
    m['c']='e';
    m['d']='s';
    m['e']='o';
    m['f']='c';
    m['g']='v';
    m['h']='x';
    m['i']='d';
    m['j']='u';
    m['k']='i';
    m['l']='g';
    m['m']='l';
    m['n']='b';
    m['o']='k';
    m['p']='r';
    m['q']='z';
    m['r']='t';
    m['s']='n';
    m['t']='w';
    m['u']='j';
    m['v']='p';
    m['w']='f';
    m['x']='m';
    m['y']='a';
    m['z']='q';
    
    int t;
    cin >> t;
    cin.get();
    for (int ind = 1; ind <= t; ind++) {
        char line[101];
        cin.getline(line, 101);
        cout << "Case #" << ind << ": ";
        for(int i = 0; i < strlen(line); i++) {
                cout << m[line[i]];
        }
        
        cout << endl;
    }
        
   // getch();
    return 0;
}
