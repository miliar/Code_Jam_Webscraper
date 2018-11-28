#include <cstdio>

void main2()
{
    int N;
    scanf("%d", &N);
    int nb[N];
    bool gagne[N];
    int somme = 0;
    for (int i=0; i<N; i++)
    {
        scanf("%d", &nb[i]);
        somme += nb[i];
        gagne[i] = false;
    }
    
    bool stable = false;
    int somme2 = somme;
    int N2 = N;
    double points;
    while (!stable)
    {
        stable = true;  
        points = (somme+somme2)/(double)N2;
        for (int i=0; i<N; i++)
        {
            if (!gagne[i])
            {
                if ((double)nb[i] > points)
                {
                    stable = false;
                    gagne[i] = true;
                    somme2 -= nb[i];
                    N2--;
                }
            }
        }
    }
    
    for (int i=0; i<N; i++)
    {
        if (gagne[i])
            printf("0.0 ");
        else
            printf("%lf ", 100.*(points-(double)nb[i]) / (double) somme);
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++)
    {
        printf("Case #%d: ", i+1);
        main2();
        printf("\n");
    }
}
