#include <stdio.h>
#include <stdlib.h>

int lev[1100][3];

int main(){
    FILE *f = fopen("2.in","r");
    FILE *o = fopen("2.out","w");
    
    int T;
    fscanf(f,"%d",&T);
    for (int t = 1 ;t <= T ; t++){
        int N;
        fscanf(f,"%d",&N);
        for (int i =  0 ; i < N ;i++){
            fscanf(f,"%d %d",&lev[i][0],&lev[i][1]);
            lev[i][2] = 2;
        }
        int star = 0 ; int last = 0; int max = -1;
        int count= 0;
        while (star < N+N) {
            max = -1;
            for (int j = 0 ; j  < N ; j++){
                if (star >= lev[j][1]) {
                    if (lev[j][2] > 0) {
                        star += lev[j][2];
                        lev[j][2] = 0;
                        count++;
                    }
                } else if (star >= lev[j][0] && lev[j][2] > 1 &&(max == -1 || lev[j][1] > lev[max][1])) {
                    max = j;
                }
            }
            if (star == last) {
                if (max == -1) break;
                lev[max][2] = 1;
                star++;
                count++;
            }
            last = star;
        }
        fprintf(o,"Case #%d: ",t);
        if (star == N+N) {
            fprintf(o,"%d\n",count);
        } else {
            fprintf(o,"Too Bad\n");
        }
    }
    
    system("pause");
    fclose(f);
    fclose(o);    
}
