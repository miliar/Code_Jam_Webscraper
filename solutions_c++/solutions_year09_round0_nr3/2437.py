#include<iostream>

char frase[100];

char saudacao[] = "welcome to code jam";

int count=0;

bool Calcula(int indice1,int indiceDois, int tamanho)
{
    int i;
    for(i=indiceDois;i<tamanho;i++)
    {
        char c = saudacao[indice1];
            char c2 = frase[i];
        if(saudacao[indice1]==frase[i])
        {
            if(indice1==18)
                count++;
            Calcula(indice1 + 1,i + 1,tamanho);
        }
    }
}

int main()
{

    int casos,i,j;
    scanf("%d", &casos);

    gets(frase);
    char resp[20];
    for(i=0;i<casos;i++)
    {
        gets(frase);
        Calcula(0,0,strlen(frase));
        sprintf(resp, "%d", count);
        int tam = strlen(resp);
        printf("Case #%d: ", i+1, count);
        if(tam>4)
        {
            for(j=tam-4;j<tam;j++)
                printf("%c", resp[j]);
            printf("\n");
        }
        else if(tam<4)
        {
            for(j=0;j<4-tam;j++)
                printf("0");
            printf("%s\n", resp);
        }
        else
            printf("%s\n",resp);
        count = 0;
    }
    return 0;
}
