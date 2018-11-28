#include <cstdio>

int main() {

    int T, i;
    char a[26] = {'y', 'h', 'e', 's',	'o',
    'c',	'v',	'x',	'd',	'u',
    'i',	'g',	'l',	'b',	'k',
    'r',	'z',	't',	'n',	'w',
    'j',	'p',	'f',	'm',	'a',	'q'};

    char text[101], c;

    scanf("%d ", &T);

    for (i = 1; i <= T; i++) {
        printf("Case #%d: ", i);

        do {
            scanf("%c", &c);
            if(c>= 'a' && c <= 'z') {
                c = a[c-'a'];
            }
            printf("%c", c);
        }while(c!='\n');

    }//end for

    return 0;
}//end main
