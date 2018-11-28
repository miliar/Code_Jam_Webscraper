#include <stdio.h>
#include <math.h>

using namespace std;

int main(){
    FILE* finput;
    FILE* foutput;
    finput = fopen("A-large.in", "r");
    foutput = fopen("A-large.out", "w");

    int t, n, k, pot;
    fscanf(finput, "%d", &t);

    for(int x=1;x<=t;x++){
        fscanf(finput, "%d %d", &n, &k);
        pot = pow(2, n);
        fprintf(foutput, "Case #%d: ", x);
        if(k%pot == pot-1){
            fprintf(foutput, "ON\n");
        } else {
            fprintf(foutput, "OFF\n");
        }
    }

    fclose(finput);
    fclose(foutput);

}
