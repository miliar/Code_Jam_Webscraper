#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
void map(char &S)
{ switch(S)
          { case 'a':
                S='y';
                break;
           case 'b':
                S='h';
                break;
           case 'c':
                S='e';
                break;
           case 'd':
                S='s';
                break;
           case 'e':
                S='o';
                break;
           case 'f':
                S='c';
                break;
           case 'g':
                S='v';
                break;
           case 'h':
                S='x';
                break;
           case 'i':
                S='d';
                break;
           case 'j':
                S='u';
                break;
           case 'k':
                S='i';
                break;
           case 'l':
                S='g';
                break;
           case 'm':
                S='l';
                break;
           case 'n':
                S='b';
                break;
           case 'o':
                S='k';
                break;
           case 'p':
                S='r';
                break;
           case 'q':
                S='z';
                break;
           case 'r':
                S='t';
                break;
           case 's':
                S='n';
                break;
           case 't':
                S='w';
                break;
           case 'u':
                S='j';
                break;
           case 'v':
                S='p';
                break;
           case 'w':
                S='f';
                break;
           case 'x':
                S='m';
                break;
           case 'y':
                S='a';
                break;
           case 'z':
                S='q';
                break;    
                }
 }
int main(int argc, char *argv[])
{
    ifstream in("A-small-attempt2.in");
    ofstream out("out.txt");
    char S;
    int T;
    in>>T;
    in.get(S);
    for(int i=0;i<T;i++)
    {
                 out<<"Case #"<<i+1<<": ";
                do
                 {           
                 in.get(S);                   
                 map(S);
                 out<<S;                 
                 }while(S!='\n');
                 }
                 in.close();
                 out.close();
    system("PAUSE");
    return EXIT_SUCCESS;
}
