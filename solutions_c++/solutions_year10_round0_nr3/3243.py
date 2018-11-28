#include <stdio.h>
#include <queue>

using namespace std;

int main(){
    queue<int> cola;
    queue<int> enCurso;

    FILE* finput;
    FILE* foutput;
    finput = fopen("C-small-attempt0.in", "r");
    foutput = fopen("C-small-attempt0.out", "w");

    int t, r, k, n, temp, suma, total, tamPar;
    fscanf(finput, "%d", &t);
    for(int x=1; x<=t; x++){
        fscanf(finput, "%d %d %d", &r, &k, &n);
        total = 0;

        for(int i=0;i<n;i++){
            fscanf(finput, "%d", &temp);
            cola.push(temp);
        }

        for(int i=0;i<r;i++){

            suma=0;

            while(!cola.empty() && suma+cola.front()<=k){

                temp=cola.front();
                cola.pop();
                suma += temp;
                enCurso.push(temp);

            }
            total+=suma;
            tamPar = enCurso.size();
            for(int j=0;j<tamPar;j++){
                temp = enCurso.front();
                enCurso.pop();
                cola.push(temp);

            }
        }
        fprintf(foutput, "Case #%d: %d\n", x, total);
        tamPar = cola.size();
        for(int j=0;j<tamPar;j++){
            cola.pop();
        }

    }

    fclose(finput);
    fclose(foutput);


}
