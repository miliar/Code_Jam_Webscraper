#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>

using namespace std;

#define TAM 1024


int main(){
    int nt;
    int candy[TAM];
    FILE *fin = fopen("entree.txt","r");
    FILE *fout = fopen("sortie.txt","w");
    fscanf(fin,"%d",&nt);

    for(int t = 1 ; t <= nt ; t++){
        int n;
        fscanf(fin,"%d",&n);
        for(int i = 0 ; i < n ; i++) fscanf(fin,"%d",&candy[i]);

        int ans = -1;
        for(int i = 1 ; i < 1 << n - 1; i++){
            int k = i;
            int soma1 = 0;
            int x1 = 0;
            int x2 = 0;
            int soma2 = 0;
            //printf("%d\n",k);
            for(int j = 0 ; j < n ; j ++){
                //printf(" %d %d",k&1,candy[j]);
                if(k%2 == 0){
                    soma1 = (soma1 | candy[j]) - (soma1 & candy[j]);
                    x1 += candy[j];
                }
                else{
                    soma2 = (soma2 | candy[j]) - (soma2 & candy[j]);
                    x2 += candy[j];
                }
                //printf("%d %d\n",soma1,soma2);
                k/=2;
            }
            //printf("\n\n\n\n");
            //printf("%d %d\n",soma1,soma2);
            if(soma1 == soma2) ans = max(ans,max(x1,x2));
        }
        fprintf(fout,"Case #%d:",t);
        if(ans == - 1) fprintf(fout," NO\n");
        else fprintf(fout," %d\n",ans);
    }
    return 0;
}
