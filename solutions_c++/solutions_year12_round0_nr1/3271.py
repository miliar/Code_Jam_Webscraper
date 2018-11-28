#include<iostream.h>
#include<fstream.h>
#include<string.h>
#include<stdio.h>

char change(char ch)
{
 switch(ch)
 {
  case 'a': return 'y';
case 'b': return 'h';
case 'c': return 'e';
case 'd': return 's';
case 'e': return 'o';
case 'f': return 'c';
case 'g': return 'v';
case 'h': return 'x';
case 'i': return 'd';
case 'j': return 'u';
case 'k': return 'i';
case 'l': return 'g';
case 'm': return 'l';
case 'n': return 'b';
case 'o': return 'k';
case 'p': return 'r';
case 'q': return 'z';
case 'r': return 't';
case 's': return 'n';
case 't': return 'w';
case 'u': return 'j';
case 'v': return 'p';
case 'w': return 'f';
case 'x': return 'm';
case 'y': return 'a';
case 'z': return 'q';
 }
return ' ';


}

int main()
{
ifstream fin;ofstream fout;
fin.open("data.in",ios::in);
fout.open("data.out",ios::out);

char ch;
int t;
fin>>t;
fin.get(ch);
for(int i=0;i<t;i++)
{
 fout<<"Case #"<<(i+1)<<": ";

                fin.get(ch);
                do
                {
                  fout<<change(ch);
                  fin.get(ch);
                }while(ch!='\n' || fin.eof());

                fout<<endl;

}

}