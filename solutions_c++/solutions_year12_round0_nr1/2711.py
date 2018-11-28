#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <vector>
using namespace std;

#define MAX_TAM 501   //500 caracteres + el terminador (no se me pasa una)
#define CANT_LETRAS 26
#define ES_LETRA(let) ( ('a' <= let&&let <= 'z') || ('A' <= let&&let <= 'Z') )

int main()
{
    char dec[256];
    dec[' ']=' ';
    dec['y']='a';
    dec['n']='b';
    dec['f']='c';
    dec['i']='d';
    dec['c']='e';
    dec['w']='f';
    dec['l']='g';
    dec['b']='h';
    dec['k']='i';
    dec['u']='j';
    dec['o']='k';
    dec['m']='l';
    dec['x']='m';
    dec['s']='n';
    dec['e']='o';
    dec['v']='p';
    dec['z']='q';
    dec['p']='r';
    dec['d']='s';
    dec['r']='t';
    dec['j']='u';
    dec['g']='v';
    dec['t']='w';
    dec['h']='x';
    dec['a']='y';
    dec['q']='z';
    dec['\n']='\n';
    dec['\0']='\0';
    ifstream in("A-small-attempt0.in");
    ofstream out("ans.out");
    int n;
    in >> n;
        in.ignore(50, '\n');
    for(int i=0; i<n; i++){
        out << "Case #" << i+1 << ": ";
        char texto[200];//idem
        in.getline(texto, sizeof(texto));

        char *fin=strlen(texto)+texto;
        for(char *cur=texto; cur<fin; cur++){   //Decodifica caracter por caracter

                //Hay que decodificarla
                out.put(dec[*cur]);
        }
        out << endl;
        texto[0]='\0';

    }

    return 0;
}
