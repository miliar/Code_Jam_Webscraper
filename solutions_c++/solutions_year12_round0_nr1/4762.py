#include <stdio.h>
#include <iostream>

using namespace std;

char DIC[400];





int main()
{
DIC['a']='y';
DIC['b']='h';
DIC['c']='e';
DIC['d']='s';
DIC['e']='o';
DIC['f']='c';
DIC['g']='v';
DIC['h']='x';
DIC['i']='d';
DIC['j']='u';
DIC['k']='i';
DIC['l']='g';
DIC['m']='l';
DIC['n']='b';
DIC['o']='k';
DIC['p']='r';
DIC['q']='z';
DIC['r']='t';
DIC['s']='n';
DIC['t']='w';
DIC['u']='j';;
DIC['v']='p';
DIC['w']='f';
DIC['x']='m';
DIC['y']='a';
DIC['z']='q';
DIC[' ']=' ';
int n;
cin>> n;

    char tmp;
    cin.get(tmp);
char linea[200];
for (int i=0;i<n;i++)
{
    char nuevaLinea[200];
    cin.getline(linea,110);
    int j;
    for( j=0;j<strlen(linea);j++)
    {
        nuevaLinea[j]=DIC[linea[j]];
    }
    nuevaLinea[j]=0;
    cout << "Case #"<< i+1 <<": "<< nuevaLinea<< endl;
}

    return 0;
    
}
