#include <stdio.h>
#include <string.h>

int main()
{
	char forma[300][300];
    char desforma[300];
    char lista[102];
    char listanova[102];
    char listanova2[102];

    int i,x, j, c1,  n, listaaux[300];
    char aux1,aux2,aux3;

	scanf("%d ",&n);

	for (i= 1; i<=n;i++)
	{
		scanf("%d ",&c1);
		memset(forma,' ',sizeof(char)*300*300);
		memset(desforma,' ',sizeof(char)*300);
        memset(listaaux,0,sizeof(int)*300);
		for (j = 0; j < c1;j++)
		{
			scanf("%c%c%c ",&aux1,&aux2,&aux3);
 			forma[aux1][aux2] = aux3;
			forma[aux2][aux1] = aux3;
		}

		scanf("%d ",&c1);
		for (j = 0; j < c1;j++)
		{
			scanf("%c%c ",&aux1,&aux2);
 			desforma[aux1] = aux2;
 			desforma[aux2] = aux1;
		}

		scanf("%d ",&c1);
		for (j = 1; j <= c1;j++)
		{
			scanf("%c",&aux1);
 			lista[j] = aux1;
		}
        lista[j] == '\0';

        x = 1;
        for (j = 1; j <= c1;j++)
        {

            if (lista[j+1] == '\0')
            {
                listanova[x++] = lista[j];
                break;
            }

            //desforma
            listaaux[lista[j]] = 1;
            if (desforma[lista[j]] != ' ')
            {
                if (listaaux[desforma[lista[j]]] == 1)
                {
                        //desformou
                        listaaux[lista[j]] = 0;
                        listaaux[desforma[lista[j]]] = 0;
                }
            }
            // forma
            if (listaaux[lista[j]] == 1 && forma[lista[j]][lista[j+1]] != ' ')
            {
//                listanova[x++] = forma[lista[j]][lista[j+1]];
                lista[j+1] = forma[lista[j]][lista[j+1]];
                listaaux[lista[j]] = 0;
            }
            else
            {
                 listanova[x++] = lista[j];
            }
        }
        listanova[x] = ' ';



        memset(listaaux,0,sizeof(int)*300);

        for (j = 1; j <= x;j++)
        {
            listaaux[listanova[j]] = 1;
            if (desforma[listanova[j]] != ' ')
            {
                if (listaaux[desforma[listanova[j]]] == 1)
                {
                        //desformar
                        listaaux[desforma[listanova[j]]] = 0;
                        listaaux[listanova[j]] = 0;
                        int t = j;
                        aux2 = desforma[listanova[j]];
                        while(1)
                        {
                            listanova[t] = ' ';
                            t--;
                            if (t == 0) break;
                        }

                        for (t = 1; t <= j; t++ )
                            if (listanova[t] != ' ')
                                listaaux[listanova[t]] = 1;
                }
            }

        }

        int q = 1;
        for (j = 1; j <= x; j++ )
           if (listanova[j] != ' ')
                 listanova2[q++] = listanova[j];

        printf("Case #%d: [",i);

        for (j = 1; j < q;j++)
        {
            if (j == q-1)
                printf("%c",listanova2[j]);
            else
                printf("%c, ",listanova2[j]);
        }
        printf("]\n");
	}

}
