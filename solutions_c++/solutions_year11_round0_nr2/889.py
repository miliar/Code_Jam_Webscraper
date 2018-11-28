#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define STATES \
    STATE(Q) \
    STATE(W) \
    STATE(E) \
    STATE(R) \
    STATE(A) \
    STATE(S) \
    STATE(D) \
    STATE(F)
//Q, W, E, R, A, S, D, F
enum elem{
#define STATE(e) e,
    STATES
#undef STATE
};

int id(char c)
{
    switch (c) {
#define  STATE(e) case '#@e' : return e;
       STATES
#undef STATE
    }
    return 0;
}
char gen[8][8], opp[8][8];
char flag[8], stack[100];
int top;
int main()
{
  //  #define JK(q) printf("#@q")
   /* int t, c, d, n, tind;
    int i, j , k;
    char e1, e2, e3;
    scanf("%d", &t);
    for(tind = 1 ; tind <= t; t++)
    {
        memset(gen, 0, sizeof gen );
        memset(opp, 0, sizeof opp );

        scanf("%d", &c);
        for(i = 0 ; i < c; i++) {
            scanf(" %c%c%c", &e1, &e2, &e3);
            gen[id(e1)][id(e2)] = gen[id(e2)][id(e1)] = e3;
        }

        scanf("%d", &d);
        for(i = 0; i < d; i++) {
            scanf(" %c%c", &e1, &e2);
            opp[id(e1)][id(e2)] = opp[id(e2)][id(e1)] = 1;
        }

        scanf("%d ", &n);
        for(i = 0; i < 8; i++) flag[i] = 0;
        for(i = 0, top = -1; i < n; i++) {
            e1 = getchar();
            k = id(e1);
            if(top >= 0 && (e2 = gen[id(stack[top])][k]) > 0)//stack is not empty
                stack[top] = e2;
            else if (flag[k] != 0) {
                top = -1;
                for(j = 0; j < 8; j++) flag[j] = 0;
            }
            else {
                stack[++top] = e1;
                for(j = 0; j < 8; j++) flag[j] |= opp[k][j];
            }
        }
        printf("Case #%d: [", tind );
        for(i = 0; i <= top; i++)
            printf("%c%s", stack[i], ((i!= top)? ", ":""));
        printf("]\n");
    }*/
    return 0;
}
