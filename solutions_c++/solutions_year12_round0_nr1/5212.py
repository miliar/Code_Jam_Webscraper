#include<cstdio>
#include<cstring>
// char str1[1000];
// char str2[1000];
char str[1000];
char conv[300];

void init() {
    conv['a'] = 'y';
    conv['b'] = 'h';
    conv['c'] = 'e';
    conv['d'] = 's';
    conv['e'] = 'o';
    conv['f'] = 'c';
    conv['g'] = 'v';
    conv['h'] = 'x';
    conv['i'] = 'd';
    conv['j'] = 'u';
    conv['k'] = 'i';
    conv['l'] = 'g';
    conv['m'] = 'l';
    conv['n'] = 'b';
    conv['o'] = 'k';
    conv['p'] = 'r';
    conv['q'] = 'z';
    conv['r'] = 't';
    conv['s'] = 'n';
    conv['t'] = 'w';
    conv['u'] = 'j';
    conv['v'] = 'p';
    conv['w'] = 'f';
    conv['x'] = 'm';
    conv['y'] = 'a';
    conv['z'] = 'q';
}

int main() {
    // freopen("A-small-attempt0.in", "r", stdin);
    // freopen("A-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d",&T);
    gets(str);
    init();
    for (int kase = 1; kase<=T; kase++) {
        gets(str);
        // puts(str);
        // gets(str2);
        int len = strlen(str);
        printf("Case #%d: ",kase);
        for (int i=0; i<len; i++) {
            if (str[i] == ' ') printf(" ");
            // if (str1[i] == ' ') continue;
            else printf("%c", conv[str[i]]);
            // conv[str1[i]] = str2[i];
        }
        printf("\n");
    }
    return 0;
}
