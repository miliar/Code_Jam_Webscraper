        #include <cstdlib>
        #include <iostream>
        
        using namespace std;
        const int VET_SIZE=21;
        
        long int solve(long int *v, int N){
                long int table[N][VET_SIZE];
            long int resto, divisao;
            int counter = 0;
               for(int i=0; i<N;i++){
                resto = v[i];
                divisao = v[i];
                for(int j=0; j<VET_SIZE;j++){
                    if(divisao != 1){
                        resto = divisao%2;
                        divisao = divisao/2;
                    }
                    else{
                        resto = divisao;
                        divisao = 0;
                    }
                        table[i][j] = resto;
                }
            }
                for(int i = 0; i<VET_SIZE;i++){
                int soma = 0;
                for(int j = 0; j<N;j++){
                    soma += table[j][i];
                }
                if(soma%2 == 0) counter ++;
            }
                if(counter == VET_SIZE){
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
        
            else if(counter != VET_SIZE)return 0;
        
        }
        
        
        int main(int argc, char *argv[]){
        
            long int v[1000];
        
            int T, N;
            FILE *in;
            FILE *out;
            long int Final = 0;
        
            in = fopen("C-large.in", "r");
            out = fopen("saida.txt", "w");
        
            fscanf(in, "%d\n", &T);
        /*Inicia o For*/
            for(int i = 0; i<T; i++){
                fscanf(in, "%d\n", &N);
                for(int j = 0; j<N; j++){
                    fscanf(in, "%ld ", &v[j]);
                    }
                Final = solve(v, N);
                //Finaliza com a resposta
                if(Final == 0)fprintf(out, "Case #%d: NO\n", i+1);
                else fprintf(out, "Case #%d: %d\n", i+1, Final);
        
            }
        
            return 0;
        }
