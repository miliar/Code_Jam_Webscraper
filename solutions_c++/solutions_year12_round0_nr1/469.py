#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

const int MAXS = 300;
char table[26], str[MAXS];

int main()
{
    int T;
    cin.getline(str, MAXS);

    table[ 'a'-'a' ] = 'y'; 
    table[ 'b'-'a' ] = 'h'; 
    table[ 'c'-'a' ] = 'e'; 
    table[ 'd'-'a' ] = 's'; 
    table[ 'e'-'a' ] = 'o';
    table[ 'f'-'a' ] = 'c'; 
    table[ 'g'-'a' ] = 'v'; 
    table[ 'h'-'a' ] = 'x'; 
    table[ 'i'-'a' ] = 'd'; 
    table[ 'j'-'a' ] = 'u'; 
    table[ 'k'-'a' ] = 'i'; 
    table[ 'l'-'a' ] = 'g'; 
    table[ 'm'-'a' ] = 'l'; 
    table[ 'n'-'a' ] = 'b'; 
    table[ 'o'-'a' ] = 'k'; 
    table[ 'p'-'a' ] = 'r'; 
    table[ 'q'-'a' ] = 'z'; 
    table[ 'r'-'a' ] = 't'; 
    table[ 's'-'a' ] = 'n'; 
    table[ 't'-'a' ] = 'w'; 
    table[ 'u'-'a' ] = 'j'; 
    table[ 'v'-'a' ] = 'p'; 
    table[ 'w'-'a' ] = 'f'; 
    table[ 'x'-'a' ] = 'm'; 
    table[ 'y'-'a' ] = 'a'; 
    table[ 'z'-'a' ] = 'q'; 


    T = atoi(str);

    for(int t = 1; T--; ++t)
    {
        cin.getline(str, MAXS);
        int len = strlen(str);
        printf("Case #%d: ", t);
        for(int i = 0; i < len; i++)
            if(str[i] >= 'a' && str[i] <= 'z')
                printf("%c", table[ str[i]-'a' ]);
            else
                printf("%c", str[i]);
        putchar('\n');
    }


    return 0;
}
