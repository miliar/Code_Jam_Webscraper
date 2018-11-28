#include <iostream>
#include <stdlib.h>
#include <stdio.h>
using namespace std;

int main(void){
    int T;
    char ch, abc[] = "yhesocvxduiglbkrztnwjpfmaq";

    scanf("%d\n", &T);
    for(int i = 1; i <= T; i ++){
        printf("Case #%d: ", i);
        while((ch = getchar()) != '\n')
            if(ch == ' ')
                printf(" ");
            else
                printf("%c", abc[(ch - 'a')]);
        printf("\n");
    }

    return 0;
}
