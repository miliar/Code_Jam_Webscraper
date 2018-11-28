#include <iostream>
#include <stdio.h>
#include <string>
#include <map>

using namespace std;
map <char,char> letras;


int main()
{
    letras['a']='y';
letras['b']='h';
letras['c']='e';
letras['d']='s';
letras['e']='o';
letras['f']='c';
letras['g']='v';
letras['h']='x';
letras['i']='d';
letras['j']='u';
letras['k']='i';
letras['l']='g';
letras['m']='l';
letras['n']='b';
letras['o']='k';
letras['p']='r';
letras['q']='z';
letras['r']='t';
letras['s']='n';
letras['t']='w';
letras['u']='j';
letras['v']='p';
letras['w']='f';
letras['x']='m';
letras['y']='a';
letras['z']='q';
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tt;
    cin>>tt;
    getchar();
    for(int cont=0; cont<tt; cont++){
        string parrafo;
        getline(cin, parrafo);
        cout<<"Case #"<<cont+1<<": ";
        for(int cont2=0; cont2<parrafo.length(); cont2++){
            if(parrafo[cont2]!= ' '){
                cout<<letras[parrafo[cont2]];
            }else{
                cout<<" ";
            }
        }
        cout<<endl;
    }

    return 0;
}
