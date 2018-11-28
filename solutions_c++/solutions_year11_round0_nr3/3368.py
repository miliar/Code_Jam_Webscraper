#include <cstdlib>
#include <iostream>

using namespace std;


long int ex(long int *v, int N){

    long int mat[N][21];
    long int resto, div;
    int counter = 0;
    int teste = 0;

    for(int i=0; i<N;i++){
        resto = v[i];
        div = v[i];
        for(int j=0; j<21;j++){
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




    for(int i = 0; i<21;i++){
        int soma = 0;
        for(int j = 0; j<N;j++){
            soma += mat[j][i];
        }
        if(soma%2 == 0) counter ++;
    }



    if(counter == 21){
        long int menor = 0;
        for(int i=1; i<N;i++){
            if(v[menor] <= v[i])menor = menor;
            else menor = i;
        }
        int somax = 0;
        for(int i=0; i<N;i++){
            if(i != menor)somax += v[i];
            else somax = somax;
        }

        return somax;
    }

    else if(counter != 21)return 0;

}



int main(int argc, char *argv[]){

    long int v[100];

    int T, N, Tot = 0;
    FILE *in;
    FILE *out;
    int teste;


    in = fopen("C-small-attempt1.in", "r");
    out = fopen("out.txt", "w");

    fscanf(in, "%d\n", &T);

    for(int i = 0; i<T; i++){
        fscanf(in, "%d\n", &N);
        for(int j = 0; j<N; j++){
            fscanf(in, "%ld ", &v[j]);
            }
        Tot = ex(v, N);
        if(Tot == 0)fprintf(out, "Case #%d: NO\n", i+1);
        else fprintf(out, "Case #%d: %d\n", i+1, Tot);
        //scanf("%d", &teste);
    }

    return 0;
}
