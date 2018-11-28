#include<cstdio>
#include<cstring>

char MAP[300];
char in[300];

int main() {
    memset( MAP, 0, sizeof(char) );
    
    MAP['a'] = 'y', MAP['b'] = 'h', MAP['c'] = 'e', MAP['d'] = 's';
    MAP['e'] = 'o', MAP['f'] = 'c', MAP['g'] = 'v', MAP['h'] = 'x';
    MAP['i'] = 'd', MAP['j'] = 'u', MAP['k'] = 'i', MAP['l'] = 'g';
    MAP['m'] = 'l', MAP['n'] = 'b', MAP['o'] = 'k', MAP['p'] = 'r';
    MAP['q'] = 'z', MAP['r'] = 't', MAP['s'] = 'n', MAP['t'] = 'w';
    MAP['u'] = 'j', MAP['v'] = 'p', MAP['w'] = 'f', MAP['x'] = 'm';
    MAP['y'] = 'a', MAP['z'] = 'q';
    MAP[' '] = ' ';

    
    int ntc;
    scanf("%d", &ntc);
    getchar();

    for( int TC=1; TC<=ntc; TC++ ) {
        gets(in);
        printf("Case #%d: ", TC);
        int len = strlen(in);
        for( int i=0; i<len; i++ ) {
            printf("%c", MAP[ in[i] ] );
        }
        puts("");

    }
    return 0;
}
