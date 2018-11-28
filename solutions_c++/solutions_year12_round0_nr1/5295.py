#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int main(int argc, char * )
{
    int n, i,j;    
    map<char,char> tr;
    char line[110];
    char out[110];
    
    tr['a']='y';
    tr['b']='h';
    tr['c']='e';
    tr['d']='s';
    tr['e']='o';
    tr['f']='c';
    tr['g']='v';
    tr['h']='x';
    tr['i']='d';
    tr['j']='u';
    tr['k']='i';
    tr['l']='g';
    tr['m']='l';
    tr['n']='b';
    tr['o']='k';
    tr['p']='r';
    tr['r']='t';
    tr['s']='n';
    tr['t']='w';
    tr['u']='j';
    tr['v']='p';
    tr['w']='f';
    tr['x']='m';
    tr['y']='a';
    tr['z']='q';
    tr['q']='z';
    
    cin >> n;
    cin.getline(line,1);
    for (i=0;i<n;++i)
    {
          cin.getline(line, 110);
          char *ch, *cho, cht;
          for (ch=line, cho=out; *ch; ++ch, ++cho)
             *cho = (cht = tr[*ch]) ? cht : *ch;
          *cho = 0;
          cout << "Case #" << i+1 << ": " << out << endl;
    }  
    return 0;
}
