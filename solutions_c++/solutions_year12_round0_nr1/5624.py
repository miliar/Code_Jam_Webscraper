#include <iostream>
#include <string>
#include <map>
#include <fstream>


using namespace std;


void napolni(map<char, char>&);

int main()
{
    map<char, char> kom;
    napolni(kom);
    int n;
    ifstream fin ("input.in");
    ofstream fout("output.out");
    fin >> n;
    for (int i=0; i<=n; ++i)
    {
        string temp;
        getline(fin, temp );
        for (string::iterator it=temp.begin(); it!=temp.end(); ++it)
            *it=kom[*it];
        fout << "Case #" << i << ": " << temp << endl;
        cout << "Case #" << i << ": " << temp << endl;
    }
    return 0;
}

void napolni(map<char, char>& mapa)
{
    mapa['a']='y'; mapa['b']='h'; mapa['c']='e'; mapa['d']='s'; mapa['e']='o';
    mapa['f']='c'; mapa['g']='v'; mapa['h']='x'; mapa['i']='d'; mapa['j']='u';
    mapa['k']='i'; mapa['l']='g'; mapa['m']='l'; mapa['n']='b'; mapa['o']='k';
    mapa['p']='r'; mapa['q']='z'; mapa['r']='t'; mapa['s']='n'; mapa['t']='w';
    mapa['u']='j'; mapa['v']='p'; mapa['w']='f'; mapa['x']='m'; mapa['y']='a';
    mapa['z']='q'; mapa[' ']=' ';
}
