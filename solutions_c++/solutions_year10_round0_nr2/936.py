#include<stdio.h>
#include<math.h>
#include<conio.h>

int mdc(int a, int b)
{
    int maior, menor, k;
    maior = a > b ? a : b ;
    menor = a > b ? b : a ;
    while(menor != 0)
    {
        k = maior%menor;
        maior = menor;
        menor = k;
    }
    return maior;
}    

int main()
{
    int N, i, j, anos, caso = 1, T, event, last;
    int vector[1001];
    FILE *IN, *OUT;
    
    IN = fopen("FWsmall.in", "r");
    OUT = fopen("FWsmall.out", "w");
    
    fscanf(IN, "%d", &T);
    printf("%d\n",T);
    getch();
    while(caso<=T)
    {
        fscanf(IN, "%d",&N);
        for(i=0; i<N; i++)
        {
            fscanf(IN, "%d", &event);
            vector[i] = event;
        }
        
        last = event;
        
        for(i=0; i<N; i++)
        {
            for(j=0; j<N; j++)
            {
                if(vector[j] > vector[i])
                {
                    event = vector[j];
                    vector[j] = vector[i];
                    vector[i] = event;
                }
            }
        }
             
        for(j=0; j<N-1; j++)
            vector[j] = vector[j+1] - vector[j];
            
        anos = vector[0];
        for(i=1; i<N-1; i++)
            anos = mdc(anos, vector[i]);       
        
        anos = (anos - (last % anos)) % anos;
        
        fprintf(OUT, "Case #%d: %d\n",caso,anos);
        caso++;
    }
    getch();
    return 0;
}
