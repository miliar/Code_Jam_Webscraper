#include<cstdio>

int main(){
    int t, x, c, d, n;
    int i, j, k, lin, col, form, magica, tam;
    int comb[26][26], opos[26][26], alfa[26][2], lista[100];
    char linha, coluna, forma, mag;
    bool oposto;

    scanf("%d", &t);

    for(x = 1; x <= t; x++) {
        scanf("%d", &c);

        for(i = 0; i < 26; i++) {
            alfa[i][0] = 0;
            alfa[i][1] = 0;
            for(j = 0; j < 26; j++) {
                comb[i][j] = -1;
                opos[i][j] = 0;
            }
        }

        for(i = 0; i < c; i++) {
            scanf(" %c%c%c", &linha, &coluna, &forma);
            lin = (int)linha - 'A';
            col = (int)coluna - 'A';
            form = (int)forma - 'A';
            comb[lin][col] = form;
            comb[col][lin] = form;
        }

        scanf("%d", &d);

        for(i = 0; i < d; i++) {
            scanf(" %c%c", &linha, &coluna);
            lin = (int)linha - 'A';
            col = (int)coluna - 'A';
            opos[lin][col] = 1;
            opos[col][lin] = 1;
        }

        scanf("%d", &n);


        tam = 0;
        k = 1;
        for(i = 0; i < n; i++) {
            scanf(" %c", &mag);
            magica = (int)mag - 'A';

            if(tam >= 1 && comb[magica][ lista[tam - 1] ]  >= 0) {
                if(alfa[ lista[tam - 1] ][0] == k)
                    alfa[ lista[tam - 1] ][1]--;
                lista[tam - 1] = comb[magica][ lista[tam - 1] ];
            }
            else {
                oposto = false;
                for(j = 0; j < 26; j++) {
                    if(opos[magica][j] == 1 && alfa[ j ][0] == k && alfa[ j ][1] > 0) {
                        k++; //limpa alfa
                        tam = 0; //limpa lista
                        oposto = true;
                        break;
                    }
                }

                if(!oposto) {
                    lista[tam] = magica;
                    tam++;
                    if(alfa[magica][0] != k) {
                        alfa[magica][0] = k;
                        alfa[magica][1] = 1;
                    }
                    else
                        alfa[magica][1]++;
                }
            }
        }

        printf("Case #%d: [", x);
        if(tam > 0)
            printf("%c", lista[0] + 'A');
        for(i = 1; i < tam; i++)
            printf(", %c", lista[i] + 'A');
        printf("]\n");
    }

    return 0;
}
