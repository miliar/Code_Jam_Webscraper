#include <stdio.h>
#include <stdlib.h>
int testcase;
int d[11000];
int l[11000];
int m[11000];
int main(){
    printf("hello ");
    FILE *f = fopen("a.in","r");
    FILE *o = fopen("a.out","w");
    
    // type your code here 
    fscanf(f,"%d",&testcase);
    for (int testid = 1 ; testid <= testcase ; testid++){
        fprintf(o,"Case #%d: ",testid);
        int N ,D;
        fscanf(f,"%d",&N);
        for (int n = 0 ; n< N ; n++){
            fscanf(f,"%d %d",&d[n],&l[n]);
            m[n] = 0;
        }
        fscanf(f,"%d",&D);
        m[0] = d[0];
        bool ans = 0;
        
        for (int i = 0 ;i< N ; i++ ) {
            if (d[i] + m[i] >= D) ans = 1;
            for (int j = i+1 ; j< N ;j++) {
                if (d[i]+m[i] >= d[j]) {
                    int mm = d[j] - d[i];
                    if (mm > l[j]) mm = l[j];
                    if (mm > m[j]) m[j] = mm;
                }
            }
        }
        if (ans == 1)
            fprintf(o,"YES\n");
        else fprintf(o,"NO\n");
    }
    
    fclose(f);
    fclose(o);
    printf("world\n");
    system("pause");
}
