#include <cstdlib>
#include <iostream>
#include <stdio.h>

using namespace std;


long int ex(long int *v, int N){

    int tam_vet = 21;

    long int mat[N][tam_vet];

    long int resto, div;

    int counter = 0;

    for(int i=0; i<N;i++){

        resto = v[i];

        div = v[i];

        for(int j=0; j<tam_vet;j++){
            if(div != 1){
                resto = div%2;
                div = div/2;
            }
            else{
                resto = div;
                div = 0;
            }

            mat[i][j] = resto;
        }
    }

    for(int i = 0; i<tam_vet;i++){
        int soma = 0;
        for(int j = 0; j<N;j++){
            soma += mat[j][i];
        }
        if(soma%2 == 0) counter ++;
    }

    if(counter == tam_vet){
        long int menor = 0;

        for(int i=1; i<N;i++){
            if(v[menor] <= v[i])
                menor = menor;
            else
                menor = i;
        }


        int somax = 0;
        for(int i=0; i<N;i++){
            if(i != menor)somax += v[i];
            else somax = somax;
        }

        return somax;
    }

    if(counter != tam_vet)return 0;

    return 0;

}


int main(int argc, char *argv[]){

    long int v[1000];

    int T, N;
    FILE *in;
    FILE *out;

    long int total = 0;

    in = fopen("arquivo.txt", "r");
    out = fopen("saida.txt", "w");

    fscanf(in, "%d\n", &T);

    for(int i = 0; i<T; i++){
        fscanf(in, "%d\n", &N);
        for(int j = 0; j<N; j++){
            fscanf(in, "%ld ", &v[j]);
            }
        total = ex(v, N);
        if(total == 0)fprintf(out, "Case #%d: NO\n", i+1);
        else fprintf(out, "Case #%d: %ld\n", i+1, total);

    }

    return 0;
}
