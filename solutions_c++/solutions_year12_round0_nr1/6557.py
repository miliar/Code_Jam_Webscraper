#include <cstdio>
#include <map>

using namespace std;

int main()
{
    int n,c;
    map<int,int> mapa;
    
    mapa['a'] = 'y';
    mapa['b'] = 'h';
    mapa['c'] = 'e';
    mapa['d'] = 's';
    mapa['e'] = 'o';
    mapa['f'] = 'c';
    mapa['g'] = 'v';
    mapa['h'] = 'x';
    mapa['i'] = 'd';
    mapa['j'] = 'u';
    mapa['k'] = 'i';
    mapa['l'] = 'g';
    mapa['m'] = 'l';
    mapa['n'] = 'b';
    mapa['o'] = 'k';
    mapa['p'] = 'r';
    mapa['q'] = 'z';
    mapa['r'] = 't';
    mapa['s'] = 'n';
    mapa['t'] = 'w';
    mapa['u'] = 'j';
    mapa['v'] = 'p';
    mapa['w'] = 'f';
    mapa['x'] = 'm';
    mapa['y'] = 'a';
    mapa['z'] = 'q';
    
    scanf("%d\n",&n);
    
    for(int i = 0; i < n; i++){
            printf("Case #%d: ",i+1);
            while( (c = getchar()) != '\n'){
                    if(c == ' ') 
                         putchar(c);
                    else
                        putchar(mapa[c]);
            }
            putchar(c);
    }

getchar();

 return 0;
}
