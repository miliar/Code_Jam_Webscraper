#include <sstream>
#include <iostream>
#include <fstream>
#include <string>
#include <list>

using namespace std;

ifstream in("B-large.in");
ofstream out("B.out");

list<char> numeros;
list<char>::iterator it;
char N[22];
int T;

int main()
{
    int X, indice;
    char numeroActual;
    
    in>>T;
    for (X=1; X<=T; X++)
    {
        in>>N;
        indice = -1;
        for (int i=strlen(N)-2; i>=0; i--)
        {
            for (int j=i+1; j<strlen(N); j++)
            {
                if (N[i]<N[j])
                {
                    indice = i;
                    break;
                }
            }
            if (indice >= 0)
                break;
        }

        for (int i=indice+1; i<strlen(N); i++)
            numeros.push_back(N[i]);
        numeros.sort();

        if (indice >= 0)
            numeroActual = N[indice];
        else
        {
            numeroActual = '0';
            indice = 0;
        }

        for (it=numeros.begin(); it!=numeros.end(); it++)
            if (*it > numeroActual)
            {
                N[indice++]=(*it);
                numeros.erase(it);
                break;
            }

        numeros.push_back(numeroActual);
        numeros.sort();

        for (it=numeros.begin(); it!=numeros.end(); )
        {
            N[indice++]=(*it);
            it = numeros.erase(it);
        }

        N[indice++]='\0';
        
        out<<"Case #"<<X<<": "<<N<<endl;
    }
    return EXIT_SUCCESS;
}
