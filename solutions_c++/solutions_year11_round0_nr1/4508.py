#include<stdio.h>
#include<string.h>

int main(int argc, char **argv)
{
    int casos;

    int n;

    int comandosLaranja;
    int buttonsLaranja[103];

    int comandosAzul;
    int buttonsAzul[103];

    char comandos[103];

    int tempo, posO, posB;

    scanf("%d", &casos);

    for(int k = 1; k <= casos; k++)
    {
        scanf("%d", &n);

        tempo = 0;
        posO = 1;
        posB = 1;

        comandosAzul = 0;
        comandosLaranja = 0;

        char temp;
        int butaoTemp;
        int total = 0;
        int feitosLaranja = 0;
        int feitosAzul = 0;

        for(int i = 0; i < n; i++)
        {
            if(i >= 0)
            {
                scanf("%*c");
            }
            scanf("%c %d", &temp, &butaoTemp);

            if(temp == 'O')
            {
                buttonsLaranja[comandosLaranja] = butaoTemp;
                comandosLaranja++;
            }
            else
            {
                buttonsAzul[comandosAzul] = butaoTemp;
                comandosAzul++;
            }

            comandos[i] = temp;
        }

        while(total < n)
        {
            bool mudei = false;

            int targetO = buttonsLaranja[feitosLaranja];

            if(posO < targetO)
            {
                posO++;
            }
            else if(posO > targetO)
            {
                posO--;
            }
            else
            {
                if(comandos[feitosAzul+feitosLaranja] == 'O')
                {
                    feitosLaranja++;
                    total++;
                    mudei = true;
                }
            }

            int targetB = buttonsAzul[feitosAzul];

            if(posB < targetB)
            {
                posB++;
            }
            else if(posB > targetB)
            {
                posB--;
            }
            else
            {
                if(comandos[feitosAzul+feitosLaranja] == 'B' && !mudei)
                {
                    feitosAzul++;
                    total++;
                }
            }

            tempo++;
        }

        printf("Case #%d: %d\n", k, tempo);


    }

    return 0;
}
