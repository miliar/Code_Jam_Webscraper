#include <cstdlib>
#include <iostream>

using namespace std;

int T, P;
int M[1024];
int D[1024];
bool seen[1024];    //All possible games
int price[1024];

int pow(int a){
    int r = 1;
    for(int i = 1; i <= a; i++) r*=2;
    return r;
}

bool check(int s, int z){
     for(int i = s; i < z; i++){
             if(D[i] >0)return true;
     }
     return false;
}

void der(int s, int z){
     for(int i = s; i < z;i++)D[i]-=1;
}
 
int main(int argc, char *argv[])
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("Solution.txt", "w", stdout);
    
    
    scanf("%d ", &T);
    
    for(int cas = 1; cas <= T; cas++){
            scanf("%d ", &P);
            
            memset(M, 0, sizeof(M));
            memset(D, 0, sizeof(D));

            for(int i = 0; i < pow(P); i++){
                    scanf("%d ", &M[i]);
                    D[i] = P - M[i];
            }  
            
            for(int i = 0; i < pow(P)-1; i++)scanf("%d ", &price[i]);  
            
            int cost = 0;
            
            for(int i = 0; i < P; i++){
                                int g = pow(i);
                                int si = pow(P) / g;
                                
                                for(int j = 0; j < g; j++){
                                        if(check(j*si, (j+1)*si)){
                                                      der(j*si, (j+1)*si);
                                                      cost+=1;
                                        }
                                } 
                        }
                        
            printf("Case #%d: %d\n",cas, cost);

    }
    
    
    
    return 0;
}
