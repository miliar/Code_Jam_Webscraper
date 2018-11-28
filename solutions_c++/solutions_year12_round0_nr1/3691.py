#include <cstdio>

using namespace std;

char map[256];
int N;
char s[1024];

int main(){
    int i;
    char *c;

    for(i = 0; i < 256; i++){
        map[i] = (char) i;
    }

    map[(int) 'a'] = 'y';
    map[(int) 'b'] = 'h';
    map[(int) 'c'] = 'e';
    map[(int) 'd'] = 's';
    map[(int) 'e'] = 'o';
    map[(int) 'f'] = 'c';
    map[(int) 'g'] = 'v';
    map[(int) 'h'] = 'x';
    map[(int) 'i'] = 'd';
    map[(int) 'j'] = 'u';
    map[(int) 'k'] = 'i';
    map[(int) 'l'] = 'g';
    map[(int) 'm'] = 'l';
    map[(int) 'n'] = 'b';
    map[(int) 'o'] = 'k';
    map[(int) 'p'] = 'r';
    map[(int) 'q'] = 'z';
    map[(int) 'r'] = 't';
    map[(int) 's'] = 'n';
    map[(int) 't'] = 'w';
    map[(int) 'u'] = 'j';
    map[(int) 'v'] = 'p';
    map[(int) 'w'] = 'f';
    map[(int) 'x'] = 'm';
    map[(int) 'y'] = 'a';
    map[(int) 'z'] = 'q';

    scanf("%d\n", &N);

    for(i = 1; i <= N; i++){
        fgets_unlocked(s, 1024, stdin);
        printf("Case #%d: ", i);
        for(c = s; *c; c++){
            putchar(map[(int) *c]);
        }
    }

    return 0;
}
