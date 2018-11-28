#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int main() {
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i++) {        
        int n;
        char r; int p;
        int to = 0,po = 1,pb = 1,tb = 0;
        int too = 0, tbb = 0;
        int total = 0;
        char lastcmd = 'X';
        scanf("%d",&n);    
        for(int j = 0;j < n;j++) {
            scanf(" %c %d",&r,&p);
            if(r == 'O') { 
                 if(lastcmd == 'B') {
                      to = abs(p - po) + 1;
                      if(to <= tbb) {
                            total += 1;
                            too = 1;
                      }
                      else if(to > tbb) {
                           total += to - tbb;
                           too = to - tbb;     
                      }                
                 }
                 else {
                      to = abs(p - po) + 1;
                      total += to;
                      too += to;
                 }
                 po = p;
                 lastcmd = 'O'; 
            }
            else if(r == 'B') { 
                 if(lastcmd == 'O') {
                      tb = abs(p - pb) + 1;
                      if(tb <= too) {
                            total += 1;
                            tbb = 1;
                      }
                      else if(tb > too) {
                           total += tb - too;
                           tbb = tb - too;     
                      }               
                 }
                 else {
                      tb = abs(p - pb) + 1;
                      total += tb;
                      tbb += tb;     
                 }
                 pb = p;
                 lastcmd = 'B'; 
            }    

        }
        printf("Case #%d: %d\n",i,total);        
                    
    }            
    
    return 0;
}
