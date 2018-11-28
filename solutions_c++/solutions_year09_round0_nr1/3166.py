#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    int L,D,N;
    int caso=1;
    int resposta;
    scanf("%d %d %d", &L, &D, &N);
    char dicionario[D][L];
    for(int i =0;i<D;i++)
    {
        scanf("%s",dicionario[i]);
    }
    //break the input in L blocks to verify in the dictionary.
    char palavra[500];

    for(int i=0;i<N;i++)
    {
        resposta=0;
        scanf("%s", palavra);
        char blocos[L][26]; //26 maximum alphabetic letters input if no one repeat
        int nB = 0; //counter block.
        for(int j=0;j<501;j++)
        {
            if(palavra[j]=='\0') break;
            else if(palavra[j]=='(')
            {
                j++;
                for(int k=0;palavra[j]!=')';j++,k++)
                {
                    blocos[nB][k]=palavra[j];
                    blocos[nB][k+1] = '\0';
                }
                nB++;
            }
            else
            {
                blocos[nB][0] = palavra[j];
                blocos[nB][1] = '\0'; //I have problems with that thing.
                nB++;
            }
        }
        //I have the blocks, now verify the possibilities.
        bool verificador;
        for(int j=0;j<D;j++) // palavras do dicionario
        {
            for(int k=0;k<L;k++) //posição na palavra e bloco respectivo.
            {
                verificador = false;
                for(int l=0;blocos[k][l]!='\0';l++)
                {
                    if(blocos[k][l]==dicionario[j][k])
                    {
                       verificador = true;
                       break;
                    }
                }
                if(k==(L-1) && verificador==true)
                {
                    resposta++;
                    break;
                }
                if(verificador==false) break;
            }
        }

        printf("Case #%d: %d\n", caso, resposta);
        caso++;
    }

    return 0;
}

