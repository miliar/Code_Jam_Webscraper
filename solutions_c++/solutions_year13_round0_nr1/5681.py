#include<cstdio>
#include<iostream>

using namespace std;

enum Ganhardor{X=0,O,Draw,NotOver,Indefinido};

Ganhardor verifica(char matriz[][4])
{
    int linha,coluna,quantidade;
    char tipo;
    bool apareceu_um_ponto=false;

    for(linha=0;linha<4;linha++)
    {
        tipo='T';
        quantidade=0;

        for(coluna=0;coluna<4;coluna++)
        {
            if(matriz[linha][coluna]=='.')
            {
                apareceu_um_ponto=true;
                break;
            }
            else
            {
                if(tipo=='T')
                {
                    quantidade++;
                    tipo=matriz[linha][coluna];
                }
                else if(tipo=='X')
                {
                    if(matriz[linha][coluna] == 'X' || matriz[linha][coluna] == 'T') quantidade++;
                    else break;
                }
                else
                {
                    if(matriz[linha][coluna] == 'O' || matriz[linha][coluna] == 'T') quantidade++;
                    else break;
                }
            }
        }

        if(quantidade==4)
        {
            if(tipo == 'X') return X;
            else return O;
        }
    }

    for(coluna=0;coluna<4;coluna++)
    {
        tipo='T';
        quantidade=0;

        for(linha=0;linha<4;linha++)
        {
            if(matriz[linha][coluna]=='.')
            {
                apareceu_um_ponto=true;
                break;
            }
            else
            {
                if(tipo=='T')
                {
                    quantidade++;
                    tipo=matriz[linha][coluna];
                }
                else if(tipo=='X')
                {
                    if(matriz[linha][coluna] == 'X' || matriz[linha][coluna] == 'T') quantidade++;
                    else break;
                }
                else
                {
                    if(matriz[linha][coluna] == 'O' || matriz[linha][coluna] == 'T') quantidade++;
                    else break;
                }
            }
        }

        if(quantidade==4)
        {
            if(tipo == 'X') return X;
            else return O;
        }
    }

    tipo='T';
    quantidade=0;

    for(linha=coluna=0;linha<4;linha++,coluna++)
    {
        if(matriz[linha][coluna]=='.')
        {
            apareceu_um_ponto=true;
            break;
        }
        else
        {
            if(tipo=='T')
            {
                quantidade++;
                tipo=matriz[linha][coluna];
            }
            else if(tipo=='X')
            {
                if(matriz[linha][coluna] == 'X' || matriz[linha][coluna] == 'T') quantidade++;
                else break;
            }
            else
            {
                if(matriz[linha][coluna] == 'O' || matriz[linha][coluna] == 'T') quantidade++;
                else break;
            }
        }
    }

    if(quantidade==4)
    {
        if(tipo == 'X') return X;
        else return O;
    }

    tipo='T';
    quantidade=0;

    for(linha=0,coluna=3;linha<4;linha++,coluna--)
    {
        if(matriz[linha][coluna]=='.')
        {
            apareceu_um_ponto=true;
            break;
        }
        else
        {
            if(tipo=='T')
            {
                quantidade++;
                tipo=matriz[linha][coluna];
            }
            else if(tipo=='X')
            {
                if(matriz[linha][coluna] == 'X' || matriz[linha][coluna] == 'T') quantidade++;
                else break;
            }
            else
            {
                if(matriz[linha][coluna] == 'O' || matriz[linha][coluna] == 'T') quantidade++;
                else break;
            }
        }
    }

    if(quantidade==4)
    {
        if(tipo == 'X') return X;
        else return O;
    }


    if(apareceu_um_ponto) return NotOver;
    else return Draw;
}

void poem_matriz(char matriz[][4])
{
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cout <<  matriz[i][j];
            }

            cout << endl;
        }
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);


    int quantidade_casos_teste, caso=0;

    char matriz[4][4],carac[20];

    Ganhardor resposta;

    scanf("%d",&quantidade_casos_teste);

    while(quantidade_casos_teste--)
    {
        caso++;

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                scanf("%1s",carac);
                matriz[i][j]=carac[0];
            }
        }

        //poem_matriz(matriz);

        printf("Case #%d: ",caso);

        resposta=verifica(matriz);

        if(resposta==X) printf("X won\n");
        else if(resposta==O) printf("O won\n");
        else if(resposta == NotOver) printf("Game has not completed\n");
        else  printf("Draw\n");
    }

    return 0;
}
