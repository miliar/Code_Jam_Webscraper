#include <iostream>
#include <string>
#include <cmath>
using namespace std;

const int MAXN = 1000+10;
long long n, N, D, PD, PG, tests, test;
bool ans; 

int main(){
    freopen("1.in","r",stdin); 
    freopen("1.out","w",stdout);

    scanf("%d",&tests);
     
    for (test = 1; test <= tests; ++test){
        scanf("%d %d %d", &N, &PD, &PG); 
        
        ans = false; 
        
        if ((PG == 100 && PD != 100) || (PD != 0 && PG == 0)){
             ans = false; 
        } else {
        
		for (long long n = 1; n <= N; ++n ) {
            D = n * PD; 
            if (D % 100 == 0) {
                //cout << n << '\t' << PD << "\t" << D << endl; 
                ans = true; 
                break; 
            }
            if (n > 10000000) break; 
        }
        }
        
        if (ans)
		  printf("Case #%d: Possible\n", test);
        else
          printf("Case #%d: Broken\n", test);

    }   
     
    return 0;  
}
