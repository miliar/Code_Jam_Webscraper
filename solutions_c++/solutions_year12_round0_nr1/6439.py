#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <vector>
using namespace std;
int main()
{
    FILE *in = fopen( "A-small-attempt0.in" , "r" );
    FILE *out = fopen( "A-small-attempt0.out" , "w" );
    int tcases;
    fscanf( in , "%d", &tcases );
    char garb;
    fscanf( in , "%c",&garb);
    string line="";
    for(int t=1;t<=tcases;t++)
    {
            fprintf(out , "Case #%d: ",t);
            line="";
            while(true){
            char z;
            fscanf( in , "%c", &z );
            if(z=='\n')break;
            line +=z;
            }
            for(int i=0;i<line.length();i++)
            {
                switch(line[i])
                {
                    case 'a': fprintf( out , "y");break;
                    case 'b': fprintf( out , "h");break;
                    case 'c': fprintf( out , "e");break;
                    case 'd': fprintf( out , "s");break;
                    case 'e': fprintf( out , "o");break;
                    case 'f': fprintf( out , "c");break;
                    case 'g': fprintf( out , "v");break;
                    case 'h': fprintf( out , "x");break;
                    case 'i': fprintf( out , "d");break;
                    case 'j': fprintf( out , "u");break;
                    case 'k': fprintf( out , "i");break;
                    case 'l': fprintf( out , "g");break;
                    case 'm': fprintf( out , "l");break;
                    case 'n': fprintf( out , "b");break;
                    case 'o': fprintf( out , "k");break;
                    case 'p': fprintf( out , "r");break;
                    case 'q': fprintf( out , "z");break;
                    case 'r': fprintf( out , "t");break;
                    case 's': fprintf( out , "n");break;
                    case 't': fprintf( out , "w");break;
                    case 'u': fprintf( out , "j");break;
                    case 'v': fprintf( out , "p");break;
                    case 'w': fprintf( out , "f");break;
                    case 'x': fprintf( out , "m");break;
                    case 'y': fprintf( out , "a");break;
                    case 'z': fprintf( out , "q");break;
                    case ' ': fprintf( out , " ");break;
                }
            }
            fprintf(out , "\n");

    }

    return 0;
}
