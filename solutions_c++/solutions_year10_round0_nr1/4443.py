#include<iostream>
using namespace std;

int main(){
    int exp2[30], testCase;
    
    exp2[0] = 1;
    for(int i = 1; i < 30; i++)
         exp2[i] = exp2[i-1]<<1;
         
    FILE* fr = fopen("A-small-attempt0.in.txt", "r");
    FILE* fw = fopen("a_small.txt", "w");
    
    fscanf(fr, "%d", &testCase);

    for(int i = 0; i < testCase; i++){
        int n, k;
        fscanf(fr, "%d %d", &n, &k);
        
        if((k+1) % exp2[n] == 0)
            fprintf(fw, "Case #%d: ON\n", i+1);
        else
            fprintf(fw, "Case #%d: OFF\n", i+1);
    }
    
    fclose(fr);
    fclose(fw);
    
    system("pause");
    return 0;
}
