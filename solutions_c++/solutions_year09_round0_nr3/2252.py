/* 
 * File:   WelcomeFinder.cpp
 * Author: ziv wities
 *
 * Created on 3 ������ 2009, 18:49
 */

#include <stdlib.h>
#include <stdio.h>

#define X_W 0
#define X_WE 1
#define X_WEL 2
#define X_WELC 3
#define X_WELCO 4
#define X_WELCOM 5
#define X_WELCOME 6
#define X_WELCOME_ 7
#define X_WELCOME_T 8
#define X_WELCOME_TO 9
#define X_WELCOME_TO_ 10
#define X_WELCOME_TO_C 11
#define X_WELCOME_TO_CO 12
#define X_WELCOME_TO_COD 13
#define X_WELCOME_TO_CODE 14
#define X_WELCOME_TO_CODE_ 15
#define X_WELCOME_TO_CODE_J 16
#define X_WELCOME_TO_CODE_JA 17
#define X_WELCOME_TO_CODE_JAM 18
#define MESSAGE_LEN 19
#define MASK 10000

int nCount[MESSAGE_LEN] = {0};

void AddTransition(int x_advanceTo) {
    nCount[x_advanceTo] += nCount[x_advanceTo - 1];
    nCount[x_advanceTo] %= MASK;
}

void HandleChar(char c) {
    switch (c) {
        case 'w': nCount[X_W] += 1;
            nCount[X_W] %= MASK;
            break;
        case 'e':
            AddTransition(X_WE);
            AddTransition(X_WELCOME);
            AddTransition(X_WELCOME_TO_CODE);
            break;
        case 'l':
            AddTransition(X_WEL);
            break;
        case 'c':
            AddTransition(X_WELC);
            AddTransition(X_WELCOME_TO_C);
            break;
            break;
        case 'o':
            AddTransition(X_WELCO);
            AddTransition(X_WELCOME_TO);
            AddTransition(X_WELCOME_TO_CO);
            break;
        case 'm':
            AddTransition(X_WELCOM);
            AddTransition(X_WELCOME_TO_CODE_JAM);
            break;
        case 't':
            AddTransition(X_WELCOME_T);
            break;
        case 'd':
            AddTransition(X_WELCOME_TO_COD);
            break;
        case 'j':
            AddTransition(X_WELCOME_TO_CODE_J);
            break;
        case 'a':
            AddTransition(X_WELCOME_TO_CODE_JA);
            break;
        case ' ':
            AddTransition(X_WELCOME_);
            AddTransition(X_WELCOME_TO_);
            AddTransition(X_WELCOME_TO_CODE_);
            break;
        default: /*do nothing*/ break;
    }


}

/*
 * 
 */
int main(int argc, char** argv) {
    FILE* in = fopen("C-large.in", "r");
    FILE* out = fopen("C-large.out", "w");

    int nTests;
    fscanf(in, "%d\n", &nTests);

    for (int i = 1; i <= nTests; ++i) {
        // init the count:
        for (int j=0; j<MESSAGE_LEN; ++j)
            nCount[j] = 0;
        
        // read the string, counting possibilities:
        char c;
        while (((c = fgetc(in)) != '\n') && (c != EOF)) {
            HandleChar(c);
            printf("%c",c, c);
        }
        printf("\n");

        fprintf(out, "Case #%d: %04d\n", i, nCount[X_WELCOME_TO_CODE_JAM] % MASK);
        printf("Case #%d: %04d\n", i, nCount[X_WELCOME_TO_CODE_JAM] % MASK);

    }

    fclose(in);
    fclose(out);
    return (EXIT_SUCCESS);
}

