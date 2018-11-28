#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string>
#include<map>

using namespace std;

int main()

{
int t;

cin>>t;

map<char,char> mapa;
map <char, char> :: iterator i;
mapa['y']='a';
mapa['n']='b';
mapa['f']='c';
mapa['i']='d';
mapa['c']='e';
mapa['w']='f';
mapa['l']='g';
mapa['b']='h';
mapa['k']='i';
mapa['u']='j';
mapa['o']='k';
mapa['x']='m';
mapa['s']='n';
mapa['p']='r';
mapa['e']='o';
mapa['v']='p';
mapa['g']='v';
mapa['p']='r';
mapa['m']='l';
mapa['d']='s';
mapa['r']='t';
mapa['j']='u';
mapa['t']='w';
mapa['h']='x';
mapa['a']='y';
mapa['q']='z';
mapa['z']='q';
mapa[' ']=' ';

int x=1;

string g;
getline(cin,g);
for(int k=1; k<=t;k++)

{

    getline(cin,g);

cout<< "Case #"<<x<<": ";
x++;
for(int c=0; c< g.size();c++)
{

cout<<mapa.find(g[c])->second;

    }
cout<<endl;
}



}

