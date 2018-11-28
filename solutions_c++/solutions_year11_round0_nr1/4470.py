#include<cstdio>

int main(){

    int t, n, p, i, j, x, y;

    int tempo_tarefas[101], quant_tarefas[100];
    int tempo_total, it, iq, b1, b2, r_ant, r_atual;

    char r;

    scanf("%d", &t);

    for(x = 1; x <= t; x++) {

        for(i = 0; i < 101; i++)
            tempo_tarefas[i] = 0;

        scanf("%d", &n);

        b1 = 1;
        b2 = 1;
        r_ant = -1;
        iq = -1;
        for(i = 0; i < n; i++) {
            scanf(" %c %d", &r, &p);

            if(r == 'O') {
                r_atual = 0;
                tempo_tarefas[i] = (b1 < p) ? p - b1 : b1 - p;
                b1 = p;
            }
            else {
                r_atual = 1;
                tempo_tarefas[i] = (b2 < p) ? p - b2 : b2 - p;
                b2 = p;
            }

            if(r_ant != r_atual) {
                r_ant = r_atual;
                iq++;
                quant_tarefas[iq] = 1;
            }
            else
                quant_tarefas[iq]++;
        }

        it = 0;
        y = 0;
        for(i = 0; i < iq+1; i++) {
            tempo_total = 0;
            for(j = 0; j < quant_tarefas[i]; j++) {
                tempo_total += tempo_tarefas[it] + 1;
                it++;
            }

            if(tempo_total < tempo_tarefas[it])
                tempo_tarefas[it] -= tempo_total;
            else
                tempo_tarefas[it] = 0;

            y += tempo_total;
        }

        printf("Case #%d: %d\n", x, y);
    }

    return 0;
}

