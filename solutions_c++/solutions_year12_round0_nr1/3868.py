#include <cstdio>
#include <cstring>

char gao(char r) {
    switch(r) {
        case 'a':
            r = 'y';
            break;
        case 'b':
            r = 'h';
            break;
        case 'c':
            r = 'e';
            break;
        case 'd':
            r = 's';
            break;
        case 'e':
            r = 'o';
            break;
        case 'f':
            r = 'c';
            break;
        case 'g':
            r = 'v';
            break;
        case 'h':
            r = 'x';
            break;
        case 'i':
            r = 'd';
            break;
        case 'j':
            r = 'u';
            break;
        case 'k':
            r = 'i';
            break;
        case 'l':
            r = 'g';
            break;
        case 'm':
            r = 'l';
            break;
        case 'n':
            r = 'b';
            break;
        case 'o':
            r = 'k';
            break;
        case 'p':
            r = 'r';
            break;
        case 'q':
            r = 'z';
            break;
        case 'r':
            r = 't';
            break;
        case 's':
            r = 'n';
            break;
        case 't':
            r = 'w';
            break;
        case 'u':
            r = 'j';
            break;
        case 'v':
            r = 'p';
            break;
        case 'w':
            r = 'f';
            break;
        case 'x':
            r = 'm';
            break;
        case 'y':
            r = 'a';
            break;
        case 'z':
            r = 'q';
            break;
        default:
            break;
    }
    return r;
}

int main() {
    char s[105];
    int T, c = 0;
    gets(s);
    sscanf(s, "%d", &T);
    while(T--) {
        gets(s);
        printf("Case #%d: ", ++c);
        for(int i = 0; i < strlen(s); i++)
            printf("%c", gao(s[i]));
        puts("");
    }
}
