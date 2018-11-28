#include <stdio.h>
#include <stdlib.h>

int main(){
    FILE *f = fopen ("inB.txt","r");
    FILE *fo = fopen("outB.txt","w");
    
    int T ;
    fscanf(f,"%d",&T);
    for (int t = 1 ; t <= T ; t++){
        int N,S,P;
        fscanf(f,"%d %d %d",&N,&S,&P);
        int ans = 0;
        int m = 0;
        int d = 0;
        for (int n = 0 ; n < N ; n++){
            fscanf(f,"%d",&m);
           // printf("[%d ",m);
            
            d = m % 3 ;
            m /= 3;
            if (d != 0) m++;
            if (m >= P) {
                ans++;
                //printf("+");
            }
            else if (S > 0 && m < 10 && d!=1 && m > 0){
                m++;
                if (m >= P) {
                    ans++;
                    S--;
                    //printf("+");
                }
            }
            //printf("]");
        }
        fprintf(fo,"Case #%d: %d\n",t,ans);
    }
    fclose(fo);
    system("pause");
}
