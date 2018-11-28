/* main.cpp */

#include <queue>

using namespace std;

int main(){
    queue<int> fila, fila2;
    int T, R, k, N;
    int p, sum;
    int i, aux;
    
    scanf("%d", &T);;
    for (i = 1; i <= T; i++){
        scanf("%d %d %d", &R, &k, &N);
        
        for( ; N > 0; N--){
             scanf("%d", &aux);
             
             fila.push(aux);
        }
        
        sum = 0;
        for ( ; R > 0; R--){
            p = 0;
            
            while (!fila2.empty()){
                  fila.push(fila2.front());
                  fila2.pop();
            }
            
            while (!fila.empty() && (p + fila.front() <= k)){
                  sum += fila.front();
                  p += fila.front();
                  
                  fila2.push(fila.front());
                  fila.pop();
            }
        }
        
        while (!fila.empty()) fila.pop();
        while (!fila2.empty()) fila2.pop();
        
        printf("Case #%d: %d\n", i, sum);
    }

    return 0;
}
