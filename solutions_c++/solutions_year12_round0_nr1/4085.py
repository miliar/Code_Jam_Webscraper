#include <cstdio>

using namespace std;

char tab[50000];

int main(){
    tab['a'] = 'y';
    tab['b'] = 'h';
    tab['c'] = 'e';
    tab['d'] = 's';
    tab['e'] = 'o';
    tab['f'] = 'c';
    tab['g'] = 'v';
    tab['h'] = 'x';
    tab['i'] = 'd';
    tab['j'] = 'u';
    tab['k'] = 'i';
    tab['l'] = 'g';
    tab['m'] = 'l';
    tab['n'] = 'b';
    tab['o'] = 'k';
    tab['p'] = 'r';
    tab['q'] = 'z';
    tab['r'] = 't';
    tab['s'] = 'n';
    tab['t'] = 'w';
    tab['u'] = 'j';
    tab['v'] = 'p';
    tab['w'] = 'f';
    tab['x'] = 'm';
    tab['y'] = 'a';
    tab['z'] = 'q';
    int n;
    scanf("%d\n", &n);
    char p[105];
    int caso=1;
    while(n--){
        gets(p);
        printf("Case #%d: ", caso++);
        for(int i=0; p[i]; ++i){
            if(p[i]==' ') putchar(' ');
            else putchar(tab[p[i]]);
        }
        puts("");

    }
}
