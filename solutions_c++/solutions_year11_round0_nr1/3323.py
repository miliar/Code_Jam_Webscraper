#include <stdio.h>

int main()
{
    int tempo, o, b, i, n, buttons, teste, posO,posB,flagO,flagB;
    char aux1, aux2, vetorB[102], vetorO[102], vacao[102][2];
    int auxi2;
    scanf("%d ",&n);
    for (teste = 1; teste <= n; teste++)
    {
        tempo = o = b = 0;
        scanf("%d ",&buttons);
        for (i = 0; i< buttons; i++)
        {
             scanf("%c %d ",&aux1,&auxi2);
             aux2 = auxi2;
             if (aux1 == 'O')
                vetorO[o++] = aux2;
             else
                vetorB[b++] = aux2;
             vacao[i][0] = aux1;
             vacao[i][1] = aux2;
        }
        vacao[i][0] = vacao[i][1] =  '\0';
        vetorB[b] = vetorO[o] = 0;
        o = b = i = 0;
        posO = posB = 1;

        while (1)
        {
                tempo++;
                flagO = flagB = 0;
                if (vacao[i][0] == '\0') break;

                if (vacao[i][0] == 'O')
                {
                     if (posO == vacao[i][1]){ // fez a acao  -- vacao guarda a localizacao da acao
                            i++;
                            o++;    //proxima acao da O
                            flagO = 1;
                        }
                }
                else
                {
                      if (posB == vacao[i][1]){ // fez a acao
                            i++;
                            b++;    //proxima acao do B
                            flagB = 1;
                        }
                }

                if (posO < vetorO[o] && flagO == 0) // n fez Acao ainda e n chegou aonde quer
                    posO++;

                if (posB < vetorB[b] && flagB == 0) // n fez Acao ainda e n chegou aonde quer
                    posB++;

                if (posO > vetorO[o] && flagO == 0) // n fez Acao ainda e n chegou aonde quer
                    posO--;

                if (posB > vetorB[b] && flagB == 0) // n fez Acao ainda e n chegou aonde quer
                    posB--;

        }
         printf("Case #%d: %d\n",teste, --tempo );
    }
    return 0;
}
