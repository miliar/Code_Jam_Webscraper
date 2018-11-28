#include<cstdio>
#include<cmath>

double x[100];
double y[100];
double r[100];
int n;

int main()
{
    int t, teste;
    int i, j, a;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        scanf("%d", &n);
        for (i=0; i<n; i++)
        {
            int aux1, aux2, aux3;
            scanf("%d %d %d", &aux1, &aux2, &aux3);
            x[i] = aux1;
            y[i] = aux2;
            r[i] = aux3;
        }
        double resp = 1000000;
        if (n == 1)
        {
            printf("Case #%d: %lf\n", t+1, r[0]);
        }
        else if (n == 2)
        {
            if (r[0] > r[1])
                printf("Case #%d: %lf\n", t+1, r[0]);
            else
                printf("Case #%d: %lf\n", t+1, r[1]);
        }
        else
        {
            double aux;
            aux = sqrt((x[0] - x[1])*(x[0] - x[1]) + (y[0] - y[1])*(y[0] - y[1])) + r[0] + r[1];
            aux = aux/2;
            if (aux < r[2]) aux = r[2];
            if (aux < resp) resp = aux;
            aux = sqrt((x[2] - x[1])*(x[2] - x[1]) + (y[2] - y[1])*(y[2] - y[1])) + r[2] + r[1];
            aux = aux/2;
            if (aux < r[0]) aux = r[0];
            if (aux < resp) resp = aux;
            aux = sqrt((x[0] - x[2])*(x[0] - x[2]) + (y[0] - y[2])*(y[0] - y[2])) + r[0] + r[2];
            aux = aux/2;
            if (aux < r[1]) aux = r[1];
            if (aux < resp) resp = aux;
            
            printf("Case #%d: %lf\n", t+1, resp);        
        }
    }
    return 0;
}
