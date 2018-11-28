#include<fstream>
#include<iostream>
#include<string>

using namespace std;

char switchLetter(char x)
{
 switch(x)
 {
 case 'a': return 'y'; break;
 case 'b': return 'h'; break;
 case 'c': return 'e'; break;
 case 'd': return 's'; break;
 case 'e': return 'o'; break;
 case 'f': return 'c'; break;
 case 'g': return 'v'; break;
 case 'h': return 'x'; break;
 case 'i': return 'd'; break;
 case 'j': return 'u'; break;
 case 'k': return 'i'; break;
 case 'l': return 'g'; break;
 case 'm': return 'l'; break;
 case 'n': return 'b'; break;
 case 'o': return 'k'; break;
 case 'p': return 'r'; break;
 case 'q': return 'z'; break;
 case 'r': return 't'; break;
 case 's': return 'n'; break;
 case 't': return 'w'; break;
 case 'u': return 'j'; break;
 case 'v': return 'p'; break;
 case 'w': return 'f'; break;
 case 'x': return 'm'; break;
 case 'y': return 'a'; break;
 case 'z': return 'q'; break;
 }
}

string English(string x)
{
 string r;
 for(int i=0;i<x.length();i++)
  r+=switchLetter(x[i]);

 return r;
}

int main()
{
 ifstream in("A-small-attempt0.in");
 ofstream out("output.txt");

 int testCases;
 string line[30],dummy;

 in>>testCases;
 getline(in,dummy);
 for(int i=0;i<testCases;i++)
 {
  getline(in,line[i]);
  out<<"Case #"<<i+1<<": "<<English(line[i])<<endl;
 }

 cin>>testCases;
 return 0;
}