#include <cstdio>

int main() {
    char table[27] = "yhesocvxduiglbkrztnwjpfmaq";

    char input;
    unsigned tests;
    scanf("%u\n", &tests);
    for(unsigned i = 1; i <= tests; ++i) {
        printf("Case #%u: ", i);
        while((input = getchar()) != 10) {
            if(input >= 'a' && input <= 'z')
                putchar(table[input - 'a']);
            else
                putchar(input);
        }
        putchar(10);
    }
    return 0;
}
