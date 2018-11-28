#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
int main()
{
    int soma,j,qtd,i,T, N, S, P,maior,menor;
    scanf("%i\n",&T);
    for (i = 0; i < T; i++)
    {
        qtd = 0;
        scanf("%i %i %i",&N,&S,&P);
        for (int j = 0; j < N; j++)
        {
             scanf("%i",&soma);
             maior = (int)ceil(soma/3.0f);
             menor = (int)floor(soma/3.0f);

             if (maior>= P)
                 qtd++;
             else if (S>0 && (
                       (maior - menor == 0 && maior + 1 >= P && menor>0) ||
                       (maior - menor == 1 && maior + 1 >= P && 2*menor + maior + 1  <= soma))
                     )
             {
                        qtd++;
                        S--;
             }
        }
        printf("Case #%i: %i\n", i + 1, qtd);
    }
  return 0;
}
