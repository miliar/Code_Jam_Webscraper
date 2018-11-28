#include <stdio.h>

int main() {
    int i,t,n,p,tt;
    FILE *ff=fopen("A-large.in","r"), *gg=fopen("A-large.out","w");

    fscanf(ff,"%d", &tt);
    for(i=1; i<=tt; i++) {
        fscanf(ff,"%d%d", &n, &t);
        if (t==0) {
           fprintf(gg,"Case #%d: OFF\n", i);
        } else {
           p=1<<(n);
           fprintf(gg,"Case #%d: ", i);
           if ( (t+1) % p == 0) fprintf(gg,"ON\n"); else fprintf(gg,"OFF\n");
        }

    }

    fclose(ff); fclose(gg);
    return 0;
}
