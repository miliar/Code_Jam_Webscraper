#include <cstdio>
#include <cstring>

int main() {

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int casos;
    scanf("%d", &casos);
    //printf("Numero de Casos: %d\n", casos);


    int qtdEngines, qtdPerguntas;
    bool marcados[110];
    bool marca;
    char nomeEngines[110][110];
    int sequencia[1010];

    for (int i = 1; i <= casos; i++) {
        scanf("%d\n", &qtdEngines);
        //printf("qtdEngines: %d\n", qtdEngines);


        //printf("Engines:\n");
        for (int j = 0; j < qtdEngines; j++) {
            gets(nomeEngines[j]);
            //printf("%s\n", nomeEngines[j]);
        }


        scanf("%d\n", &qtdPerguntas);
        char temp[110];
        for (int j = 0; j < qtdPerguntas; j++) {
            gets(temp);

            bool achou = false;;
            int k = 0;
            while (!achou) {
                if (strcmp(nomeEngines[k], temp) == 0) {
                    achou = true;
                } else {
                    k++;
                }
            }

            sequencia[j] = k;
        }

        /*
        printf("Sequencia:\n");
        for (int j = 0; j < qtdPerguntas; j++) {
            printf("%d ", sequencia[j]);
        }
        printf("\n");
        */
        memset(marcados, false, sizeof(marcados));
        marca = true;

        /*if (i = 3) {
            printf("Antes de tudo: ");
            for (int k = 0; k < qtdEngines; k++) {
                printf("%d ", (marcados[k]?1:0));
            }
            printf("\n");
        }*/



        int switches = 0;

        marcados[sequencia[0]] = marca;
        /*if (i = 3) {
            printf("Marcou o primeiro: ");
            for (int k = 0; k < qtdEngines; k++) {
                printf("%d ", (marcados[k]?1:0));
            }
            printf("\n");
        }*/
        int qtdMarcados = 1;
        for (int j = 1; j < qtdPerguntas; j++) {

            if (marcados[sequencia[j]] != marca) { //nao esta marcado
                //printf("nao esta marcado %d qtMarcados = %d\n", sequencia[j], qtdMarcados);
                if (qtdMarcados < qtdEngines-1) {
                     /*if (i = 3) {
                        printf("antes de marcar: ");
                        for (int k = 0; k < qtdEngines; k++) {
                            printf("%d ", (marcados[k]?1:0));
                        }
                        printf("\n");
                    }*/
                    marcados[sequencia[j]] = marca;
                    ++qtdMarcados;
                    //printf("%d %d\n", sequencia[j], (marcados[j]?1:0));
                    //printf("marcou %d qtdMarcados = %d\n", sequencia[j], qtdMarcados);
                    /*if (i = 3) {
                        printf("Apos marcar: ");
                        for (int k = 0; k < qtdEngines; k++) {
                            printf("%d ", (marcados[k]?1:0));
                        }
                        printf("\n");
                    }*/

                } else {
                    /*if (i = 3) {
                        printf("\nTeste antes: ");
                        for (int k = 0; k < qtdEngines; k++) {
                            printf("%d ", (marcados[k]?1:0));
                        }
                        printf("\n");
                    }*/
                    ++switches;
                    marca = !marca;
                    qtdMarcados = 1;

                    //printf("Mais um entre %d e %d\nMarca = %d\n", j-1, j, (marca?1:0));

                    /*if (i = 3) {
                        for (int k = 0; k < qtdEngines; k++) {
                            printf("%d ", (marcados[k]?1:0));
                        }
                        printf("\n");
                    }*/
                }

            }

        }

        printf("Case #%d: %d\n", i, switches);
    }

    return 0;
}
