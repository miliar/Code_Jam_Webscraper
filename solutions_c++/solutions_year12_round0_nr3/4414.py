#include <iostream>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <stdio.h>

/* Prototipo de función */
void Permutaciones(char *, int l=0);
bool notexist(int Ra);
void LimpiarHechos();

using namespace std;
int T=0;
int Hechos[2000000];
int main()
{
    int N, A, B, c=0;
    cin>>N;
    for (int ic=1; ic<=N; ic++)
    {
        T=0;
        cin>>A>>B;
        char X[(int)log(A)+1];
        for (int k=A; k<=B; k++)
        {
            int r=sprintf(X,"%i",k);

            for (int pl=0; pl<strlen(X); pl++)
            {
                char y=X[strlen(X)-1];
                for (int q=strlen(X)-1; q>=0; q--)
                {
                    if (q-1!=-1)X[q]=X[q-1];
                    else
                    {
                        X[0]=y;
                    }
                }
                int M=atoi(X);
                if (A<=M && M<k && M<=B  && notexist(M))
                {
                    Hechos[T]=M;
                    T++;
                }
            }
            LimpiarHechos();
        }
        printf("Case #%i: %i\n",ic,T);
    }
    return 0;
}
bool notexist(int Ra)
{
    for (int i=0; i<T; i++)
    {
        if (Hechos[i]==Ra) return false;
    }
    return true;
}

void LimpiarHechos()
{
    for (int i=0; i<T; i++)
    {
        Hechos[i]=-1;
    }
}
