#include<iostream>
#include<cstdlib>

#include<map>

using namespace std;

map<char,char> letras;

void construirMapa()
{
    letras['a'] = 'y';
    letras['b'] = 'h';
    letras['c'] = 'e';
    letras['d'] = 's';
    letras['e'] = 'o';
    letras['f'] = 'c';
    letras['g'] = 'v';
    letras['h'] = 'x';
    letras['i'] = 'd';
    letras['j'] = 'u';
    letras['k'] = 'i';
    letras['l'] = 'g';
    letras['m'] = 'l';
    letras['n'] = 'b';
    letras['o'] = 'k';
    letras['p'] = 'r';
    letras['q'] = 'z';
    letras['r'] = 't';
    letras['s'] = 'n';
    letras['t'] = 'w';
    letras['u'] = 'j';
    letras['v'] = 'p';
    letras['w'] = 'f';
    letras['x'] = 'm';
    letras['y'] = 'a';
    letras['z'] = 'q';
    letras[' '] = ' ';
}

int main()
{
    //char rta[101];
    string pal;
    construirMapa();
    //cout<<letras['t'];

    int t;
    scanf("%d", &t);
    cin.ignore();
    for (int j=1; j<=t; j++)
    {
        getline(cin,pal);

        cout<<"Case #"<<j<<": ";
        for ( int i=0; i<pal.size(); i++)
        {
            cout<<letras[pal[i]];
        }
        cout<<endl;
    }

    return 0;
}
