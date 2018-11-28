#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

main()
    {int T;
    string str;

    cin >> T;
    getchar();

    for(int i=0; i<T; i++)
        {getline(cin, str);

        int tam = str.length();
        while(tam--)
            {switch(str[tam])
                {case 'a': str[tam] = 'y'; break;
                case 'b': str[tam] =  'h'; break;
                case 'c': str[tam] = 'e'; break;
                case 'd': str[tam] = 's'; break;
                case 'e': str[tam] = 'o'; break;
                case 'f': str[tam] = 'c'; break;
                case 'g': str[tam] = 'v'; break;
                case 'h': str[tam] = 'x'; break;
                case 'i': str[tam] = 'd'; break;
                case 'j': str[tam] = 'u'; break;
                case 'k': str[tam] = 'i'; break;
                case 'l': str[tam] = 'g'; break;
                case 'm': str[tam] = 'l'; break;
                case 'n': str[tam] = 'b'; break;
                case 'o': str[tam] = 'k'; break;
                case 'p': str[tam] = 'r'; break;
                case 'q': str[tam] = 'z'; break;
                case 'r': str[tam] = 't'; break;
                case 's': str[tam] = 'n'; break;
                case 't': str[tam] = 'w'; break;
                case 'u': str[tam] = 'j'; break;
                case 'v': str[tam] = 'p'; break;
                case 'w': str[tam] = 'f'; break;
                case 'x': str[tam] = 'm'; break;
                case 'y': str[tam] = 'a'; break;
                case 'z': str[tam] = 'q'; break;}}

            cout<< "Case #" << i+1 << ": "<<str<<endl;}
    return 0;}
