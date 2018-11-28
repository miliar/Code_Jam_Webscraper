#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

#define EPS 0.000001

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {
            int pd,pg;
            long long int n;
            int r = 0;
            scanf("%lld %d %d",&n,&pd,&pg);
            if(n > 100) r = 1;
            else {
            for(int j = 1;j <= n;j++) {
                    //double p = ((double)pd)/100; 
                    
                    //if(p*j - (int)(p*j+EPS) < EPS) {
                     //   printf("j = %d\n",j);
                      //  if(j <= n) {  
                        //     r = 1;
                            
                        //}
                     //   break;
                    //}
                    if((pd*j) % 100 == 0) {
                        if(j <= n)        
                            r = 1;
                        break;  
                    }                 
            }
            }
            if(pd == 0) r = 1;
            else if(pg == 0) r = 0;        
            if(r == 1 && ( pg != 100 || pg == 100 && pd == 100) )
                 printf("Case #%d: Possible\n",i);
            else printf("Case #%d: Broken\n",i);
    
    
    
    }
    return 0;
}
