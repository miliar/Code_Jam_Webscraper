#include <stdio.h>
#include <iostream>
#include <cmath>

using namespace std;

#define MAX 105
#define eps 1e-7

long long n, A, B, C, D, x00, y00, M;
long long coord[MAX][3], cnt, rez = 0;
double midX, midY, fract1, fract2, intpart;
int nb_tests;

void genCoord();

double fabs(double x)
{
    if (x < 0) return -x;
    return x;
}

int main()
{
    FILE *fin = fopen("A.in", "r");
    FILE *fout = fopen("Aout.out", "w");
    fscanf(fin, "%lld", &nb_tests);
    for (int t = 1; t <= nb_tests; ++t)
    {
        rez = 0;
        fscanf(fin, "%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x00, &y00, &M);
        genCoord();
      // printf("Generated : \n");
      //  for (int j = 0; j < cnt; ++j)
       // {
       //     printf("%lld ", coord[j][0]);
       //     printf("%lld\n", coord[j][1]);
       // }
        for (int j1 = 0; j1 < cnt; ++j1)
            for (int j2 = j1+1; j2 < cnt; ++j2)
                for (int j3 = j2+1; j3 < cnt; ++j3)
                {
                    midX = (double)(coord[j1][0] + coord[j2][0] + coord[j3][0]) / 3.0;
                    midY = (double)(coord[j1][1] + coord[j2][1] + coord[j3][1]) / 3.0;
                    fract1 = modf(midX , &intpart);
                    fract2 = modf(midY , &intpart);
                    if (fabs(fract1) < eps && fabs(fract2) < eps)
                        rez++;
                }
        fprintf(fout, "Case #%d: %lld", t, rez);
        if (t != nb_tests)
            fprintf(fout, "\n");
    }
    fclose(fin);
    fclose(fout);
    
    //system("pause");
    
    return 0;
}

void genCoord()
{
    cnt = 0;
    long long X = x00, Y = y00;
    coord[cnt][0] = X;
    coord[cnt][1] = Y;
    cnt++;
    for (int i = 1; i < n; ++i)
    {
        X = (A * X + B) % M;
        Y = (C * Y + D) % M;
        coord[cnt][0] = X;
        coord[cnt][1] = Y;
        cnt++;
    }
}

