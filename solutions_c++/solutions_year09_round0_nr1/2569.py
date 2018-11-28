#include <iostream>
#include<string.h>

using namespace std;

int main()
{

    int L, D, N,i,j,k;

    scanf("%d %d %d", &L, &D, &N);

    char palavras[D][L+1];
    int qtd[D][L];

    char p[100000];

    memset(qtd, 0,sizeof(int) * D * L);

    for(i=0;i<D;i++)
    {
        scanf("%s", palavras[i]);
    }

    gets(p);
    for(k=0;k<N;k++)
    {
        gets(p);

        int tam = strlen(p);
        int indLetra=0;
        bool abriuChave=false;
        for(i=0;i<tam;i++)
        {
            if(p[i]=='(')
            {
                abriuChave=true;
            }
            else if(p[i]==')')
            {
                indLetra++;
                abriuChave=false;
            }
            else
            {
                for(j=0;j<D;j++)
                {
                    if(palavras[j][indLetra]==p[i])
                        qtd[j][indLetra]=1;
                }
                if(abriuChave==false)
                    indLetra++;
            }
        }
        int cont=0;
        for(i=0;i<D;i++)
        {
            int valor = 0;
            for(j=0;j<L;j++)
            {
                valor += qtd[i][j];
            }
            if(valor==L)
                cont++;
        }

        printf("Case #%d: %d\n", k+1, cont);

        memset(qtd, 0,sizeof(int) * D * L);
    }
    return 0;
}
