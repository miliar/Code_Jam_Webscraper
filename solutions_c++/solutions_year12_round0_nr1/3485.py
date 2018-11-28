#include <iostream>
#include <stdio.h>
#include <sstream>
#include <cmath>
using namespace std;

int main() {
int test;
freopen("A.in", "r", stdin);
freopen("aout.txt", "w", stdout);
cin>>test;
char junk[100];
cin.getline(junk,100);
for(int i=1;i<=test;i++)
{
cout<<"Case #"<<i<<": ";
char s[256];
cin.getline(s,256);

for(int j=0;s[j]!='\0';j++)
{
switch(s[j])
{
case 'y':cout<<'a';break;
case 'n':cout<<'b';break;
case 'f':cout<<'c';break;
case 'i':cout<<'d';break;
case 'c':cout<<'e';break;
case 'w':cout<<'f';break;
case 'l':cout<<'g';break;
case 'b':cout<<'h';break;
case 'k':cout<<'i';break;
case 'u':cout<<'j';break;
case 'o':cout<<'k';break;
case 'm':cout<<'l';break;
case 'x':cout<<'m';break;
case 's':cout<<'n';break;
case 'e':cout<<'o';break;
case 'v':cout<<'p';break;
case 'z':cout<<'q';break;
case 'p':cout<<'r';break;
case 'd':cout<<'s';break;
case 'r':cout<<'t';break;
case 'j':cout<<'u';break;
case 'g':cout<<'v';break;
case 't':cout<<'w';break;
case 'h':cout<<'x';break;
case 'a':cout<<'y';break;
case 'q':cout<<'z';break;
case ' ':cout<<' ';break;

}
}
cout<<endl;
}
	return 0;
}
