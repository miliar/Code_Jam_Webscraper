#include <cstdio>
#include <cstring>


char l1, l2, l3;
int c, forma[27][27], opoe[27][27], n, f, o, in[101],size, satual, l, aux;


int main() {
    int caso, i, j;
    scanf("%d", &n);
    for(caso=1; caso<=n; caso++) {
        memset(opoe, 0, sizeof(opoe));
        for(i=0;i<27;i++)
            for(j=0;j<27;j++)
                forma[i][j] = -1;
        scanf("%d", &f);
        for(i=0;i<f;i++) {
            getchar(); scanf("%c%c%c", &l1, &l2, &l3);
            forma[l1 - 'A'][l2 - 'A'] = l3 - 'A';
            forma[l2 - 'A'][l1 - 'A'] = l3 - 'A';
        }
        scanf("%d", &o);
        for(i=0;i<o;i++) {
            getchar(); scanf("%c%c", &l1, &l2);
            opoe[l1 - 'A'][l2 - 'A'] = 1;
            opoe[l2 - 'A'][l1 - 'A'] = 1;
        }

        scanf("%d", &size);getchar();
        satual = 0;

        for(i=0;i<size;i++) {
            scanf("%c", &l1);
            l = l1 - 'A';

            if(satual==0)
                in[satual++] = l;
            else {
                aux = forma[l][in[satual-1]];
                if(aux != -1)
                    in[satual-1] = aux;
                else {
                    for(j=0;j<satual;j++)
                        if(opoe[l][in[j]]) break;
                    if(j<satual)
                        satual = 0;
                    else
                        in[satual++] = l;
                }
            }
        }

        printf("Case #%d: [", caso);
        for(i=0;i<satual;i++) {
            printf("%c", in[i]+'A');
            if(i<satual-1)
                printf(", ");
        }
        printf("]\n");


    }

    return 0;
}
