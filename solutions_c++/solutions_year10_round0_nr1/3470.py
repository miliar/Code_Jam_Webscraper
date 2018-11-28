#include<stdio.h>
#include<math.h>
#include<conio.h>

int main()
{
    int N, K, clicks, i, caso = 1, T, state;
    FILE *IN, *OUT;
    
    IN = fopen("A-large.in", "r");
    OUT = fopen("saidalarge1.txt", "w");
    
    fscanf(IN, "%d", &T);
    printf("%d", T);
    getch();
    while(caso<=T)
    {
        fscanf(IN, "%d %d", &N, &K);
        clicks = (int) pow(2,N);
        if(K % clicks == clicks - 1)
        {
            fprintf(OUT, "Case #%d: ON\n", caso);
            printf("Case #%d: ON\n", caso);
        }
        else 
        {
            fprintf(OUT, "Case #%d: OFF\n", caso);
            printf("Case #%d: OFF\n", caso);
        }
        caso++;    
    }
    getch();
    return 0;
}
