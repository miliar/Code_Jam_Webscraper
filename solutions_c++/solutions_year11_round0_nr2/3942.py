#include <stdio.h>
#include <string.h>
#include <map>

int C;
int D;
int N;
char com[36][4];
char opp[28][3];
char invoke[101];
int lastadd=0;

char iscombine(char buf[101], int buf_index, char c)
{
    if (buf_index == 0)
        return 0;
    char d = buf[buf_index-1];
    for (int i=0;i<C;i++) {
        if (c==com[i][0] && d==com[i][1])
            return com[i][2];
        else if (c==com[i][1] && d==com[i][0])
            return com[i][2];
    }
    return 0;
}

int isop(char oplist[101], int op_index, char c)
{
    for (int i=0;i<op_index;i++) {
        if (oplist[i]==c) {
            return 1;
        }
    }
    return 0;
}

void inc(char oplist[101], int* op_indexp, char d)
{
    for (int i=0;i<*op_indexp;i++) {
        if (oplist[i] == d) return;
    }
    oplist[*op_indexp] = d;
    *op_indexp = *op_indexp + 1;
    lastadd++;
}

void addop(char oplist[101], int* op_indexp, char c)
{
    int d;
    for (int i=0;i<D;i++) {
        if (opp[i][0] == c) {
            d = opp[i][1];
            inc(oplist, op_indexp, d);
        }else if (opp[i][1] == c) {
            d = opp[i][0];
            inc(oplist, op_indexp, d);
        }
    }
}

void func()
{

    scanf("%d", &C);

    for (int i=0;i<C;i++) {
        scanf("%s", com[i]);
    }

    scanf("%d", &D);
    for (int i=0;i<D;i++) {
        scanf("%s", opp[i]);
    }

    scanf("%d", &N);
    scanf("%s", invoke);

    int buf_index=0;
    int op_index=0;
    char buf[101];
    char oplist[101];
    bool is_last_char_added_op = false;

    for (int i=0;i<N;i++) {
        char c;
        if (c = iscombine(buf, buf_index, invoke[i])) {
            buf[buf_index-1] = c;
            if (lastadd!=0) {
                op_index-=lastadd;
                lastadd=0;
            }
            continue;
        }
        if (isop(oplist, op_index, invoke[i])) {
            buf_index=0;
            op_index = 0;
            lastadd=0;
        }else{
            lastadd=0;
            buf[buf_index++]=invoke[i];
            addop(oplist, &op_index, invoke[i]);
        }
    }

    printf("[");
    for (int i=0;i<buf_index-1;i++) {
        printf("%c, ", buf[i]);
    }
    if (buf_index > 0)
        printf("%c", buf[buf_index-1]);
    printf("]\n");
}

main()
{
    int T;
    scanf("%d", &T);
    for (int i=0;i<T;i++) {
        printf("Case #%d: ", i+1);
        func();
    }
}
