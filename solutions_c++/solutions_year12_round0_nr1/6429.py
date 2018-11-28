#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
char translate(char ch)
{
    switch(ch)
    {
                case 'a': return('y');
                         break; 
                case 'b': return('h');
                         break; 
                case 'c': return('e');
                         break; 
                case 'd': return('s');
                         break; 
                case 'e': return('o');
                         break; 
                case 'f': return('c');
                         break; 
                case 'g': return('v');
                         break; 
                case 'h': return('x');
                         break; 
                case 'i': return('d');
                         break; 
                case 'j': return('u');
                         break; 
                case 'k': return('i');
                         break; 
                case 'l': return('g');
                         break; 
                case 'm': return('l');
                         break; 
                case 'n': return('b');
                         break; 
                case 'o': return('k');
                         break; 
                case 'p': return('r');
                         break; 
                case 'q': return('z');
                         break; 
                case 'r': return('t');
                         break; 
                case 's': return('n');
                         break; 
                case 't': return('w');
                         break; 
                case 'u': return('j');
                         break; 
                case 'v': return('p');
                         break; 
                case 'w': return('f');
                         break; 
                case 'x': return('m');
                         break; 
                case 'y': return('a');
                         break; 
                case 'z': return('q');
                         break; 
                default: return(ch);
                         break;
    }
}
                                                       
int main()
{
    int t, i, j;
	char str[30][101], dummy[30];
	cin>>t;
	gets(dummy);
	for(i=0; i<t; i++)
	{
             gets(str[i]);
    }
    for(i=0; i<t; i++)
    {
             for(j=0; j<strlen(str[i]); j++)
             {
                      str[i][j]=translate(str[i][j]);
                      }
             cout<<"\nCase #"<<i+1<<": "<<str[i];

    }
    cin>>t;
    return(0);
}

    
    
             
	
