//Satria Aji Mufatra a.k.a Jim.Kakatata
//satriamufatra@gmail.com

#include <iostream>
#include <fstream>
#include <cstring>
#include <string>

using namespace std;

int main()
{
ifstream in;
in.open("A-small-attempt2.in");

ofstream out;
out.open("aa3.txt");

char x[200];
int cs=0;
in>>cs;

for (int i=0; i<cs; i++)
{
int k=0;
out<<"Case #"<<i+1<<": ";

if (i==0)
in.getline(x, 200);

in.getline(x,200);

while (x[k]!='\0')
{
switch (x[k])
{
case 'y': out<<'a'; break;
case 'n': out<<'b'; break;
case 'f': out<<'c'; break;
case 'i': out<<'d'; break;
case 'c': out<<'e'; break;
case 'w': out<<'f'; break;
case 'l': out<<'g'; break;
case 'b': out<<'h'; break;
case 'k': out<<'i'; break;
case 'u': out<<'j'; break;
case 'o': out<<'k'; break;
case 'm': out<<'l'; break;
case 'x': out<<'m'; break;
case 's': out<<'n'; break;
case 'e': out<<'o'; break;
case 'v': out<<'p'; break;
case 'z': out<<'q'; break;
case 'p': out<<'r'; break;
case 'd': out<<'s'; break;
case 'r': out<<'t'; break;
case 'j': out<<'u'; break;
case 'g': out<<'v'; break;
case 't': out<<'w'; break;
case 'h': out<<'x'; break;
case 'a': out<<'y'; break;
case 'q': out<<'z'; break;

default: out<<' '; break;
}

k++;
}
out<<endl;

}


in.close();
out.close();

return 0;
}
