#include<iostream>
#include<string>
using namespace std;


int main()
{
int n;
cin>>n;
char s[26],ans[30][100],value; string w;
getline(cin,w);
for(int i=0;i<n;i++)
{string q;
	getline(cin,q);int j;	
for( j=0;j<q.length();j++)
{	
switch(char(q.at(j)))
{
case 'a': value='y'; break;
case 'b': value='h'; break;
case 'c': value='e'; break;
case 'd': value='s'; break;
case 'e': value='o'; break;
case 'f': value='c'; break;
case 'g': value='v'; break;
case 'h': value='x'; break;
case 'i': value='d'; break;
case 'j': value='u'; break;
case 'k': value='i'; break;
case 'l': value='g'; break;
case 'm': value='l'; break;
case 'n': value='b'; break;
case 'o': value='k'; break;
case 'p': value='r'; break;
case 'q': value='z'; break;
case 'r': value='t'; break;
case 's': value='n'; break;
case 't': value='w'; break;
case 'u': value='j'; break;
case 'v': value='p'; break;
case 'w': value='f'; break;
case 'x': value='m'; break;
case 'y': value='a'; break;
case 'z': value='q'; break;
case ' ': value=' '; break;

}
ans[i][j]=value;
}
ans[i][j]='\0';ans[i][100]='\0';
}
for(int i=0;i<n;i++)
cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
}
