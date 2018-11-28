#include <cstdio>
#include <cstring>
using namespace std;

char Googlerese[27] = "yhesocvxduiglbkrztnwjpfmaq";

char* solve(char* dest, char* src) {
    char *output = dest;
    for (; *src; src++, dest++)
        *dest = *src == ' ' ? ' ' : Googlerese[*src - 'a'];
    *dest = '\0';
    return output;
}

void trim(char* s) {
    size_t len = strlen(s);
    if (s[len - 1] == '\n')
        s[len - 1] = 0;
}

int main() {
    char input[102], output[102]; // include '\n' and null
    int T;

    scanf("%d\n", &T);
    for (int t = 1; t <= T; t++) {
        fgets(input, 102, stdin);
        trim(input);
        printf("Case #%d: %s\n", t, solve(output, input));
    }
    return 0;
}
