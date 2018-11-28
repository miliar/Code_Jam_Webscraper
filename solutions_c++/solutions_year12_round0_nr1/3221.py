#include <stdio.h>
#include <string>
#include <map>
using namespace std;

string res;
map< char , char > m;

int main ()
{
    FILE *in = fopen ("A.in","r");
    FILE *out = fopen ("A.out","w");

    int t;
    int k = 1;
    char c;

    m[ 'y' ] = 'a'; m[ 'n' ] = 'b'; m[ 'f' ] = 'c'; m[ 'i' ] = 'd'; m[ 'c' ] = 'e'; m[ 'w' ] = 'f'; m[ 'l' ] = 'g'; m[ 'b' ] = 'h'; m[ 'k' ] = 'i'; m[ 'u' ] = 'j';
    m[ 'o' ] = 'k'; m[ 'm' ] = 'l'; m[ 'x' ] = 'm'; m[ 's' ] = 'n'; m[ 'e' ] = 'o'; m[ 'v' ] = 'p'; m[ 'z' ] = 'q'; m[ 'p' ] = 'r'; m[ 'd' ] = 's'; m[ 'r' ] = 't';
    m[ 'j' ] = 'u'; m[ 'g' ] = 'v'; m[ 't' ] = 'w'; m[ 'h' ] = 'x'; m[ 'a' ] = 'y'; m[ 'q' ] = 'z';

    fscanf (in,"%d",&t);
    fscanf (in,"%c",&c);

    while( t -- )
    {
        res = "";

        fscanf (in,"%c",&c);
        while( c != '\n' )
        {
            if (c == ' ') res += " ";
            else res += m[c];
            fscanf (in,"%c",&c);
        }

        fprintf (out,"Case #%d: ",k);
        fprintf (out,"%s\n",res.c_str());
        k ++;
    }
}
