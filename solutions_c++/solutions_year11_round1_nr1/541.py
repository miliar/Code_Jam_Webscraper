#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <queue>
#include <map>
#include <vector>
#include <string>
#include <cctype>
#include <set>

using namespace std;

int caso, t, pd, pg;
long long n;

bool z(){
    for(int i = 1; i <= n; i++){
        for(int j = 0; j <= i; j++){
            if(j*100 == pd*i){
                return true;
            }
        }
    }
    return false;
}

int main (){
    caso = 1;
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    scanf("%d", &t);
    while(t--){
        printf("Case #%d: ", caso++);
        scanf("%lld %d %d", &n, &pd, &pg);
        if((pd < 100 && pg == 100) || (pd > 0 && pg == 0)){
            printf("Broken\n");
        }
        else{
            if(n >= 100) printf("Possible\n");
            else{
               if(z()) printf("Possible\n");
               else printf("Broken\n");
            }
            
        }
        
    }
	
    return 0;
}
