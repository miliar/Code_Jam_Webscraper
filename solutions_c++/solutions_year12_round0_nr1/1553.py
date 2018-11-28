#include <iostream>

using namespace std;

char g[] = "yhesocvxduiglbkrztnwjpfmaq";

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A.out", "w", stdout);
    int nCase; 
    char s1[1024];
    scanf("%d", &nCase); gets(s1);
    for (int tCase = 1; tCase <= nCase; ++tCase) {
        gets(s1);
        printf("Case #%d: ", tCase);
        for (int i = 0; s1[i]; ++i) {
            if (s1[i] >= 'a' && s1[i] <= 'z')
               putchar(g[s1[i]-'a']);
            else putchar(' ');
        }
        puts("");
    }
    return 0;
} 
