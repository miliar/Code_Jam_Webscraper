#include <iostream>
#include <map>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    int c, g, d;
    string texto, texto2;
    char x;
    map<char, char> abc;
    vector<string> cadena;
    ofstream myfile;

    abc['a']='y';
    abc['b']='h';
    abc['c']='e';
    abc['d']='s';
    abc['e']='o';
    abc['f']='c';
    abc['g']='v';
    abc['h']='x';
    abc['i']='d';
    abc['j']='u';
    abc['k']='i';
    abc['l']='g';
    abc['m']='l';
    abc['n']='b';
    abc['o']='k';
    abc['p']='r';
    abc['q']='z';
    abc['r']='t';
    abc['s']='n';
    abc['t']='w';
    abc['u']='j';
    abc['v']='p';
    abc['w']='f';
    abc['x']='m';
    abc['y']='a';
    abc['z']='q';
    abc[' ']=' ';

    cin>>d;
    g=0;
    while(g<=d)
    {
        getline(cin, texto);

        for(c=0; c<texto.size(); c++)
        {
            x=texto[c];
            texto2+=abc[x];
        }
        cadena.push_back(texto2);
        texto2.clear();

        g++;
    }

    myfile.open("output.txt");

    for(g=1; g<=d; g++)
    {
        myfile<<"Case #"<<g<<": "<<cadena[g]<<"\n";
    }

    myfile.close();


    /*Buscar Caracter
    int c;
    char a, b;
    map<char, char> abc;
    for(c=0; c<26; c++)
    {
        cin>>a>>b;
        abc[a]=b;
    }

    map<char, char>::iterator it;

    for(it=abc.begin(); it!=abc.end(); it++)
    {
        cout<<"abc['"<<it->first<<"']='"<<it->second<<"';"<<endl;
    }*/

    return 0;
}
