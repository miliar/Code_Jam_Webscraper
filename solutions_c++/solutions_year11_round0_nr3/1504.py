#include<stdio.h>
#include<vector>

using namespace std;

int main(){
    int T, g, N, h;
    int i, k;
    vector<int> x;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        x.clear();
        scanf("%d ", &N);
        for(h=0; h<N; h++){
            int a;
            scanf("%d ", &a);
            x.push_back(a);
        }
    
        k = x.size();
        int soma = 0;
        for(i=0; i<k; i++){
            soma = soma ^ x[i];
           // printf("i=%d, x[i]=%d, soma=%d\n", i, x[i], soma);
        }
        //printf("soma = %d\n", soma);
        printf("Case #%d: ", g);
        if(soma!=0){
            printf("NO\n");
            continue;
        }
        int minimo = 2000000;
        int yes=0;
        for(i=0; i<k; i++){
            if(x[i] < minimo)
                minimo=x[i];
            yes += x[i];
        }
        //printf("yes =%d, minimo=%d\n", yes, minimo);
        printf("%d\n", yes-minimo);
    }
    return 0;
}
