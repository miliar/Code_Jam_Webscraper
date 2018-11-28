#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

char s[27] = "yhesocvxduiglbkrztnwjpfmaq";//"ynficwlbkuomxsevzpdrjgtha";


char str[150];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int icase, tt = 0;
    scanf("%d", &icase);
    getchar();
    while (icase--) {
        printf("Case #%d: ", ++tt);
        gets(str);
        for (int i = 0; i < (int)strlen(str); i++) {
            if (str[i] == ' ') printf(" ");
            else printf("%c", s[str[i] - 'a']);
        }
        printf("\n");

    }
    return 0;
}
