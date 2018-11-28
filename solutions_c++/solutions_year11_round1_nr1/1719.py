#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		
        int N, PD, PG;
        scanf("%d %d %d", &N, &PD, &PG);

       //printf("N=%d, PD=%d, PG=%d\n",N,PD,PG);
        
        if ((PG==100 && PD<100) || (PG==0 && PD>0))  {
            printf("Broken\n");
            continue;
        
        }else if(PD==0 && PG==0){
            printf("Possible\n");
            continue;
        
        }else{
            bool broken = true;
            for (int played = 1; played<=N; played++){
            
                if((played * PD) % 100 == 0){
                    
                    //int won = (played * PD) / 100;
                    
                    //printf("played=%d, won=%d, PG=%d\n",played,won,PG);
                    
                    //if ( won * 100 / PG >= played) {
                        broken=false;
                        break;
                    //}
                    
                }
            }
            printf(broken?"Broken\n":"Possible\n");
        }
        
	}
    
	return 0;
}