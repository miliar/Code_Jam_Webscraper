#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    string G;
    string S;
    int T;
    ofstream salida;
    ifstream entrada;
    entrada.open("A-small-attempt0.in");
    salida.open("exit.txt");
    
    entrada>> T;
    entrada.ignore();
    
    for(int i=0; i<T; i++)
    {
        S="";
        getline(entrada, G);
        for(int j=0; j< G.size(); j++)
        {
            if(G[j] == ' ')
               S+=' ';
            else if(G[j] == 'a')
               S+='y';
            else if(G[j] == 'b')
               S+='h';
            else if(G[j] == 'c')
               S+='e';
            else if(G[j] == 'd')
               S+='s';
            else if(G[j] == 'e')
               S+='o';
            else if(G[j] == 'f')
               S+='c';
            else if(G[j] == 'g')
               S+='v';
            else if(G[j] == 'h')
               S+='x';
            else if(G[j] == 'i')
               S+='d';
            else if(G[j] == 'j')
               S+='u';
            else if(G[j] == 'k')
               S+='i';
            else if(G[j] == 'l')
               S+='g';
            else if(G[j] == 'm')
               S+='l';
            else if(G[j] == 'n')
               S+='b';
            else if(G[j] == 'o')
               S+='k';
            else if(G[j] == 'p')
               S+='r';
            else if(G[j] == 'q')
               S+='z';
            else if(G[j] == 'r')
               S+='t';
            else if(G[j] == 's')
               S+='n';
            else if(G[j] == 't')
               S+='w';
            else if(G[j] == 'u')
               S+='j';
            else if(G[j] == 'v')
               S+='p';
            else if(G[j] == 'w')
               S+='f';
            else if(G[j] == 'x')
               S+='m';
            else if(G[j] == 'y')
               S+='a';
            else if(G[j] == 'z')
               S+='q';
        }
        
        salida << "Case #" <<i+1 << ": " << S <<endl;    
    }
    
    salida.close();
    return 0;    
}
