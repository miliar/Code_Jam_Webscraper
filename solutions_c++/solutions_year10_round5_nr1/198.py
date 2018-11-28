

#include <cstdio>

const int
    MAXD = 10000,
    SQRT_MAXD = 100,
    POWERS[] = {1, 10, 100, 1000, 10000};

int T, tc, cant_primes, D, K;
bool mark[MAXD];
int primes[MAXD], vals[20]; 

int main(){

    for (int i = 2; i < SQRT_MAXD; i++)
        if (!mark[i])
            for (int j = i * i; j < MAXD; j += i)
                mark[j] = true;
                
    for (int i = 2; i < MAXD; i++)
        if (!mark[i]){
            primes[cant_primes++] = i;
            //printf("%d\n", primes[cant_primes - 1]);
        }    

    //printf("cant_primes = %d\n", cant_primes);
    //return 0;

    scanf("%d", &T);
    
    for (tc = 1; tc <= T; tc++){
    
        int sol = -1, max_val = -1;        
        
        scanf("%d %d", &D, &K);
        
        //printf("D = %d POWERS[D] = %d\n", D, POWERS[D]);
        
        for (int i = 0; i < K; i++){
            scanf("%d", &vals[i]);
            if (vals[i] > max_val) max_val = vals[i];
        }
        
        int pos = 0;
        
        while (primes[pos] <= max_val) pos++;
        
        if (K != 1){
        
        //printf("HERE\n");
        
        for (int p = pos; p < cant_primes && primes[p] < POWERS[D]; p++){
            int pr = primes[p];
            //tf("pr = %d\n", pr);
            for (int a = 0; a < pr; a++){
            
                int b = ((vals[1] - a * vals[0]) % pr + pr) % pr;
                
                    bool err = false;
                    
                    int s = vals[0];
                    for (int i = 1; i < K; i++){
                        int ns = (a * s + b) % pr;
                        if (ns != vals[i]){
                            err = true;
                            break;
                        }
                        s = ns;
                    }
                    
                    
                    if (!err){
                    
                        s = (a * s + b) % pr;
                        
                        //printf("here a = %d b = %d s = %d\n", a, b, s);
                        
                    
                        if (sol == -1){
                            sol = s;
                        } else if (s != sol){
                            sol = -1;
                            a = p;
                            p = cant_primes;
                            break;
                        }
                     }
 
            
            }
        }
        
        }
        
        else{
        
                for (int p = pos; p < cant_primes && primes[p] < POWERS[D]; p++){
            int pr = primes[p];
            //printf("pr = %d\n", pr);
            for (int a = 0; a < pr; a++)
                for (int b = 0; b < pr; b++){
                
                    bool err = false;
                    
                    int s = vals[0];
                    for (int i = 1; i < K; i++){
                        int ns = (a * s + b) % pr;
                        if (ns != vals[i]){
                            err = true;
                            break;
                        }
                        s = ns;
                    }
                    
                    
                    if (!err){
                    
                        s = (a * s + b) % pr;
                        
                        //printf("here a = %d b = %d s = %d\n", a, b, s);
                        
                    
                        if (sol == -1){
                            sol = s;
                        } else if (s != sol){
                            sol = -1;
                            a = p;
                            p = cant_primes;
                            break;
                        }
                        
                        
                    
                    }
                    
                }
        }     

        
        }
 
 
 
         
        printf("Case #%d: ", tc);
        
        if (sol != -1) printf("%d\n", sol);
        else printf("I don't know.\n");
    
    }

    return 0;
}
