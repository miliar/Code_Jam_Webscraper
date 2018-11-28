#include <iostream>
#include <algorithm>

using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T,PD,PG;
    long long N;
    
    cin >> T;
    
    for(int tc = 1;tc <= T;++tc){
        cin >> N >> PD >> PG;
        
        printf("Case #%d: ",tc);
        
        bool poss = false;
        
        if(PG == 100){
            if(PD == 100) poss = true;
        }else if(PG == 0){
            if(PD == 0) poss = true;
        }else{
            int x = 100 / __gcd(100,PD);
            
            if(x <= N) poss = true;
        }
        
        if(poss) printf("Possible\n");
        else printf("Broken\n");
    }
    
    return 0;
}
