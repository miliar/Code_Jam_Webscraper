#include <stdio.h>
#include <stdlib.h>





int main (void ) {

    FILE *in = fopen("B-large.in", "r+");
    FILE *out = fopen("B-large.out","w+");
    char linha[100],C[36][3],D[28][2],N[100];
    int  tamanhoC=0,tamanhoD=0,tamanhoN=0,testes, divisao,casos;


    fscanf(in,"%[^\n]",linha);
    fgetc(in);
    testes = atoi(linha);
    printf("\n%i",testes);

for (int z=1;z<=testes;z++){

for(int t=0;t<=100;t++){
    N[t]='1';
}



    fscanf(in,"%[^' ']",linha);
    fgetc(in);
    tamanhoC = atoi(linha);


    if(tamanhoC>0){
        for(int u=0;u<tamanhoC;u++){
            fscanf(in,"%[^' ']",linha);
            C[u][0] = linha[0];
            C[u][1] = linha[1];
            C[u][2] = linha[2];
            fgetc(in);
        }
    }

    fscanf(in,"%[^' ']",linha);
    fgetc(in);
    tamanhoD = atoi(linha);


    if(tamanhoD>0){
        for(int v=0;v<tamanhoD;v++){
            fscanf(in,"%[^' ']",linha);
            D[v][0]= linha[0];
            D[v][1] =linha[1];
            fgetc(in);
        }
    }


    fscanf(in,"%[^' ']",linha);
    fgetc(in);
    tamanhoN = atoi(linha);


    if(tamanhoN>0){
        fscanf(in,"%[^\n]",linha);
        for(int g=0;g<tamanhoN;g++){
        N[g]=linha[g];
        }
        fgetc(in);
            printf("\n %i",tamanhoN);
    }




    for (int i=1;i<tamanhoN;i++){

       for(int w=0;w<tamanhoC;w++){
            if (N[i]==C[w][0] && N[i-1]==C[w][1]){
                N[i-1]='1';
                N[i]=C[w][2];
            }

            if(N[i]==C[w][1] && N[i-1]==C[w][0]){
                N[i-1]='1';
                N[i]=C[w][2];
            }
        }
       for(int p=0;p<tamanhoD;p++){
            if(N[i]==D[p][0]){
                for(int x=0;x<i;x++){
                    if(N[x]==D[p][1]){
                        for(int j=0;j<=i;j++){
                            N[j]='1';
                        }
                    }
                }
            }
            if(N[i]==D[p][1]){
                for(int x=0;x<i;x++){
                    if(N[x]==D[p][0]){
                        for(int j=0;j<=i;j++){
                            N[j]='1';
                        }
                    }
                }
            }
       }
    }

int cont = 0;
    fprintf(out,"Case #%d: [",z);
    for (int x=0;x<sizeof(N)-1;x++){
        if(N[x]!='1'&&x>0&&cont>0){
            fprintf(out,", %c",N[x]);
        }else if(N[x]!='1'&& cont==0) {
            fprintf(out,"%c",N[x]);
            cont++;
        }
    }
    if(N[sizeof(N)-1]!='1'){
        fprintf(out,"%c]\n",N[sizeof(N)-1]);
    }else{fprintf(out,"]");}
    fprintf(out,"\n");





}



    fclose(in);
    fclose(out);
}

