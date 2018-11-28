#include <iostream>
#include <string>

using namespace::std;

char convertir(char a)
{
    switch (a)
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
        case ' ': return ' '; break;
        default: return '-'; break;
    }
}

int main()
{
    int n,i,m;
    string frase="";
    string conversion="";
    cin>>n;
    int a=0;
    while(n>=0)
    {
        getline(cin,frase);
        m=(int)frase.size();
        if(m>0)
        {
            for(i=0;i<m;i++)
            {
                conversion=conversion+convertir(frase[i]);
            }
            cout<<"Case #"<<a+1<<": "<<conversion;
            if(n>0)
            {
                cout<<endl;
            }
            a++;
        }
        conversion="";
        n--;
    }
    return 0;
}
