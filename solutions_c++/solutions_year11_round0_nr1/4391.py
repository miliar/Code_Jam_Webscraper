#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main(){
    FILE *fin = fopen("entree.txt","r");
    FILE *fout = fopen("sortie.txt","w");

    int nt;
    fscanf(fin,"%d",&nt);
    for(int t = 1 ; t<=nt ; t++){
        int k;
        fscanf(fin, "%d",&k);

        char c;
        int btp;
        int ans = 0;

        int bp,op,bdelta,odelta;
        bp = op = 1;
        bdelta = odelta = 0;

        for(int pas = 1 ; pas <= k ; pas++){
            fscanf(fin, " %c %d",&c,&btp);
            if(c == 'O'){
                ans += max(abs(btp - op) - odelta,0) + 1 ;
                bdelta += max(abs(btp - op) - odelta,0) + 1;
                odelta = 0;
                op = btp;
            }
            if(c == 'B'){
                ans += max(abs(btp - bp) - bdelta,0) + 1;
                odelta += max(abs(btp - bp) - bdelta,0) + 1;
                bdelta = 0;
                bp = btp;
            }
        }

        fprintf(fout,"Case #%d: %d\n",t,ans);

    }

    fclose(fout);
    fclose(fin);
    return 0;

}
